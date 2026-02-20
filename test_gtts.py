from gtts import gTTS
import os

output_dir = "content/voiceovers"
os.makedirs(output_dir, exist_ok=True)

# Test with script 007 excerpt
test_text = "My landlord tried to evict me because of a TikTok with two million views. Apartment flooded four times."

print("🎙️ Testing gTTS (Google Translate TTS - completely FREE)...")

tts = gTTS(text=test_text, lang='en', slow=False)
output_file = os.path.join(output_dir, "test_gtts.mp3")
tts.save(output_file)

if os.path.exists(output_file):
    size = os.path.getsize(output_file) / 1024
    print(f"✅ SUCCESS! ({size:.1f} KB)")
    print(f"📁 Saved: {output_file}")
    print("🎧 Listen to test the quality!")
else:
    print("❌ Failed to create file")
