#!/usr/bin/env python3
"""
Generate TTS for all scripts in batch
Uses Edge-TTS (free, no API key)
"""

import sys
import asyncio
import json
from pathlib import Path

sys.path.insert(0, 'C:\\Users\\field\\.openclaw\\workspace')

from automation.edge_tts_generator import EdgeTTSGenerator

async def generate_tts_for_package(package_dir: Path):
    """Generate TTS audio for a single video package."""
    
    # Load script
    script_path = package_dir / "script.json"
    if not script_path.exists():
        print(f"❌ No script.json found in {package_dir}")
        return
    
    with open(script_path, 'r') as f:
        script = json.load(f)
    
    print(f"\n🎙️ Generating TTS for: {script['hook'][:40]}...")
    
    # Build full text
    parts = [script['hook']]
    parts.extend(script['context'])
    for beat in script['escalation']:
        parts.append(beat['text'])
    parts.append(script['twist'])
    parts.append(script['cliffhanger'])
    
    full_text = " ".join(parts)
    
    # Generate TTS
    output_path = package_dir / "audio.mp3"
    
    generator = EdgeTTSGenerator()
    await generator.generate_tts(
        text=full_text,
        output_path=str(output_path),
        voice="en-US-GuyNeural",
        rate="+10%",
        write_subtitles=True
    )
    
    print(f"✅ Audio saved: {output_path}")
    return output_path

async def main():
    """Generate TTS for all packages."""
    
    print("🎬 Generating TTS for all video packages...\n")
    
    # Find all packages from today
    projects_dir = Path("projects")
    packages = [d for d in projects_dir.iterdir() if d.is_dir() and "2026-02-20" in d.name]
    
    print(f"Found {len(packages)} packages\n")
    
    audio_files = []
    for package in packages:
        audio_path = await generate_tts_for_package(package)
        if audio_path:
            audio_files.append(str(audio_path))
    
    print(f"\n🎉 Generated TTS for {len(audio_files)} videos!")
    print("📁 Files:")
    for f in audio_files:
        print(f"  - {f}")
    
    # Save manifest
    manifest = {
        "date": "2026-02-20",
        "videos": len(audio_files),
        "audio_files": audio_files,
        "voice": "en-US-GuyNeural",
        "rate": "+10%",
        "status": "READY_FOR_CAPCUT"
    }
    
    with open("projects/NIGHT_BATCH_MANIFEST.json", 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\n✅ Manifest saved: projects/NIGHT_BATCH_MANIFEST.json")

if __name__ == "__main__":
    asyncio.run(main())
