#!/usr/bin/env python3
"""Create compressed preview of PRO video 001"""

from moviepy import VideoFileClip
from pathlib import Path

input_path = Path("content/videos_pro/tiktok_001_PRO.mp4")
output_path = Path("content/videos_pro/tiktok_001_PRO_preview.mp4")

print("🎬 Loading PRO video...")
video = VideoFileClip(str(input_path))

print("📐 Creating 30-sec preview (lower res)...")
# Take first 30 seconds, lower resolution
preview = video.subclipped(0, 30).resized(height=960)

print("💾 Exporting preview...")
preview.write_videofile(
    str(output_path),
    fps=24,
    codec='libx264',
    audio_codec='aac',
    bitrate='600k',
    temp_audiofile='temp-audio.m4a',
    remove_temp=True,
    logger=None
)

video.close()
preview.close()

size = output_path.stat().st_size / (1024*1024)
print(f"✅ Preview created! Size: {size:.1f} MB")
