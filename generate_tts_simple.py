#!/usr/bin/env python3
"""
Simple TTS Generator using Edge-TTS
No subtitle generation - just audio
"""

import sys
import asyncio
import edge_tts
from pathlib import Path

sys.path.insert(0, 'C:\\Users\\field\\.openclaw\\workspace')

async def generate_simple_tts(text: str, output_path: str, voice: str = "en-US-GuyNeural", rate: str = "+10%"):
    """Simple TTS generation without subtitles."""
    
    print(f"🎙️  Generating {len(text)} chars with {voice} at {rate}...")
    
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(output_path)
    
    print(f"✅ Saved: {output_path}")
    return output_path

async def main():
    """Generate TTS for all package scripts."""
    
    import json
    
    print("🎬 Generating TTS audio files...\n")
    
    projects_dir = Path("projects")
    packages = [d for d in projects_dir.iterdir() if d.is_dir() and "2026-02-20" in d.name and "My_" in d.name]
    
    print(f"Found {len(packages)} video packages\n")
    
    audio_files = []
    
    for package in packages:
        script_path = package / "script.json"
        if not script_path.exists():
            print(f"⚠️ Skipping {package.name} (no script.json)")
            continue
        
        with open(script_path, 'r') as f:
            script = json.load(f)
        
        print(f"\n📄 {script['hook'][:50]}...")
        
        # Build text
        parts = [script['hook']]
        parts.extend(script['context'])
        for beat in script['escalation']:
            parts.append(beat['text'])
        parts.append(script['twist'])
        parts.append(script['cliffhanger'])
        
        full_text = " ".join(parts)
        
        # Generate TTS
        output_path = package / "audio.mp3"
        
        try:
            await generate_simple_tts(full_text, str(output_path))
            audio_files.append(str(output_path))
        except Exception as e:
            print(f"❌ Failed: {e}")
            continue
    
    print(f"\n🎉 Generated {len(audio_files)} audio files!")
    
    # Save manifest
    manifest = {
        "date": "2026-02-20",
        "videos": len(audio_files),
        "packages": [Path(a).parent.name for a in audio_files],
        "status": "READY_FOR_CAPCUT"
    }
    
    with open("projects/BATCH_COMPLETE.json", 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"✅ Complete! Check projects/BATCH_COMPLETE.json")

if __name__ == "__main__":
    asyncio.run(main())
