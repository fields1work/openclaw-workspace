import requests
import os

# ElevenLabs API
api_key = 'sk_84c2f129b8c6eb04af4a8ff8fc8c3cc16218c4cd7a04c2dd'
voice_id = 'pNInz6obpgDQGcFmaJgB'  # Adam voice
output_dir = 'content/voiceovers'

# Create output directory if needed
os.makedirs(output_dir, exist_ok=True)

# All 9 scripts condensed for voiceover
scripts = [
    ("001_girlfriend_sister", "My girlfriend's sister hit on me at dinner. We've been dating two years. Her family loves me. Sunday dinner. Her parents' house. I'm the golden boyfriend. Sister keeps staring. I ignore it. She accidentally touches my leg under the table. I move my chair. She moves closer. Bathroom break. She follows me into the hallway. Grabs my hand. Whispers: I've wanted you for months. Girlfriend calls from the kitchen: Babe, you okay? Sister smiles. Don't answer. She doesn't know anything. But my phone was recording everything."),
    
    ("002_boss_affair", "My boss paid me two thousand dollars to cover his affair. I'm his assistant. Six months on the job. His wife calls the office daily. Thinks he's working late. He gives me a second phone. Answer if she calls. One rule: Never mention the hotel charges. I book his business dinners at five star hotels. Last week, I met the woman I'm covering for. She's his wife's best friend from college. She looked me in the eyes: You know this is wrong. I nodded. Then checked my bank account. The deposit cleared. But so did my conscience."),
    
    ("003_fired_revelation", "I found out why they really fired me. Worked at this startup for two years. Last Tuesday, HR called me in. Budget cuts. But my access card still worked that night. Went back to grab my stuff from the server room. Heard my boss talking. Door was cracked. We had to fire someone. Investors love cost cutting. They fired me so the CEO could keep his fifty thousand dollar bonus. Then I saw the numbers on his screen. The company wasn't broke. They just posted record profits. I took photos before security found me."),
    
    ("004_money_hustle", "How I made one thousand three hundred forty seven dollars in one week without a job. Got laid off on Monday. Rent due Friday. No time for job applications. Needed cash now. Day one: Listed my skills on Craigslist. Day two: Three people wanted help with AI prompts. Day three: Charged two hundred dollars per person. Took twenty minutes each. Day four: Repeat clients. They told friends. Day five: Eight hundred forty seven earned. Rent covered. Day six and seven: Scaled to one thousand three hundred forty seven. Found my business. The skill everyone paid for? Copy paste from Chat GPT. Your nine to five is training. Your bills are motivation."),
]

total_chars = 0
total_credits = 0

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
            credits = chars  # Approximate: 1 char = 1 credit
            total_credits += credits
            print(f"✅ Saved! (~{credits} credits)")
        else:
            print(f"❌ Error {response.status_code}: {response.text[:100]}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")

print(f"\n🎉 BATCH COMPLETE!")
print(f"📊 Total characters: {total_chars}")
print(f"📊 Estimated credits: ~{total_credits}")
print(f"📁 Saved to: {output_dir}/")
