import pyttsx3
import os

# Test Windows built-in TTS (completely free!)
output_dir = "content/voiceovers"
os.makedirs(output_dir, exist_ok=True)

# Initialize TTS engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')
print(f"🎙️ Available voices: {len(voices)}")
for i, voice in enumerate(voices[:3]):  # Show first 3
    print(f"  {i}: {voice.name}")

# Test with first script excerpt
test_text = "My girlfriend's sister hit on me at dinner. We've been dating two years. Her family loves me."

# Try to set a good voice
if len(voices) > 0:
    engine.setProperty('voice', voices[0].id)
    
# Adjust speed (slower for TikTok = better)
engine.setProperty('rate', 150)  # Default is usually 200

# Save to file
output_file = f"{output_dir}/test_windows_tts.mp3"
engine.save_to_file(test_text, output_file)
engine.runAndWait()

print(f"✅ Test file saved: {output_file}")
print(f"📊 Check if it sounds good!")
