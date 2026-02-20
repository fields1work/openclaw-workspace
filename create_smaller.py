#!/usr/bin/env python3
"""Create smaller version for Telegram"""

from moviepy import VideoFileClip
from pathlib import Path

input_path = Path("content/videos_ultra/tiktok_001_ULTRA.mp4")
output_path = Path("content/videos_ultra/tiktok_001_ULTRA_viewable.mp4")

print("🎬 Loading ULTRA video...")
video = VideoFileClip(str(input_path))

print("📐 Compressing more...")
compressed = video.resized(height=720).with_fps(24)

print("💾 Exporting...")
compressed.write_videofile(
    str(output_path),
    fps=24,
    codec='libx264',
    audio_codec='aac',
    bitrate='2500k',
    temp_audiofile='temp-audio.m4a',
    remove_temp=True,
    logger=None
)

video.close()
compressed.close()

size = output_path.stat().st_size / (1024*1024)
print(f"✅ Done! Size: {size:.1f} MB")
