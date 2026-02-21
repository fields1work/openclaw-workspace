"""
Video Renderer MVP - TikTok Reddit Story Automation
Generates TikTok-ready videos from script + gameplay + TTS

Usage:
    python renderer.py --script script.txt --gameplay gameplay.mp4 --tts audio.mp3 --output output.mp4

Fields Build System - Phase 1
"""

from moviepy.editor import *
from moviepy.video.fx.all import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import sys
from pathlib import Path

# TikTok specs from BluePrint v1.0
OUTPUT_RESOLUTION = (1080, 1920)  # 9:16
FPS = 30
BITRATE = "10000k"  # 10 Mbps sweet spot
CODEC = "libx264"

# Caption specs
CAPTION_FONT_SIZE = 54  # pt
CAPTION_FONT = "Arial-Bold"  # Fallback system font
CAPTION_COLOR = (255, 255, 255)  # White
CAPTION_STROKE_COLOR = (0, 0, 0)  # Black
CAPTION_STROKE_WIDTH = 4
CAPTION_POSITION = "lower_third"  # 75% down
HOOK_FONT_SIZE = 72
HOOK_COLOR = (255, 107, 53)  # Orange #FF6B35

class TikTokVideoRenderer:
    """
    Renders Reddit story videos optimized for TikTok virality.
    
    Implements Viral Format Blueprint v1.0 specifications.
    """
    
    def __init__(self, output_path="exports"):
        self.output_path = Path(output_path)
        self.output_path.mkdir(exist_ok=True, parents=True)
        self.font_cache = {}
    
    def render_video(self, script_data, gameplay_path, tts_path, output_filename):
        """
        Main render pipeline.
        
        Args:
            script_data: Dict with 'hook', 'captions' (list of {text, start, end}), 'cliffhanger'
            gameplay_path: Path to gameplay footage (Subway Surfers/Minecraft)
            tts_path: Path to TTS audio file
            output_filename: Output MP4 filename
        """
        print(f"🎬 Starting render: {output_filename}")
        
        # Load assets
        gameplay = VideoFileClip(str(gameplay_path))
        tts_audio = AudioFileClip(str(tts_path))
        
        # Trim gameplay to audio length
        duration = tts_audio.duration
        gameplay = gameplay.loop(duration=duration)
        gameplay = gameplay.resize(OUTPUT_RESOLUTION)
        
        # Build video layers
        print("📝 Building caption layers...")
        caption_clips = self._build_captions(script_data, duration)
        hook_clip = self._build_hook(script_data['hook'])
        
        # Composite
        print("🎨 Compositing...")
        video = CompositeVideoClip(
            [gameplay] + caption_clips + [hook_clip],
            size=OUTPUT_RESOLUTION
        )
        video = video.set_audio(tts_audio)
        video = video.set_duration(duration)
        
        # Export with TikTok-optimized settings
        output_path = self.output_path / output_filename
        print(f"📤 Exporting to: {output_path}")
        print(f"   Specs: {OUTPUT_RESOLUTION[0]}x{OUTPUT_RESOLUTION[1]} @ {FPS}fps, ~10Mbps")
        
        video.write_videofile(
            str(output_path),
            fps=FPS,
            codec=CODEC,
            bitrate=BITRATE,
            audio_codec="aac",
            audio_bitrate="192k",
            threads=4,
            logger=None  # Use tqdm progress
        )
        
        # Cleanup
        gameplay.close()
        tts_audio.close()
        video.close()
        
        print(f"✅ Render complete: {output_path}")
        return output_path
    
    def _build_captions(self, script_data, total_duration):
        """Build caption clips from script data."""
        clips = []
        
        for caption in script_data.get('captions', []):
            text = caption['text']
            start = caption['start']
            end = caption['end']
            
            # Create text clip
            txt_clip = (TextClip(
                text,
                fontsize=CAPTION_FONT_SIZE,
                color='white',
                stroke_color='black',
                stroke_width=CAPTION_STROKE_WIDTH,
                font='Arial-Bold',
                method='caption',
                size=(OUTPUT_RESOLUTION[0] - 100, None),  # Safe margins
                align='center'
            )
            .set_start(start)
            .set_duration(end - start)
            .set_position(('center', 0.75), relative=True))  # Lower third
            
            clips.append(txt_clip)
        
        return clips
    
    def _build_hook(self, hook_text):
        """Build the 3-second orange hook."""
        hook = (TextClip(
            hook_text,
            fontsize=HOOK_FONT_SIZE,
            color='#FF6B35',  # Orange
            stroke_color='black',
            stroke_width=5,
            font='Arial-Bold',
            method='caption',
            size=(OUTPUT_RESOLUTION[0] - 60, None),
            align='center'
        )
        .set_start(0)
        .set_duration(3.0)  # Exactly 3 seconds per BluePrint
        .set_position('center'))
        
        return hook
    
    def _create_pattern_interrupts(self, duration):
        """
        Generate subtle zooms at 5-7 second intervals.
        Returns list of dicts with timing and effect.
        """
        interrupts = []
        current_time = 5.0  # First interrupt at 5s
        
        while current_time < duration - 1:
            interrupts.append({
                'time': current_time,
                'type': 'micro_zoom',
                'duration': 0.5,
                'scale': 1.05
            })
            current_time += np.random.uniform(5, 7)  # Random 5-7s gaps
        
        return interrupts


def quick_test():
    """Test render with sample data."""
    renderer = TikTokVideoRenderer()
    
    # Sample script data (matches BluePrint v1.0 structure)
    script_data = {
        'hook': 'My wife was living a double life',
        'captions': [
            {'text': 'I thought I knew everything about Sarah.', 'start': 3.0, 'end': 5.5},
            {'text': "We'd been married for three years.", 'start': 5.5, 'end': 7.5},
            {'text': 'But six months ago, things got weird.', 'start': 7.5, 'end': 10.0},
            {'text': 'She started locking her phone.', 'start': 10.0, 'end': 12.0},
        ],
        'cliffhanger': "I've been the affair partner this whole time."
    }
    
    # This would need actual file paths
    print("🧪 Running test render with sample data...")
    print("   (Requires gameplay.mp4 and tts.mp3 to be present)")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='TikTok Video Renderer')
    parser.add_argument('--script', help='Script JSON file path')
    parser.add_argument('--gameplay', help='Gameplay video path')
    parser.add_argument('--tts', help='TTS audio path')
    parser.add_argument('--test', action='store_true', help='Run test render')
    
    args = parser.parse_args()
    
    if args.test:
        quick_test()
    elif args.script and args.gameplay and args.tts:
        # Load script JSON and render
        renderer = TikTokVideoRenderer()
        # TODO: Load script from JSON
        print("🚧 Full render mode - implement JSON loading")
    else:
        print("Usage:")
        print("  python renderer.py --test")
        print("  python renderer.py --script script.json --gameplay video.mp4 --tts audio.mp3")
