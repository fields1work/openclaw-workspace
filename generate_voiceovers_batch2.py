import requests
import os

# ElevenLabs API
api_key = 'sk_84c2f129b8c6eb04af4a8ff8fc8c3cc16218c4cd7a04c2dd'
voice_id = 'pNInz6obpgDQGcFmaJgB'  # Adam voice
output_dir = 'content/voiceovers'

os.makedirs(output_dir, exist_ok=True)

# Scripts 005-009
scripts = [
    ("005_roommate_adderall", "Found out my roommate's been stealing my Adderall for six months. Prescribed for ADHD. Bottle was always running low. Thought I was just taking more than I remembered. Set up a hidden camera. Wanted to catch myself sleepwalking. Day three footage: Roommate at three AM. Opening my desk drawer. Counting pills. Taking four. Putting bottle back exactly. He'd been doing this for one hundred eighty seven days. Confronted him. He laughed: You owe me for all the times I covered your rent. I checked. Rent was auto-pay from my account. He never paid once."),
    
    ("006_other_woman", "I was the other woman for three years, and I had no idea. Met David at a coffee shop. Instant connection. Dated three years. Talked about moving in together. He traveled for work every other weekend. Said it was consulting. Last month: Found a receipt. Different name on the credit card. Not David. Name was Michael. Same last name. Reverse searched the number. Wedding registry from twenty nineteen. Michael. Married. Two kids. The consulting trips? Family vacations. I looked at our photos. Every work trip day matched his family posts."),
    
    ("007_landlord_tiktok", "My landlord tried to evict me because of a TikTok with two million views. Apartment flooded four times. Landlord said tough luck. Made a TikTok. Just showed the water. Didn't name him. Video hit two million views. Local news picked it up. Day later: Thirty day eviction notice. Violation of lease agreement. Clause cited: No social media without written consent. I read my lease. That clause was added in pen. After I signed. Lawyer looked at it. Said the added ink was six months newer than my signature."),
    
    ("008_professor_darkweb", "My professor was selling exam answers on the dark web for five hundred dollars. Organic Chemistry. Hardest class in the university. Professor always said nobody gets an A, it's designed that way. Friend bought study guide from a forum. Five hundred dollars. Bitcoin only. It was the exact exam. Every question. In order. I started investigating. Forum seller: ChemProfEightyEight. Posted a photo of his unreleased textbook from his desk. Matched background to his office window. I sat in on his night class. Took a photo. Posted on forum: Is this ChemProfEightyEight? Five minutes later: Account deleted. Too late. Two hundred students saw it."),
    
    ("009_online_friend_dad", "My online gaming friend of five years was my dad. Met Alex on Minecraft when I was thirteen. Five years of gaming together. He taught me so much about life. He knew weird details. How's your mom's lasagna recipe going? Never told him my mom made lasagna. Never mentioned it. He used phrases my dad uses. Same jokes. Same advice. I joked: You're not my dad are you? Five minutes of silence. He admitted it. Said he wanted to know me without the dad label. Found out I was gay through our chats. Planned how to support me. Before I came out to the family. He was already ready. Five years of secret friendship, just to be a better dad."),
]

total_chars = 0

for filename, text in scripts:
    print(f"🎙️ Generating {filename}...")
    
    try:
        response = requests.post(
            f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}',
            headers={'xi-api-key': api_key, 'Content-Type': 'application/json'},
            json={
                'text': text, 
                'voice_settings': {'stability': 0.5, 'similarity_boost': 0.5}
            },
            timeout=60
        )
        
        if response.status_code == 200:
            filepath = os.path.join(output_dir, f"voiceover_{filename}.mp3")
            with open(filepath, 'wb') as f:
                f.write(response.content)
            chars = len(text)
            total_chars += chars
            print(f"✅ Saved! (~{chars} credits)")
        else:
            print(f"❌ Error {response.status_code}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")

print(f"\n🎉 BATCH 2 COMPLETE!")
print(f"📊 Total characters: {total_chars}")
print(f"📊 Estimated credits: ~{total_chars}")
