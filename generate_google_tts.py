#!/usr/bin/env python3
"""
Google Cloud TTS Voiceover Generator
FREE TIER: 1 million characters/month
"""

import os
from google.cloud import texttospeech

# Configuration
output_dir = "content/voiceovers"
os.makedirs(output_dir, exist_ok=True)

# Scripts to generate (007, 008, 009)
scripts = [
    ("007_landlord_tiktok", """My landlord tried to evict me because of a TikTok with two million views. Apartment flooded four times. Landlord said tough luck. Made a TikTok. Just showed the water. Didn't name him. Video hit two million views. Local news picked it up. Day later: Thirty day eviction notice. Violation of lease agreement. Clause cited: No social media without written consent. I read my lease. That clause was added in pen. After I signed. Lawyer looked at it. Said the added ink was six months newer than my signature."""),
    
    ("008_professor_darkweb", """My professor was selling exam answers on the dark web for five hundred dollars. Organic Chemistry. Hardest class in the university. Professor always said nobody gets an A, it's designed that way. Friend bought study guide from a forum. Five hundred dollars. Bitcoin only. It was the exact exam. Every question. In order. I started investigating. Forum seller: ChemProfEightyEight. Posted a photo of his unreleased textbook from his desk. Matched background to his office window. I sat in on his night class. Took a photo. Posted on forum: Is this ChemProfEightyEight? Five minutes later: Account deleted. Too late. Two hundred students saw it."""),
    
    ("009_online_friend_dad", """My online gaming friend of five years was my dad. Met Alex on Minecraft when I was thirteen. Five years of gaming together. He taught me so much about life. He knew weird details. How is your moms lasagna recipe going? Never told him my mom made lasagna. Never mentioned it. He used phrases my dad uses. Same jokes. Same advice. I joked: You are not my dad are you? Five minutes of silence. He admitted it. Said he wanted to know me without the dad label. Found out I was gay through our chats. Planned how to support me. Before I came out to the family. He was already ready. Five years of secret friendship, just to be a better dad."""),
]

def generate_voiceover(filename, text):
    """Generate voiceover using Google Cloud TTS"""
    client = texttospeech.TextToSpeechClient()
    
    synthesis_input = texttospeech.SynthesisInput(text=text)
    
    # Select voice (neural2 sounds most natural)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Neural2-D",  # Male voice, very natural
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )
    
    # Audio configuration
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=1.0,  # Normal speed
        pitch=0.0,  # Normal pitch
    )
    
    # Generate
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    
    # Save
    output_file = os.path.join(output_dir, f"voiceover_{filename}_google.mp3")
    with open(output_file, "wb") as out:
        out.write(response.audio_content)
    
    return output_file

# Main execution
print("🎙️ GOOGLE CLOUD TTS VOICEOVER GENERATOR")
print("="*50)

# Check for credentials
cred_path = "google_tts_credentials.json"
if not os.path.exists(cred_path):
    print(f"❌ Missing: {cred_path}")
    print("Run setup_google_tts.py for instructions!")
    exit(1)

# Set credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred_path

print(f"Generating {len(scripts)} voiceovers...\n")

for i, (filename, text) in enumerate(scripts, 1):
    print(f"[{i}/{len(scripts)}] 🎙️ Generating {filename}...")
    try:
        output_file = generate_voiceover(filename, text)
        size = os.path.getsize(output_file) / 1024
        print(f"      ✅ Done! ({size:.1f} KB)")
    except Exception as e:
        print(f"      ❌ Error: {str(e)[:60]}")

print(f"\n🎉 GOOGLE TTS COMPLETE!")
print(f"💰 Used: ~{sum(len(s[1]) for s in scripts)} chars of 1M free tier")
print(f"📁 Location: {output_dir}/")
