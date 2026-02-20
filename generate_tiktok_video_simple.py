#!/usr/bin/env python3
"""
🎬 SIMPLE TikTok Video Generator
Generates video with gameplay + voiceover + captions
"""

import os
from pathlib import Path

# Paths
OUTPUT_DIR = Path("content/videos")
VOICEOVER_DIR = Path("content/voiceovers")
GAMEPLAY_DIR = Path("content/gameplay")

OUTPUT_DIR.mkdir(exist_ok=True)

# Video config
VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
VIDEO_DURATION = 60

def generate_video(script_num, script_name, gameplay_file, voiceover_file, output_name):
    """Generate a single TikTok video"""
    
    print(f"\n🎬 Generating Video {script_num}: {script_name}")
    print("="*60)
    
    # Check files exist
    gameplay_path = GAMEPLAY_DIR / gameplay_file
    voiceover_path = VOICEOVER_DIR / voiceover_file
    
    if not gameplay_path.exists():
        print(f"❌ Gameplay not found: {gameplay_path}")
        return False
    
    if not voiceover_path.exists():
        print(f"❌ Voiceover not found: {voiceover_path}")
        return False
    
    print(f"✅ Gameplay: {gameplay_path}")
    print(f"✅ Voiceover: {voiceover_path}")
    
    # Try to generate with moviepy
    try:
        print("📹 Loading moviepy...")
        
        # Try different import styles
        try:
            from moviepy import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip, ColorClip
            from moviepy import vfx
            print("✅ Using moviepy 2.x API")
        except ImportError:
            from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip, ColorClip
            print("✅ Using moviepy 1.x API")
        
        # Load gameplay
        print("📹 Loading gameplay footage...")
        video = VideoFileClip(str(gameplay_path))
        
        # Trim/loop to 60 seconds
        if video.duration < VIDEO_DURATION:
            print(f"⏱️ Looping video ({video.duration}s → {VIDEO_DURATION}s)")
            video = video.loop(duration=VIDEO_DURATION)
        else:
            video = video.subclipped(0, VIDEO_DURATION)
        
        # Resize to 9:16
        print(f"📐 Resizing to {VIDEO_WIDTH}x{VIDEO_HEIGHT}...")
        try:
            # Try moviepy 2.x way
            video = video.resized(width=VIDEO_WIDTH, height=VIDEO_HEIGHT)
        except AttributeError:
            try:
                # Try another way
                video = video.resize(newsize=(VIDEO_WIDTH, VIDEO_HEIGHT))
            except:
                print("⚠️ Using ffmpeg for resize instead...")
                # Will use ffmpeg command line as fallback
                return generate_with_ffmpeg(script_num, script_name, gameplay_path, voiceover_path, output_name)
        
        # Load audio
        print("🎙️ Adding voiceover...")
        audio = AudioFileClip(str(voiceover_path))
        
        # Trim audio to video length
        if audio.duration > VIDEO_DURATION:
            audio = audio.subclipped(0, VIDEO_DURATION)
        
        # Set audio to video
        video = video.with_audio(audio)
        
        # Export
        output_path = OUTPUT_DIR / f"{output_name}.mp4"
        print(f"💾 Exporting: {output_path}")
        
        video.write_videofile(
            str(output_path),
            fps=30,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True
        )
        
        print(f"✅ VIDEO COMPLETE: {output_path}")
        video.close()
        audio.close()
        
        return True
        
    except Exception as e:
        print(f"❌ Moviepy error: {e}")
        print("🔄 Falling back to ffmpeg...")
        return generate_with_ffmpeg(script_num, script_name, gameplay_path, voiceover_path, output_name)

def generate_with_ffmpeg(script_num, script_name, gameplay_path, voiceover_path, output_name):
    """Fallback: Use ffmpeg directly"""
    
    output_path = OUTPUT_DIR / f"{output_name}_ffmpeg.mp4"
    
    # ffmpeg command to combine video + audio
    cmd = [
        "ffmpeg", "-y",
        "-i", str(gameplay_path),
        "-i", str(voiceover_path),
        "-vf", f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}:force_original_aspect_ratio=decrease,pad={VIDEO_WIDTH}:{VIDEO_HEIGHT}:(ow-iw)/2:(oh-ih)/2",
        "-c:v", "libx264",
        "-t", str(VIDEO_DURATION),
        "-shortest",
        str(output_path)
    ]
    
    print(f"🎬 Running ffmpeg...")
    import subprocess
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ VIDEO COMPLETE: {output_path}")
        return True
    else:
        print(f"❌ ffmpeg failed: {result.stderr[:200]}")
        return False

# Generate all 9 videos
videos = [
    (1, "Girlfriend's Sister", "subway_surfers.mp4", "voiceover_001_girlfriend_sister.mp3", "tiktok_001_girlfriend_sister"),
    (2, "Boss Affair", "gta_driving.mp4", "voiceover_002_boss_affair.mp3", "tiktok_002_boss_affair"),
    (3, "Fired Revelation", "minecraft_parkour.mp4", "voiceover_003_fired_revelation.mp3", "tiktok_003_fired_revelation"),
    (4, "Money Hustle", "subway_surfers.mp4", "voiceover_004_money_hustle.mp3", "tiktok_004_money_hustle"),
    (5, "Roommate Adderall", "gta_driving.mp4", "voiceover_005_roommate_adderall.mp3", "tiktok_005_roommate_adderall"),
    (6, "Other Woman", "minecraft_parkour.mp4", "voiceover_006_other_woman.mp3", "tiktok_006_other_woman"),
    (7, "Landlord TikTok", "subway_surfers.mp4", "voiceover_007_landlord_tiktok_gtts.mp3", "tiktok_007_landlord_tiktok"),
    (8, "Professor Dark Web", "gta_driving.mp4", "voiceover_008_professor_darkweb_gtts.mp3", "tiktok_008_professor_darkweb"),
    (9, "Online Friend/Dad", "minecraft_parkour.mp4", "voiceover_009_online_friend_dad_gtts.mp3", "tiktok_009_online_friend_dad"),
]

print("🎬 TIKTOK VIDEO GENERATOR - BATCH MODE")
print("="*60)
print(f"Generating {len(videos)} videos...\n")

success_count = 0
for video_data in videos:
    if generate_video(*video_data):
        success_count += 1
    print()

print("="*60)
print(f"🎉 BATCH COMPLETE: {success_count}/{len(videos)} videos generated!")
print(f"📁 Location: {OUTPUT_DIR}/")
