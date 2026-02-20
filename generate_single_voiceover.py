import pyttsx3
import os

output_dir = "content/voiceovers"
os.makedirs(output_dir, exist_ok=True)

engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 0.9)

# Script 1 only first - test
script1 = ("001_girlfriend_sister", "My girlfriend's sister hit on me at dinner. We've been dating two years. Her family loves me. Sunday dinner. Her parents' house. I'm the golden boyfriend. Sister keeps staring. I ignore it. She accidentally touches my leg under the table. I move my chair. She moves closer. Bathroom break. She follows me into the hallway. Grabs my hand. Whispers: I've wanted you for months. Girlfriend calls from the kitchen: Babe, you okay? Sister smiles. Don't answer. She doesn't know anything. But my phone was recording everything.")

filename, text = script1
output_file = os.path.join(output_dir, f"voiceover_{filename}_free.mp3")

print(f"🎙️ Generating: {filename}...")
engine.save_to_file(text, output_file)
engine.runAndWait()

if os.path.exists(output_file):
    size = os.path.getsize(output_file) / 1024
    print(f"✅ SUCCESS! {size:.1f} KB")
    print(f"📁 Saved: {output_file}")
else:
    print("❌ Failed")
