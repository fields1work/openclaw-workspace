from gtts import gTTS
import os

output_dir = "content/voiceovers"
os.makedirs(output_dir, exist_ok=True)

# Scripts 007, 008, 009
scripts = [
    ("007_landlord_tiktok_gtts", "My landlord tried to evict me because of a TikTok with two million views. Apartment flooded four times. Landlord said tough luck. Made a TikTok. Just showed the water. Did not name him. Video hit two million views. Local news picked it up. Day later: Thirty day eviction notice. Violation of lease agreement. Clause cited: No social media without written consent. I read my lease. That clause was added in pen. After I signed. Lawyer looked at it. Said the added ink was six months newer than my signature."),
    
    ("008_professor_darkweb_gtts", "My professor was selling exam answers on the dark web for five hundred dollars. Organic Chemistry. Hardest class in the university. Professor always said nobody gets an A, it is designed that way. Friend bought study guide from a forum. Five hundred dollars. Bitcoin only. It was the exact exam. Every question. In order. I started investigating. Forum seller: ChemProfEightyEight. Posted a photo of his unreleased textbook from his desk. Matched background to his office window. I sat in on his night class. Took a photo. Posted on forum: Is this ChemProfEightyEight? Five minutes later: Account deleted. Too late. Two hundred students saw it."),
    
    ("009_online_friend_dad_gtts", "My online gaming friend of five years was my dad. Met Alex on Minecraft when I was thirteen. Five years of gaming together. He taught me so much about life. He knew weird details. How is your moms lasagna recipe going? Never told him my mom made lasagna. Never mentioned it. He used phrases my dad uses. Same jokes. Same advice. I joked: You are not my dad are you? Five minutes of silence. He admitted it. Said he wanted to know me without the dad label. Found out I was gay through our chats. Planned how to support me. Before I came out to the family. He was already ready. Five years of secret friendship, just to be a better dad."),
]

print("🎙️ GTTS VOICEOVER GENERATOR")
print("="*50)
print("Using Google Translate TTS - Completely FREE!")
print("No API key, no billing, no limits!\n")

for i, (filename, text) in enumerate(scripts, 1):
    print(f"[{i}/3] Generating {filename}...")
    
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        output_file = os.path.join(output_dir, f"voiceover_{filename}.mp3")
        tts.save(output_file)
        
        if os.path.exists(output_file):
            size = os.path.getsize(output_file) / 1024
            print(f"      ✅ Done! ({size:.1f} KB)")
        else:
            print(f"      ❌ File not created")
    except Exception as e:
        print(f"      ❌ Error: {str(e)[:50]}")

print(f"\n🎉 ALL 3 VOICEOVERS COMPLETE!")
print(f"💰 Total cost: $0.00")
print(f"🎧 Check them out and compare quality!")
