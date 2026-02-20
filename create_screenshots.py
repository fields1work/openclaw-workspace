#!/usr/bin/env python3
"""Create screenshot frames from PRO video 001"""

from moviepy import VideoFileClip
from pathlib import Path

input_path = Path("content/videos_pro/tiktok_001_PRO.mp4")

print("🎬 Loading PRO video...")
video = VideoFileClip(str(input_path))

# Extract frames at key moments
frames = [3, 8, 15, 25, 35, 45]  # Seconds where captions appear

for t in frames:
    print(f"📸 Capturing frame at {t}s...")
    frame = video.get_frame(t)
    from PIL import Image
    img = Image.fromarray(frame)
    img.save(f"content/videos_pro/frame_{t:02d}s.jpg", quality=85)
    print(f"   Saved: frame_{t:02d}s.jpg")

video.close()
print("✅ Screenshots created!")
