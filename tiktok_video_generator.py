#!/usr/bin/env python3
"""
🎬 TikTok Video Generator - Automated Reddit-Style Content
Aneko <> Fields Production Pipeline
Generates 9:16 vertical videos with captions + voiceover + gameplay background
"""

import os
import subprocess
import json
from pathlib import Path
from datetime import datetime

# Configuration
OUTPUT_DIR = Path("content/videos/auto_generated")
VOICEOVER_DIR = Path("content/voiceovers")
GAMEPLAY_DIR = Path("content/gameplay")  # Downloaded footage
ASSETS_DIR = Path("content/assets")

# Video specs
VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
VIDEO_FPS = 30
VIDEO_DURATION = 60  # seconds

class TikTokVideoGenerator:
    """Generates viral TikTok videos using moviepy or ffmpeg"""
    
    def __init__(self, script_data):
        self.script = script_data
        self.output_path = None
        
    def check_dependencies(self):
        """Check if ffmpeg and required tools are available, auto-fix PATH if needed"""
        # Try standard check first
        try:
            subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
        
        # Auto-detect ffmpeg in common locations
        common_paths = [
            r"C:\ffmpeg\bin",
            r"C:\ffmpeg\ffmpeg-6.1.1-essentials_build\bin",
            r"C:\Program Files\ffmpeg\bin",
            r"C:\Users\field\ffmpeg\bin",
        ]
        
        for path in common_paths:
            ffmpeg_exe = Path(path) / "ffmpeg.exe"
            if ffmpeg_exe.exists():
                print(f"✅ Found ffmpeg at: {path}")
                # Add to PATH for this session
                os.environ["PATH"] = os.environ["PATH"] + ";" + path
                # Also set IMAGEMAGICK_BINARY for moviepy if needed
                os.environ["IMAGEIO_FFMPEG_EXE"] = str(ffmpeg_exe)
                return True
        
        return False
    
    def generate_video(self, output_name):
        """
        Generate complete video using moviepy
        Steps:
        1. Load voiceover MP3
        2. Load gameplay footage (loop/cut to duration)
        3. Add captions with timing
        4. Combine all layers
        5. Export 1080x1920 MP4
        """
        print(f"🎬 Generating video: {output_name}")
        print(f"⏱️  Target duration: {VIDEO_DURATION}s")
        print(f"📐 Resolution: {VIDEO_WIDTH}x{VIDEO_HEIGHT}")
        
        try:
            from moviepy.editor import (VideoFileClip, AudioFileClip, TextClip, 
                                       CompositeVideoClip, ColorClip)
            from moviepy.video.fx.all import resize
            
            # Load gameplay footage
            gameplay_path = GAMEPLAY_DIR / f"{self.script.get('gameplay_type', 'subway_surfers')}.mp4"
            if not gameplay_path.exists():
                print(f"⚠️  Gameplay footage not found: {gameplay_path}")
                print(f"📝 Please download 60-second gameplay video to: {GAMEPLAY_DIR}")
                return None
            
            print(f"📹 Loading gameplay: {gameplay_path}")
            gameplay = VideoFileClip(str(gameplay_path))
            
            # Loop/crop gameplay to target duration
            if gameplay.duration < VIDEO_DURATION:
                # Loop if too short
                loops_needed = int(VIDEO_DURATION / gameplay.duration) + 1
                gameplay = gameplay.loop(n=loops_needed)
            
            # Trim to exact duration
            gameplay = gameplay.subclip(0, VIDEO_DURATION)
            
            # Resize to 9:16 vertical (1080x1920)
            gameplay = gameplay.resize((VIDEO_WIDTH, VIDEO_HEIGHT))
            
            # Load voiceover
            voiceover_path = VOICEOVER_DIR / self.script.get('voiceover_file', 'voiceover.mp3')
            if voiceover_path.exists():
                print(f"🎙️  Loading voiceover: {voiceover_path}")
                voiceover = AudioFileClip(str(voiceover_path))
                # Trim voiceover to video duration
                voiceover = voiceover.subclip(0, VIDEO_DURATION)
                gameplay = gameplay.set_audio(voiceover)
            else:
                print(f"⚠️  Voiceover not found: {voiceover_path}")
            
            # Create caption clips
            print("📝 Creating captions...")
            caption_clips = []
            
            for caption in self.script.get('captions', []):
                text = caption['text']
                start = caption['start']
                end = caption['end']
                style = caption.get('style', 'body')
                
                # Style configuration
                if style == 'hook':
                    fontsize = 60
                    color = '#ff6b35'
                    stroke_color = 'black'
                    stroke_width = 4
                    font = 'Arial-Bold'
                elif style == 'cliffhanger':
                    fontsize = 65
                    color = '#ff6b35'
                    stroke_color = 'black'
                    stroke_width = 5
                    font = 'Arial-Bold'
                elif style == 'emphasis':
                    fontsize = 50
                    color = '#ff6b35'
                    stroke_color = 'black'
                    stroke_width = 3
                    font = 'Arial'
                elif style == 'whisper':
                    fontsize = 45
                    color = '#ffffff'
                    stroke_color = 'black'
                    stroke_width = 3
                    font = 'Arial-Italic'
                else:  # body
                    fontsize = 48
                    color = '#ffffff'
                    stroke_color = 'black'
                    stroke_width = 3
                    font = 'Arial'
                
                # Create text clip
                txt_clip = TextClip(
                    text,
                    fontsize=fontsize,
                    color=color,
                    stroke_color=stroke_color,
                    stroke_width=stroke_width,
                    font=font,
                    method='caption',
                    size=(VIDEO_WIDTH - 100, None),
                    align='center'
                ).set_duration(end - start).set_start(start)
                
                # Position in lower 2/3 of screen
                txt_clip = txt_clip.set_position(('center', 0.6), relative=True)
                
                caption_clips.append(txt_clip)
            
            # Add end card
            end_card = TextClip(
                "Part 2? 👀 Follow @FieldsBuildsAI",
                fontsize=55,
                color='#ff6b35',
                stroke_color='black',
                stroke_width=4,
                font='Arial-Bold',
                method='caption',
                size=(VIDEO_WIDTH - 100, None),
                align='center'
            ).set_duration(3).set_start(VIDEO_DURATION - 3)
            end_card = end_card.set_position(('center', 0.7), relative=True)
            caption_clips.append(end_card)
            
            # Composite all layers
            print("🎬 Compositing video layers...")
            final_video = CompositeVideoClip([gameplay] + caption_clips)
            final_video = final_video.set_duration(VIDEO_DURATION)
            
            # Export
            output_path = OUTPUT_DIR / f"{output_name}.mp4"
            print(f"💾 Exporting to: {output_path}")
            
            final_video.write_videofile(
                str(output_path),
                fps=VIDEO_FPS,
                codec='libx264',
                audio_codec='aac',
                temp_audiofile=str(OUTPUT_DIR / 'temp-audio.m4a'),
                remove_temp=True
            )
            
            print(f"✅ VIDEO GENERATED: {output_path}")
            
            # Cleanup
            gameplay.close()
            if voiceover_path.exists():
                voiceover.close()
            final_video.close()
            
            return output_path
            
        except ImportError as e:
            print(f"❌ moviepy not installed: {e}")
            print(f"📝 Install with: pip install moviepy")
            return None
        except Exception as e:
            print(f"❌ Error generating video: {e}")
            return None
    
    def preview_script(self):
        """Print script breakdown for review"""
        print("\n" + "="*50)
        print("📋 SCRIPT PREVIEW")
        print("="*50)
        
        for i, scene in enumerate(self.script.get("scenes", []), 1):
            print(f"\n🎬 Scene {i} ({scene['time_start']}s - {scene['time_end']}s)")
            print(f"   Text: {scene['text']}")
            print(f"   Visual: {scene.get('visual_note', 'Subway Surfers gameplay')}")
            print(f"   Caption style: {scene.get('caption_style', 'Standard')}")
        
        print("\n" + "="*50)


