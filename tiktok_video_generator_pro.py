#!/usr/bin/env python3
"""
TikTok Video Generator PRO v2.0
With word-by-word captions, dramatic pauses, and viral formatting
"""

import os
import re
from pathlib import Path
from moviepy import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
from moviepy.audio.fx import MultiplyStereoVolume
import numpy as np

# Paths
OUTPUT_DIR = Path("content/videos_pro")
VOICEOVER_DIR = Path("content/voiceovers")
GAMEPLAY_DIR = Path("content/gameplay")
SCRIPT_DIR = Path("content/scripts")

OUTPUT_DIR.mkdir(exist_ok=True)
VOICEOVER_DIR.mkdir(exist_ok=True)

# Video specs
VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
VIDEO_FPS = 60  # Higher quality
VIDEO_DURATION = 60

# Caption styling
HOOK_COLOR = '#ff6b35'  # Orange
BODY_COLOR = '#ffffff'  # White
ACCENT_COLOR = '#ffcc00'  # Yellow for emphasis
STROKE_COLOR = '#000000'
STROKE_WIDTH = 4

class VideoGeneratorPro:
    def __init__(self):
        self.clips = []
        
    def parse_script(self, script_text):
        """Parse script with pause markers into timed segments"""
        segments = []
        lines = script_text.strip().split('\n')
        current_time = 0
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Check for pause marker
            pause_match = re.search(r'\(pause ([\d.]+)s\)', line)
            pause_duration = float(pause_match.group(1)) if pause_match else 0.5
            
            # Remove pause marker from text
            clean_text = re.sub(r'\s*\(pause [\d.]+s\)', '', line)
            
            if clean_text:
                # Estimate duration (3 words per second + pause)
                word_count = len(clean_text.split())
                segment_duration = (word_count / 2.8) + pause_duration
                
                segments.append({
                    'text': clean_text,
                    'duration': segment_duration,
                    'pause': pause_duration,
                    'is_hook': segments == [] or 'ALL CAPS' in clean_text or any(word in clean_text.upper() for word in ['FIRED', 'TERRIFIED', 'PREGNANT', 'DAD'])
                })
                current_time += segment_duration
                
        return segments
    
    def create_word_captions(self, segments, total_duration):
        """Create word-by-word caption clips"""
        caption_clips = []
        current_time = 0
        
        for segment in segments:
            words = segment['text'].split()
            word_duration = (segment['duration'] - segment['pause']) / len(words) if words else 0.5
            
            for i, word in enumerate(words):
                # Determine styling
                is_key_word = word.isupper() or word in ['BOSS', 'FIRED', 'CHEATING', 'SECRET', 'MONEY', 'POLICE']
                is_hook = segment['is_hook'] and i == 0
                
                if is_hook:
                    color = HOOK_COLOR
                    font_size = 72
                    y_pos = VIDEO_HEIGHT * 0.25  # Upper area
                elif is_key_word:
                    color = ACCENT_COLOR
                    font_size = 64
                    y_pos = VIDEO_HEIGHT * 0.75  # Lower area
                else:
                    color = BODY_COLOR
                    font_size = 58
                    y_pos = VIDEO_HEIGHT * 0.75
                
                # Create text clip
                txt_clip = TextClip(
                    text=word,
                    font_size=font_size,
                    color=color,
                    stroke_color=STROKE_COLOR,
                    stroke_width=STROKE_WIDTH,
                    size=(VIDEO_WIDTH - 100, None),
                    text_align='center',
                    duration=word_duration
                )
                
                txt_clip = txt_clip.with_position(('center', y_pos)).with_start(current_time)
                caption_clips.append(txt_clip)
                
                current_time += word_duration
            
            current_time += segment['pause']
        
        return caption_clips
    
    def generate_video(self, script_num, script_name, gameplay_file, voiceover_file, output_name, script_text):
        print(f"\n🎬 Generating Video {script_num}: {script_name}")
        print("=" * 60)
        
        gameplay_path = GAMEPLAY_DIR / gameplay_file
        voiceover_path = VOICEOVER_DIR / voiceover_file
        output_path = OUTPUT_DIR / f"{output_name}_PRO.mp4"
        
        # Check if already done
        if output_path.exists() and output_path.stat().st_size > 50000000:
            print(f"✅ Already exists ({output_path.stat().st_size/1024/1024:.1f} MB), skipping")
            return True
        
        try:
            # Load gameplay
            print("📹 Loading gameplay...")
            gameplay = VideoFileClip(str(gameplay_path))
            
            if gameplay.duration < VIDEO_DURATION:
                gameplay = gameplay.with_duration(VIDEO_DURATION).fx("vfx.loop", duration=VIDEO_DURATION)
            else:
                gameplay = gameplay.subclipped(0, VIDEO_DURATION)
            
            gameplay = gameplay.resized(new_size=(VIDEO_WIDTH, VIDEO_HEIGHT))
            
            # Load audio
            print("🎙️ Loading voiceover...")
            audio = AudioFileClip(str(voiceover_path))
            if audio.duration > VIDEO_DURATION:
                audio = audio.subclipped(0, VIDEO_DURATION)
            
            gameplay = gameplay.with_audio(audio)
            
            # Parse script and create captions
            print("📝 Creating word-by-word captions...")
            segments = self.parse_script(script_text)
            captions = self.create_word_captions(segments, VIDEO_DURATION)
            
            # Composite video
            print("🎨 Compositing video layers...")
            all_clips = [gameplay] + captions
            final_video = CompositeVideoClip(all_clips, size=(VIDEO_WIDTH, VIDEO_HEIGHT))
            
            # Export with high quality
            print("💾 Exporting PRO version (high quality)...")
            print("   This takes ~4-5 minutes per video...")
            
            final_video.write_videofile(
                str(output_path),
                fps=VIDEO_FPS,
                codec='libx264',
                audio_codec='aac',
                bitrate='8000k',  # High quality
                temp_audiofile='temp-audio.m4a',
                remove_temp=True,
                logger=None
            )
            
            gameplay.close()
            audio.close()
            final_video.close()
            
            size = output_path.stat().st_size / (1024*1024)
            print(f"✅ DONE! ({size:.1f} MB)")
            return True
            
        except Exception as e:
            print(f"❌ Error: {str(e)[:100]}")
            import traceback
            traceback.print_exc()
            return False

