#!/usr/bin/env python3
"""Create viewable compressed version of ULTRA video 001"""

from moviepy import VideoFileClip
from pathlib import Path

input_path = Path("content/videos_ultra/tiktok_001_ULTRA.mp4")
output_path = Path("content/videos_ultra/tiktok_001_ULTRA_for_telegram.mp4")

print("🎬 Loading ULTRA video (67 MB)...")
video = VideoFileClip(str(input_path))

print("📐 Compressing for Telegram viewing...")
# 720p, 30fps, lower bitrate but still good quality
compressed = video.resized(height=1280).with_fps(30)

print("💾 Exporting viewable version...")
compressed.write_videofile(
    str(output_path),
    fps=30,
    codec='libx264',
    audio_codec='aac',
    bitrate='4000k',  # 4 Mbps - good quality, smaller size
    temp_audiofile='temp-audio.m4a',
    remove_temp=True,
    logger=None
)

video.close()
compressed.close()

size = output_path.stat().st_size / (1024*1024)
print(f"✅ Viewable version created! Size: {size:.1f} MB")
