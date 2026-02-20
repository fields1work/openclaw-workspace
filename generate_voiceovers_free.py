import pyttsx3
import os

# FREE Windows TTS Solution (no ElevenLabs credits needed!)
output_dir = "content/voiceovers"
os.makedirs(output_dir, exist_ok=True)

# Initialize TTS engine
engine = pyttsx3.init()

# Get voices
voices = engine.getProperty('voices')
print(f"🎙️ Available voices: {len(voices)}")
for i, voice in enumerate(voices):
    print(f"  {i}: {voice.name}")

# Scripts to generate (001-009)
scripts = [
    ("001_girlfriend_sister", "My girlfriend's sister hit on me at dinner. We've been dating two years. Her family loves me. Sunday dinner. Her parents' house. I'm the golden boyfriend. Sister keeps staring. I ignore it. She accidentally touches my leg under the table. I move my chair. She moves closer. Bathroom break. She follows me into the hallway. Grabs my hand. Whispers: I've wanted you for months. Girlfriend calls from the kitchen: Babe, you okay? Sister smiles. Don't answer. She doesn't know anything. But my phone was recording everything."),
    
    ("002_boss_affair", "My boss paid me two thousand dollars to cover his affair. I'm his assistant. Six months on the job. His wife calls the office daily. Thinks he's working late. He gives me a second phone. Answer if she calls. One rule: Never mention the hotel charges. I book his business dinners at five star hotels. Last week, I met the woman I'm covering for. She's his wife's best friend from college. She looked me in the eyes: You know this is wrong. I nodded. Then checked my bank account. The deposit cleared. But so did my conscience."),
    
    ("003_fired_revelation", "I found out why they really fired me. Worked at this startup for two years. Last Tuesday, HR called me in. Budget cuts. But my access card still worked that night. Went back to grab my stuff from the server room. Heard my boss talking. Door was cracked. We had to fire someone. Investors love cost cutting. They fired me so the CEO could keep his fifty thousand dollar bonus. Then I saw the numbers on his screen. The company wasn't broke. They just posted record profits. I took photos before security found me."),
    
    ("004_money_hustle", "How I made one thousand three hundred forty seven dollars in one week without a job. Got laid off on Monday. Rent due Friday. No time for job applications. Needed cash now. Day one: Listed my skills on Craigslist. Day two: Three people wanted help with AI prompts. Day three: Charged two hundred dollars per person. Took twenty minutes each. Day four: Repeat clients. They told friends. Day five: Eight hundred forty seven earned. Rent covered. Day six and seven: Scaled to one thousand three hundred forty seven. Found my business. The skill everyone paid for? Copy paste from Chat GPT. Your nine to five is training. Your bills are motivation."),
    
    ("005_roommate_adderall", "Found out my roommate's been stealing my Adderall for six months. Prescribed for ADHD. Bottle was always running low. Thought I was just taking more than I remembered. Set up a hidden camera. Wanted to catch myself sleepwalking. Day three footage: Roommate at three AM. Opening my desk drawer. Counting pills. Taking four. Putting bottle back exactly. He'd been doing this for one hundred eighty seven days. Confronted him. He laughed: You owe me for all the times I covered your rent. I checked. Rent was auto-pay from my account. He never paid once."),
    
    ("006_other_woman", "I was the other woman for three years, and I had no idea. Met David at a coffee shop. Instant connection. Dated three years. Talked about moving in together. He traveled for work every other weekend. Said it was consulting. Last month: Found a receipt. Different name on the credit card. Not David. Name was Michael. Same last name. Reverse searched the number. Wedding registry from twenty nineteen. Michael. Married. Two kids. The consulting trips? Family vacations. I looked at our photos. Every work trip day matched his family posts."),
    
    ("007_landlord_tiktok", "My landlord tried to evict me because of a TikTok with two million views. Apartment flooded four times. Landlord said tough luck. Made a TikTok. Just showed the water. Didn't name him. Video hit two million views. Local news picked it up. Day later: Thirty day eviction notice. Violation of lease agreement. Clause cited: No social media without written consent. I read my lease. That clause was added in pen. After I signed. Lawyer looked at it. Said the added ink was six months newer than my signature."),
    
    ("008_professor_darkweb", "My professor was selling exam answers on the dark web for five hundred dollars. Organic Chemistry. Hardest class in the university. Professor always said nobody gets an A, it's designed that way. Friend bought study guide from a forum. Five hundred dollars. Bitcoin only. It was the exact exam. Every question. In order. I started investigating. Forum seller: ChemProfEightyEight. Posted a photo of his unreleased textbook from his desk. Matched background to his office window. I sat in on his night class. Took a photo. Posted on forum: Is this ChemProfEightyEight? Five minutes later: Account deleted. Too late. Two hundred students saw it."),
    
    ("009_online_friend_dad", "My online gaming friend of five years was my dad. Met Alex on Minecraft when I was thirteen. Five years of gaming together. He taught me so much about life. He knew weird details. How's your mom's lasagna recipe going? Never told him my mom made lasagna. Never mentioned it. He used phrases my dad uses. Same jokes. Same advice. I joked: You're not my dad are you? Five minutes of silence. He admitted it. Said he wanted to know me without the dad label. Found out I was gay through our chats. Planned how to support me. Before I came out to the family. He was already ready. Five years of secret friendship, just to be a better dad."),
]

# Generate each voiceover
voice_choice = 0  # Microsoft David (male) - good for Reddit stories
engine.setProperty('voice', voices[voice_choice].id)
engine.setProperty('rate', 160)  # Slightly slower for clarity
engine.setProperty('volume', 0.9)

print(f"\n🎙️ Using voice: {voices[voice_choice].name}")
print(f"🚀 Generating {len(scripts)} voiceovers...\n")

for i, (filename, text) in enumerate(scripts, 1):
    output_file = os.path.join(output_dir, f"voiceover_{filename}_free.mp3")
    
    print(f"[{i}/{len(scripts)}] 🎙️ voiceover_{filename}_free.mp3...")
    
    try:
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        
        # Check file was created
        if os.path.exists(output_file):
            size = os.path.getsize(output_file) / 1024  # KB
            print(f"     ✅ Done! ({size:.1f} KB)")
        else:
            print(f"     ⚠️ File not created")
            
    except Exception as e:
        print(f"     ❌ Error: {e}")

print(f"\n🎉 ALL VOICEOVERS COMPLETE!")
print(f"💰 Cost: $0 (Windows built-in TTS)")
print(f"📁 Location: {output_dir}/")
