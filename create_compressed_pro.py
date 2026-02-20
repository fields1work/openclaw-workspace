#!/usr/bin/env python3
"""Create compressed version of PRO video 001 for Telegram"""

from moviepy import VideoFileClip
from pathlib import Path

input_path = Path("content/videos_pro/tiktok_001_PRO.mp4")
output_path = Path("content/videos_pro/tiktok_001_PRO_compressed.mp4")

print("🎬 Loading PRO video (58 MB)...")
video = VideoFileClip(str(input_path))

print("📐 Compressing for Telegram (target: under 16 MB)...")
# Lower resolution, lower bitrate, 30fps instead of 60
compressed = video.resized(height=720).with_fps(30)

print("💾 Exporting compressed version...")
compressed.write_videofile(
    str(output_path),
    fps=30,
    codec='libx264',
    audio_codec='aac',
    bitrate='1500k',
    temp_audiofile='temp-audio.m4a',
    remove_temp=True,
    logger=None
)

video.close()
compressed.close()

size = output_path.stat().st_size / (1024*1024)
print(f"✅ Compressed video created! Size: {size:.1f} MB")
