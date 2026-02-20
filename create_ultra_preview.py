#!/usr/bin/env python3
"""Create compressed preview of ULTRA video 001"""

from moviepy import VideoFileClip
from pathlib import Path

input_path = Path("content/videos_ultra/tiktok_001_ULTRA.mp4")
output_path = Path("content/videos_ultra/tiktok_001_ULTRA_preview.mp4")

print("🎬 Loading ULTRA video (67 MB)...")
video = VideoFileClip(str(input_path))

print("📐 Creating 30-sec preview...")
# Take first 30 seconds, lower res for Telegram
preview = video.subclipped(0, 30).resized(height=960)

print("💾 Exporting preview...")
preview.write_videofile(
    str(output_path),
    fps=30,  # Lower FPS for smaller file
    codec='libx264',
    audio_codec='aac',
    bitrate='1000k',
    temp_audiofile='temp-audio.m4a',
    remove_temp=True,
    logger=None
)

video.close()
preview.close()

size = output_path.stat().st_size / (1024*1024)
print(f"✅ ULTRA Preview created! Size: {size:.1f} MB")
