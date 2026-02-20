#!/usr/bin/env python3
"""Generate videos 005-009"""

import os
from pathlib import Path
from moviepy import VideoFileClip, AudioFileClip

OUTPUT_DIR = Path("content/videos")
VOICEOVER_DIR = Path("content/voiceovers")
GAMEPLAY_DIR = Path("content/gameplay")

OUTPUT_DIR.mkdir(exist_ok=True)

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
VIDEO_DURATION = 60

def generate_video(script_num, script_name, gameplay_file, voiceover_file, output_name):
    print(f"\n🎬 Video {script_num}: {script_name}")
    
    gameplay_path = GAMEPLAY_DIR / gameplay_file
    voiceover_path = VOICEOVER_DIR / voiceover_file
    output_path = OUTPUT_DIR / f"{output_name}.mp4"
    
    if output_path.exists() and output_path.stat().st_size > 10000000:
        print(f"  ✅ Already exists ({output_path.stat().st_size/1024/1024:.1f} MB), skipping")
        return True
    
    if not gameplay_path.exists():
        print(f"  ❌ Gameplay not found: {gameplay_path}")
        return False
    
    if not voiceover_path.exists():
        print(f"  ❌ Voiceover not found: {voiceover_path}")
        return False
    
    try:
        print(f"  📹 Loading gameplay...")
        video = VideoFileClip(str(gameplay_path))
        
        print(f"  ⏱️ Duration: {video.duration:.1f}s")
        
        if video.duration < VIDEO_DURATION:
            video = video.with_duration(VIDEO_DURATION).fx("vfx.loop", duration=VIDEO_DURATION)
        else:
            video = video.subclipped(0, VIDEO_DURATION)
        
        print(f"  📐 Resizing to {VIDEO_WIDTH}x{VIDEO_HEIGHT}...")
        video = video.resized(new_size=(VIDEO_WIDTH, VIDEO_HEIGHT))
        
        print(f"  🎙️ Loading audio...")
        audio = AudioFileClip(str(voiceover_path))
        if audio.duration > VIDEO_DURATION:
            audio = audio.subclipped(0, VIDEO_DURATION)
        
        video = video.with_audio(audio)
        
        print(f"  💾 Exporting (this takes ~3-4 min)...")
        video.write_videofile(
            str(output_path),
            fps=30,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True,
            logger=None
        )
        
        video.close()
        audio.close()
        
        size = output_path.stat().st_size / (1024*1024)
        print(f"  ✅ DONE! ({size:.1f} MB)")
        return True
        
    except Exception as e:
        print(f"  ❌ Error: {str(e)[:80]}")
        import traceback
        traceback.print_exc()
        return False

# Videos 005-009
videos = [
    (5, "Roommate Adderall", "gta_driving.mp4", "voiceover_005_roommate_adderall.mp3", "tiktok_005_roommate_adderall"),
    (6, "Other Woman", "minecraft_parkour.mp4", "voiceover_006_other_woman.mp3", "tiktok_006_other_woman"),
    (7, "Landlord TikTok", "subway_surfers.mp4", "voiceover_007_landlord_tiktok_gtts.mp3", "tiktok_007_landlord_tiktok"),
    (8, "Professor Dark Web", "gta_driving.mp4", "voiceover_008_professor_darkweb_gtts.mp3", "tiktok_008_professor_darkweb"),
    (9, "Online Friend/Dad", "minecraft_parkour.mp4", "voiceover_009_online_friend_dad_gtts.mp3", "tiktok_009_online_friend_dad"),
]

print("="*60)
print("🎬 GENERATING VIDEOS 005-009")
print("="*60)

success = 0
for v in videos:
    if generate_video(*v):
        success += 1
    print()

print("="*60)
print(f"🎉 COMPLETE: {success}/5 videos generated!")
print(f"📁 Location: {OUTPUT_DIR}/")
print("="*60)
