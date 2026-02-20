#!/usr/bin/env python3
"""Create compressed preview of video 001"""

from moviepy import VideoFileClip
from pathlib import Path

input_path = Path("content/videos/tiktok_001_girlfriend_sister.mp4")
output_path = Path("content/videos/tiktok_001_preview.mp4")

print("🎬 Loading full video...")
video = VideoFileClip(str(input_path))

print("📐 Creating preview (540x960, 30 sec)...")
# Take first 30 seconds, lower resolution, lower bitrate
preview = video.subclipped(0, 30).resized(height=960)

print("💾 Exporting preview...")
preview.write_videofile(
    str(output_path),
    fps=24,
    codec='libx264',
    audio_codec='aac',
    bitrate='800k',  # Lower bitrate for smaller file
    temp_audiofile='temp-audio.m4a',
    remove_temp=True,
    logger=None
)

video.close()
preview.close()

size = output_path.stat().st_size / (1024*1024)
print(f"✅ Preview created! Size: {size:.1f} MB")