def create_viral_script_girlfriend_sister():
    """Create the viral script we designed"""
    return {
        "title": "My girlfriend's sister hit on me at dinner",
        "duration": 60,
        "hook": "My girlfriend's sister hit on me at family dinner",
        "gameplay_type": "subway_surfers",
        "voiceover_file": "voiceover_girlfriend_sister.mp3",
        "scenes": [
            {
                "time_start": 0,
                "time_end": 3,
                "text": "My girlfriend's sister hit on me at dinner",
                "caption_style": "HOOK - Big, orange, center",
                "visual_note": "Subway Surfers fast lane"
            },
            {
                "time_start": 3,
                "time_end": 8,
                "text": "We've been dating two years. Her family loves me.",
                "caption_style": "Context - White, lower third",
                "visual_note": "Steady run, collecting coins"
            },
            {
                "time_start": 8,
                "time_end": 15,
                "text": "Sunday dinner. Her parents' house. I'm the golden boyfriend.",
                "caption_style": "Context - White, lower third",
                "visual_note": "Continue steady run"
            },
            {
                "time_start": 15,
                "time_end": 20,
                "text": "Sister keeps staring. I ignore it.",
                "caption_style": "Escalation - White",
                "visual_note": "Speed increases"
            },
            {
                "time_start": 20,
                "time_end": 26,
                "text": 'She "accidentally" touches my leg under the table.',
                "caption_style": "Escalation - Orange emphasis",
                "visual_note": "Near-miss with train"
            },
            {
                "time_start": 26,
                "time_end": 32,
                "text": "I move my chair. She moves closer.",
                "caption_style": "Escalation - White",
                "visual_note": "Fast lane switching"
            },
            {
                "time_start": 32,
                "time_end": 38,
                "text": "Bathroom break. She follows me into the hallway.",
                "caption_style": "Twist - White",
                "visual_note": "Tunnel section, dramatic"
            },
            {
                "time_start": 38,
                "time_end": 44,
                "text": "Grabs my hand. Whispers: 'I've wanted you for months.'",
                "caption_style": "Twist - Italic, orange",
                "visual_note": "Slow motion near-miss"
            },
            {
                "time_start": 44,
                "time_end": 50,
                "text": "Girlfriend calls from the kitchen: 'Babe, you okay?'",
                "caption_style": "Twist - White",
                "visual_note": "Speed returns normal"
            },
            {
                "time_start": 50,
                "time_end": 56,
                "text": "Sister smiles. 'Don't answer. She doesn't know anything.'",
                "caption_style": "Cliffhanger - White",
                "visual_note": "Approaching jump ramp"
            },
            {
                "time_start": 56,
                "time_end": 60,
                "text": "But my phone was recording everything.",
                "caption_style": "HOOK PART 2 - BIG, orange, dramatic",
                "visual_note": "Jumps ramp slow motion"
            }
        ],
        "captions": [
            {"text": "My girlfriend's sister hit on me at dinner", "start": 0, "end": 3, "style": "hook"},
            {"text": "We've been dating two years. Her family loves me.", "start": 3, "end": 8, "style": "body"},
            {"text": "Sunday dinner. Her parents' house. I'm the golden boyfriend.", "start": 8, "end": 15, "style": "body"},
            {"text": "Sister keeps staring. I ignore it.", "start": 15, "end": 20, "style": "body"},
            {"text": 'She "accidentally" touches my leg under the table.', "start": 20, "end": 26, "style": "emphasis"},
            {"text": "I move my chair. She moves closer.", "start": 26, "end": 32, "style": "body"},
            {"text": "Bathroom break. She follows me into the hallway.", "start": 32, "end": 38, "style": "body"},
            {"text": "Grabs my hand. Whispers: 'I've wanted you for months.'", "start": 38, "end": 44, "style": "whisper"},
            {"text": "Girlfriend calls from the kitchen: 'Babe, you okay?'", "start": 44, "end": 50, "style": "body"},
            {"text": "Sister smiles. 'Don't answer. She doesn't know anything.'", "start": 50, "end": 56, "style": "body"},
            {"text": "But my phone was recording everything.", "start": 56, "end": 60, "style": "cliffhanger"}
        ],
        "posting_strategy": {
            "optimal_time": "7:00-9:00 PM CST",
            "cta": "Part 2? 👀 Follow @FieldsBuildsAI",
            "pinned_comment": "Part 2 drops tomorrow at 8 PM 👀 Follow + turn on notifications 🔔 This gets WORSE before it gets better 😬"
        }
    }


def main():
    """Main execution"""
    print("🚀 TikTok Video Generator - Starting...")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50)
    
    # Ensure directories exist
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Create viral script
    script = create_viral_script_girlfriend_sister()
    
    # Initialize generator
    generator = TikTokVideoGenerator(script)
    
    # Check if we can generate (dependencies)
    if generator.check_dependencies():
        print("✅ ffmpeg found - video generation possible")
    else:
        print("⚠️  ffmpeg not found - video generation limited")
        print("📝 Install with: choco install ffmpeg (Windows)")
    
    # Preview script
    generator.preview_script()
    
    # Generate plan (full video coming with moviepy)
    plan_path = generator.generate_video("viral_girlfriend_sister_v1")
    
    print("\n" + "="*50)
    print("🎯 NEXT STEPS:")
    print("="*50)
    print("1. Install moviepy: pip install moviepy")
    print("2. Download Subway Surfers gameplay (60 sec)")
    print("3. Generate voiceover with ElevenLabs")
    print("4. Run full video assembly")
    print(f"5. Video plan saved: {plan_path}")
    print("\n✅ Framework ready - implement full generation next!")
    
    return plan_path


if __name__ == "__main__":
    main()
