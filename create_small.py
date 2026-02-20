#!/usr/bin/env python3
"""Create ULTRA small version"""

from moviepy import VideoFileClip
from pathlib import Path

input_path = Path("content/videos_ultra/tiktok_001_ULTRA.mp4")
output_path = Path("content/videos_ultra/tiktok_001_SMALL.mp4")

print("🎬 Loading...")
video = VideoFileClip(str(input_path))

print("📐 Heavy compression...")
compressed = video.resized(height=540).with_fps(20)  # 540p, 20fps

print("💾 Exporting small...")
compressed.write_videofile(
    str(output_path),
    fps=20,
    codec='libx264',
    audio_codec='aac',
    bitrate='1200k',  # Low bitrate
    temp_audiofile='temp-audio.m4a',
    remove_temp=True,
    logger=None
)

video.close()
compressed.close()

size = output_path.stat().st_size / (1024*1024)
print(f"✅ Done! Size: {size:.1f} MB")
