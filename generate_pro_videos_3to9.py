#!/usr/bin/env python3
"""
TikTok Video Generator PRO v2.1 - Videos 003-009
With word-by-word captions, dramatic pauses, and viral formatting
"""

import os
import re
from pathlib import Path
from moviepy import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip

# Paths
OUTPUT_DIR = Path("content/videos_pro")
VOICEOVER_DIR = Path("content/voiceovers")
GAMEPLAY_DIR = Path("content/gameplay")

OUTPUT_DIR.mkdir(exist_ok=True)

# Video specs
VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
VIDEO_FPS = 60
VIDEO_DURATION = 60

# Caption styling
HOOK_COLOR = '#ff6b35'
BODY_COLOR = '#ffffff'
ACCENT_COLOR = '#ffcc00'
STROKE_COLOR = '#000000'
STROKE_WIDTH = 4

class VideoGeneratorPro:
    def __init__(self):
        self.clips = []
        
    def parse_script(self, script_text):
        """Parse script with pause markers into timed segments"""
        segments = []
        lines = script_text.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            pause_match = re.search(r'\(pause ([\d.]+)s\)', line)
            pause_duration = float(pause_match.group(1)) if pause_match else 0.5
            
            clean_text = re.sub(r'\s*\(pause [\d.]+s\)', '', line)
            
            if clean_text:
                word_count = len(clean_text.split())
                segment_duration = (word_count / 2.8) + pause_duration
                
                is_hook = len(segments) == 0 or any(word in clean_text.upper() for word in ['FIRED', 'TERRIFIED', 'PREGNANT', 'DAD', 'BOSS', 'MONEY', 'POLICE'])
                
                segments.append({
                    'text': clean_text,
                    'duration': segment_duration,
                    'pause': pause_duration,
                    'is_hook': is_hook
                })
                
        return segments
    
    def create_word_captions(self, segments):
        """Create word-by-word caption clips"""
        caption_clips = []
        current_time = 0
        
        for segment in segments:
            words = segment['text'].split()
            word_duration = (segment['duration'] - segment['pause']) / len(words) if words else 0.5
            
            for i, word in enumerate(words):
                is_key_word = word.isupper() or word in ['BOSS', 'FIRED', 'CHEATING', 'SECRET', 'MONEY', 'POLICE', 'WIFE', 'DAD']
                is_hook = segment['is_hook'] and i == 0
                
                if is_hook:
                    color = HOOK_COLOR
                    font_size = 72
                    y_pos = VIDEO_HEIGHT * 0.25
                elif is_key_word:
                    color = ACCENT_COLOR
                    font_size = 64
                    y_pos = VIDEO_HEIGHT * 0.75
                else:
                    color = BODY_COLOR
                    font_size = 58
                    y_pos = VIDEO_HEIGHT * 0.75
                
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
        
        if output_path.exists() and output_path.stat().st_size > 30000000:
            print(f"✅ Already exists ({output_path.stat().st_size/1024/1024:.1f} MB), skipping")
            return True
        
        try:
            print("📹 Loading gameplay...")
            gameplay = VideoFileClip(str(gameplay_path))
            
            if gameplay.duration < VIDEO_DURATION:
                gameplay = gameplay.with_duration(VIDEO_DURATION).fx("vfx.loop", duration=VIDEO_DURATION)
            else:
                gameplay = gameplay.subclipped(0, VIDEO_DURATION)
            
            gameplay = gameplay.resized(new_size=(VIDEO_WIDTH, VIDEO_HEIGHT))
            
            print("🎙️ Loading voiceover...")
            audio = AudioFileClip(str(voiceover_path))
            if audio.duration > VIDEO_DURATION:
                audio = audio.subclipped(0, VIDEO_DURATION)
            
            gameplay = gameplay.with_audio(audio)
            
            print("📝 Creating word-by-word captions...")
            segments = self.parse_script(script_text)
            captions = self.create_word_captions(segments)
            
            print(f"🎨 Compositing {len(captions)} caption clips...")
            all_clips = [gameplay] + captions
            final_video = CompositeVideoClip(all_clips, size=(VIDEO_WIDTH, VIDEO_HEIGHT))
            
            print("💾 Exporting PRO version...")
            print("   This takes ~4-5 minutes per video...")
            
            final_video.write_videofile(
                str(output_path),
                fps=VIDEO_FPS,
                codec='libx264',
                audio_codec='aac',
                bitrate='8000k',
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

# Scripts 003-009 with pauses
SCRIPTS = {
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

    4: """I found a bag... (pause 0.8s)
In my grandfather's attic. (pause 0.6s)
$47,000 in cash. (pause 1.2s)
And a note. (pause 0.8s)
"Don't tell your mother." (pause 1.0s)
I was going to listen. (pause 0.6s)
Until I checked the bills. (pause 0.8s)
They're ALL sequential. (pause 1.0s)
And dated... (pause 1.0s)
Two weeks ago. (pause 0.8s)
Grandpa died six months ago. (pause 1.2s)
Someone put this here. (pause 0.8s)
Recently. (pause 1.0s)
Last night... (pause 0.8s)
I heard footsteps upstairs. (pause 0.8s)
The attic door opened. (pause 1.0s)
I grabbed the bag... (pause 0.8s)
And hid in the closet. (pause 1.0s)
They didn't take anything. (pause 0.8s)
They left something. (pause 1.2s)
Another note. (pause 1.5s)
Part 2 reveals what it said.""",

    5: """My roommate has been drugging me... (pause 1.0s)
For three months. (pause 1.2s)
I thought I was tired. (pause 0.6s)
Stressed. (pause 0.6s)
Burned out. (pause 0.8s)
But it's been him. (pause 1.0s)
Crushing Adderall... (pause 0.8s)
Into my coffee. (pause 0.8s)
I found his stash... (pause 0.8s)
Hidden in the bathroom vent. (pause 1.0s)
With photos. (pause 1.0s)
Of me sleeping. (pause 1.0s)
Dozens of them. (pause 0.8s)
Timestamped. (pause 0.8s)
I called the police. (pause 0.6s)
They asked one question. (pause 1.0s)
"Are you the leaseholder?" (pause 1.0s)
I'm not. (pause 0.8s)
He is. (pause 0.8s)
They said... (pause 1.2s)
"This is a civil matter." (pause 1.5s)
Part 2 drops when I hit 10K.""",

    6: """The other woman called me. (pause 1.0s)
She didn't know... (pause 0.8s)
She was the other woman. (pause 1.0s)
Thought I was. (pause 0.8s)
We compared dates. (pause 0.6s)
Text messages. (pause 0.6s)
Hotel receipts. (pause 0.6s)
He's been seeing us both... (pause 0.8s)
For TWO YEARS. (pause 1.2s)
Same nights. (pause 0.8s)
Same excuses. (pause 0.8s)
"Working late." (pause 1.0s)
But here's where it gets crazy. (pause 1.0s)
She's pregnant. (pause 1.5s)
Five months. (pause 1.0s)
He doesn't know I know. (pause 1.0s)
And she doesn't know... (pause 1.2s)
I'm his WIFE. (pause 1.5s)
Follow for the confrontation.""",

    7: """My landlord found my TikTok. (pause 1.0s)
He's EVICTING me. (pause 1.2s)
Not for the videos. (pause 0.8s)
For what I SAID. (pause 1.0s)
I made a video... (pause 0.6s)
About my apartment problems. (pause 0.6s)
The mold. (pause 0.6s)
The broken heater. (pause 0.6s)
The leaks. (pause 0.6s)
Never named him. (pause 0.8s)
Never named the building. (pause 0.8s)
But he found it. (pause 0.8s)
His lawyer sent a letter. (pause 1.0s)
"Defamation and breach of lease." (pause 1.0s)
Three days to leave. (pause 1.0s)
I called a lawyer. (pause 0.6s)
She asked one thing. (pause 0.8s)
"Did you record the mold?" (pause 1.2s)
I did. (pause 1.0s)
Everything. (pause 1.5s)
Part 2: His reaction when he finds out.""",

    8: """My professor is selling exam answers... (pause 1.0s)
On the dark web. (pause 1.2s)
I found out by accident. (pause 0.6s)
Researching for a paper. (pause 0.6s)
Clicked the wrong link. (pause 0.8s)
Saw his USERNAME. (pause 1.0s)
His PHOTO. (pause 1.0s)
Prices listed by course code. (pause 1.0s)
"Intro to Economics - $500" (pause 1.0s)
"Advanced Accounting - $800" (pause 1.0s)
I bought one. (pause 0.8s)
To see if it was real. (pause 0.8s)
It was. (pause 1.0s)
Every answer. (pause 0.8s)
Exact questions from my midterm. (pause 1.2s)
Yesterday... (pause 0.8s)
He announced a "random" cheating investigation. (pause 1.0s)
Said he has a LIST. (pause 1.2s)
Of buyers. (pause 1.5s)
Part 2: I'm on that list.""",

    9: """My online friend of two years... (pause 0.8s)
Is my DAD. (pause 1.5s)
We met in a gaming Discord. (pause 0.6s)
Same favorite game. (pause 0.6s)
Same sense of humor. (pause 0.6s)
We talked EVERY DAY. (pause 1.0s)
Shared things... (pause 0.8s)
I never told anyone else. (pause 0.8s)
Last week... (pause 0.8s)
He sent a photo by mistake. (pause 1.0s)
His reflection... (pause 1.0s)
In his monitor. (pause 0.8s)
I saw his FACE. (pause 1.2s)
My dad's FACE. (pause 1.5s)
He doesn't know I recognized him. (pause 1.0s)
He still messages me. (pause 0.8s)
"Good morning, buddy." (pause 1.0s)
I haven't responded... (pause 1.2s)
In three days. (pause 1.5s)
Part 2: What I found in his DMs.""",
}

# Main execution
if __name__ == "__main__":
    generator = VideoGeneratorPro()
    
    videos = [
        (3, "Fired Revelation", "minecraft_parkour.mp4", "voiceover_003_fired_revelation.mp3", "tiktok_003"),
        (4, "Money Hustle", "subway_surfers.mp4", "voiceover_004_money_hustle.mp3", "tiktok_004"),
        (5, "Roommate Adderall", "gta_driving.mp4", "voiceover_005_roommate_adderall.mp3", "tiktok_005"),
        (6, "Other Woman", "minecraft_parkour.mp4", "voiceover_006_other_woman.mp3", "tiktok_006"),
        (7, "Landlord TikTok", "subway_surfers.mp4", "voiceover_007_landlord_tiktok_gtts.mp3", "tiktok_007"),
        (8, "Professor Dark Web", "gta_driving.mp4", "voiceover_008_professor_darkweb_gtts.mp3", "tiktok_008"),
        (9, "Online Friend/Dad", "minecraft_parkour.mp4", "voiceover_009_online_friend_dad_gtts.mp3", "tiktok_009"),
    ]
    
    print("=" * 60)
    print("🎬 TIKTOK VIDEO GENERATOR PRO v2.1 - Videos 003-009")
    print("Word-by-word captions + Dramatic pauses + High quality")
    print("=" * 60)
    
    success = 0
    for num, name, gameplay, voiceover, output in videos:
        script = SCRIPTS.get(num, "")
        if script and generator.generate_video(num, name, gameplay, voiceover, output, script):
            success += 1
    
    print("\n" + "=" * 60)
    print(f"🎉 COMPLETE: {success}/{len(videos)} PRO videos generated!")
    print(f"📁 Location: {OUTPUT_DIR}/")
    print("=" * 60)
