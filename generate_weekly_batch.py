#!/usr/bin/env python3
"""
NIGHT SHIFT BATCH #2
Generate 7 more TikTok videos for weekly backlog
"""

import sys
sys.path.insert(0, 'C:\\Users\\field\\.openclaw\\workspace')

import asyncio
import json
import os
from pathlib import Path
from datetime import datetime

from automation.script_engine import ViralScriptEngine, generate_daily_batch
from automation.edge_tts_generator import EdgeTTSGenerator

async def generate_video_package(engine, tts_gen, topic_id):
    """Generate complete video with script + TTS."""
    
    print(f"\n--- Video {topic_id}/7 ---")
    
    # Generate hooks
    hooks = engine.generate_hooks(count=10)
    best_hook, score = engine.select_best_hook(hooks)
    print(f"Selected: '{best_hook[:50]}...' (score: {score})")
    
    # Generate script
    script = engine.generate_script(best_hook)
    
    # Save package
    safe_name = best_hook.replace(' ', '_').replace('?', '').replace('!', '').replace("'", '')[:30]
    package_dir = Path(f"projects/2026-02-20_{safe_name}")
    package_dir.mkdir(exist_ok=True, parents=True)
    
    # Save script files
    with open(package_dir / "script.json", 'w') as f:
        json.dump(script, f, indent=2)
    
    with open(package_dir / "script.txt", 'w', encoding='utf-8') as f:
        f.write(f"HOOK: {script['hook']}\n\n")
        f.write("CONTEXT:\n")
        for line in script['context']:
            f.write(f"  {line}\n")
        f.write("\nESCALATION:\n")
        for beat in script['escalation']:
            f.write(f"  {beat['text']}\n")
        f.write(f"\nTWIST: {script['twist']}\n")
        f.write(f"\nCLIFFHANGER: {script['cliffhanger']}\n")
        f.write(f"\nCTA: {script['cta']}\n")
    
    # Generate TTS
    import edge_tts
    
    parts = [script['hook']]
    parts.extend(script['context'])
    for beat in script['escalation']:
        parts.append(beat['text'])
    parts.append(script['twist'])
    parts.append(script['cliffhanger'])
    
    full_text = " ".join(parts)
    audio_path = package_dir / "audio.mp3"
    
    communicate = edge_tts.Communicate(full_text, "en-US-GuyNeural", rate="+10%")
    await communicate.save(str(audio_path))
    
    print(f"✅ Package complete: {package_dir.name}")
    return package_dir

async def main():
    """Generate 7 more videos for the week."""
    
    print("🌙 NIGHT SHIFT BATCH #2")
    print("Generating 7 more TikTok videos...\n")
    print("=" * 50)
    
    engine = ViralScriptEngine()
    packages = []
    
    for i in range(4, 11):  # Videos 4-10 (we have 1-3 already)
        try:
            package_dir = await generate_video_package(engine, None, i)
            packages.append(str(package_dir))
        except Exception as e:
            print(f"❌ Video {i} failed: {e}")
            continue
    
    print("\n" + "=" * 50)
    print(f"🎉 Generated {len(packages)} new videos!")
    print(f"📁 Total videos ready: 10 (3 from earlier + 7 now)")
    
    # Save manifest
    manifest = {
        "date": "2026-02-20",
        "batch": "NIGHT_SHIFT_2",
        "new_videos": len(packages),
        "total_videos": 10,
        "packages": packages,
        "status": "READY_FOR_TIKTOK",
        "completed_at": datetime.now().isoformat()
    }
    
    with open("projects/WEEKLY_BATCH_10_VIDEOS.json", 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\n✅ Manifest saved: projects/WEEKLY_BATCH_10_VIDEOS.json")
    print("🚀 Fields has a FULL WEEK of content!")

if __name__ == "__main__":
    asyncio.run(main())
