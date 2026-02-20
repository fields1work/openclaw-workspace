#!/usr/bin/env python3
"""
ULTIMATE QUALITY EXPORT SCRIPT
Maximum quality TikTok video export with zero loss
Uses FFmpeg with pro-grade settings
"""

import subprocess
from pathlib import Path

def export_ultra_quality(input_path, output_path):
    """
    Export with MAXIMUM quality settings
    Professional-grade H.264 export
    """
    
    cmd = [
        'ffmpeg',
        '-i', str(input_path),           # Input file
        '-c:v', 'libx264',               # H.264 codec (best compatibility)
        '-preset', 'slow',               # Slower = better compression
        '-crf', '16',                    # CRF 16 = visually lossless (lower = better)
        '-profile:v', 'high',            # High profile H.264
        '-level:v', '4.2',               # Level 4.2 (1080p60 support)
        '-pix_fmt', 'yuv420p',           # Pixel format (compatibility)
        '-r', '60',                      # 60fps output
        '-g', '120',                     # GOP size (2 sec keyframes)
        '-bf', '2',                      # B-frames for compression
        '-c:a', 'aac',                   # Audio codec
        '-b:a', '320k',                  # Audio bitrate premium
        '-ar', '48000',                  # Audio sample rate
        '-movflags', '+faststart',       # Web streaming optimized
        '-threads', '0',                 # Use all CPU threads
        '-y',                            # Overwrite output
        str(output_path)
    ]
    
    print("🔥 EXPORTING ULTRA QUALITY")
    print("=" * 60)
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")
    print("Settings:")
    print("  • Codec: H.264 (libx264)")
    print("  • CRF: 16 (visually lossless)")
    print("  • Profile: High@4.2")
    print("  • FPS: 60")
    print("  • Audio: 320kbps AAC")
    print("=" * 60)
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        output_size = Path(output_path).stat().st_size / (1024*1024)
        print(f"✅ SUCCESS! Output size: {output_size:.1f} MB")
        return True
    else:
        print(f"❌ ERROR: {result.stderr[:200]}")
        return False

# Alternative: ProRes for editing (if you want to edit later)
def export_prores(input_path, output_path):
    """
    ProRes 422 export - LOSSLESS quality for editing
    Much larger files but zero compression artifacts
    """
    
    cmd = [
        'ffmpeg',
        '-i', str(input_path),
        '-c:v', 'prores_ks',         # ProRes codec
        '-profile:v', '3',            # ProRes 422
        '-bits_per_mb', '800',        # High bitrate
        '-pix_fmt', 'yuv422p10le',    # 10-bit color
        '-r', '60',
        '-c:a', 'pcm_s16le',          # Uncompressed audio
        '-ar', '48000',
        '-y',
        str(output_path)
    ]
    
    print("🎬 EXPORTING PRORES (LOSSLESS)")
    subprocess.run(cmd)

# Alternative: HEVC (H.265) for smaller files with same quality
def export_hevc(input_path, output_path):
    """
    H.265/HEVC export - Better compression than H.264
    Smaller files, same quality (but longer encode time)
    """
    
    cmd = [
        'ffmpeg',
        '-i', str(input_path),
        '-c:v', 'libx265',
        '-preset', 'slow',
        '-crf', '18',              # HEVC CRF 18 ≈ H.264 CRF 16
        '-r', '60',
        '-c:a', 'aac',
        '-b:a', '320k',
        '-tag:v', 'hvc1',         # For Apple compatibility
        '-y',
        str(output_path)
    ]
    
    print("🎬 EXPORTING HEVC (H.265)")
    subprocess.run(cmd)

if __name__ == "__main__":
    print("=" * 60)
    print("ULTIMATE QUALITY EXPORT OPTIONS")
    print("=" * 60)
    
    print("\nOption 1: ULTRA H.264 (RECOMMENDED)")
    print("  • Best TikTok compatibility")
    print("  • CRF 16 = visually lossless")
    print("  • File size: ~100-150 MB per 60s video")
    
    print("\nOption 2: PRORES 422")
    print("  • TRUE lossless (editing format)")
    print("  • Zero compression artifacts")
    print("  • File size: ~500-800 MB per 60s video")
    
    print("\nOption 3: HEVC (H.265)")
    print("  • Same quality, 50% smaller files")
    print("  • Slower encoding")
    print("  • May have compatibility issues")
    
    print("\n" + "=" * 60)
    print("RECOMMENDATION: Use ULTRA H.264 for TikTok")
    print("=" * 60)