# Scripts with pauses
SCRIPTS = {
    1: """I just found out... (pause 1.0s)
My girlfriend's sister... (pause 0.8s)
Is actually my boss's wife. (pause 1.2s)
Let me explain. (pause 0.5s)
Last week... (pause 0.5s)
I saw my boss at a restaurant. (pause 0.6s)
He was with a woman. (pause 0.8s)
She looked familiar. (pause 0.8s)
Too familiar. (pause 1.0s)
I didn't think much of it. (pause 0.5s)
Until yesterday. (pause 1.0s)
My girlfriend invited me to family dinner. (pause 0.6s)
Her sister walks in. (pause 0.8s)
Same woman. (pause 0.8s)
Same restaurant. (pause 0.8s)
My boss's "business dinner." (pause 1.2s)
Now I have photos... (pause 1.0s)
And a choice to make. (pause 1.5s)
Follow for Part 2. (pause 0.5s)
This gets worse.""",
    
    2: """My boss just called me... (pause 0.8s)
Into his office. (pause 0.6s)
He thinks I don't know. (pause 1.0s)
But I saw everything. (pause 1.2s)
Three weeks ago... (pause 0.5s)
Late night at the office. (pause 0.6s)
I forgot my charger. (pause 0.6s)
Went back upstairs. (pause 0.6s)
The door was locked. (pause 0.8s)
But the glass wall... (pause 0.8s)
Isn't frosted at the top. (pause 1.0s)
I saw them. (pause 1.2s)
My boss. (pause 0.8s)
And my coworker's wife. (pause 1.2s)
Now he wants to "talk." (pause 1.0s)
About my "future at the company." (pause 1.0s)
He has NO idea... (pause 1.0s)
I recorded everything. (pause 1.5s)
Follow for what happens next.""",
    
    3: """I got FIRED today. (pause 1.2s)
But I'm not mad. (pause 0.8s)
I'm TERRIFIED. (pause 1.0s)
On my way out... (pause 0.6s)
Security walked me to my car. (pause 0.6s)
That's normal, right? (pause 0.8s)
Except they didn't leave. (pause 0.8s)
They FOLLOWED me home. (pause 1.0s)
Sat outside my house... (pause 0.8s)
For THREE HOURS. (pause 1.2s)
I called the cops. (pause 0.6s)
They told me... (pause 1.0s)
"We can't help you." (pause 1.0s)
"Call your former employer." (pause 1.0s)
My boss answered. (pause 0.8s)
"You saw the files." (pause 1.2s)
"We need to talk." (pause 1.0s)
I never saw any files. (pause 1.2s)
Or did I? (pause 1.5s)
Part 2 drops tomorrow.""",
}

# Main execution
if __name__ == "__main__":
    generator = VideoGeneratorPro()
    
    videos = [
        (1, "Girlfriend's Sister", "subway_surfers.mp4", "voiceover_001_girlfriend_sister.mp3", "tiktok_001"),
        (2, "Boss Affair", "gta_driving.mp4", "voiceover_002_boss_affair.mp3", "tiktok_002"),
        (3, "Fired Revelation", "minecraft_parkour.mp4", "voiceover_003_fired_revelation.mp3", "tiktok_003"),
    ]
    
    print("=" * 60)
    print("🎬 TIKTOK VIDEO GENERATOR PRO v2.0")
    print("Word-by-word captions + Dramatic pauses + High quality")
    print("=" * 60)
    
    success = 0
    for num, name, gameplay, voiceover, output in videos[:3]:  # Start with first 3
        script = SCRIPTS.get(num, "")
        if script and generator.generate_video(num, name, gameplay, voiceover, output, script):
            success += 1
    
    print("\n" + "=" * 60)
    print(f"🎉 COMPLETE: {success}/{len(videos[:3])} PRO videos generated!")
    print(f"📁 Location: {OUTPUT_DIR}/")
    print("=" * 60)
