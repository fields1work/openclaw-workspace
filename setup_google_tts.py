# Google Cloud Text-to-Speech Setup Guide
# FREE TIER: 1 million characters per month

print("="*60)
print("📋 GOOGLE CLOUD TTS SETUP GUIDE")
print("="*60)
print("""
🎯 BENEFITS:
• FREE: 1 million characters/month
• Neural voices (sounds natural, not robotic)
• Multiple voice options (male/female, different styles)
• Better than Windows TTS, similar to ElevenLabs

📍 LOCATION to save credentials:
C:/Users/field/.openclaw/workspace/google_tts_credentials.json

🔗 Quick link:
https://console.cloud.google.com/apis/library/texttospeech.googleapis.com

⏱️ Setup time: ~5 minutes

STEPS:
1. Go to console.cloud.google.com
2. Create new project
3. Enable "Cloud Text-to-Speech API"
4. Create service account with "Cloud Text-to-Speech User" role
5. Download JSON key
6. Save as google_tts_credentials.json in workspace folder
""")

# Check if credentials already exist
import os
cred_path = "google_tts_credentials.json"
if os.path.exists(cred_path):
    print("✅ Credentials file already exists!")
    print("Ready to generate voiceovers for 007, 008, 009!")
else:
    print("⏳ Waiting for: google_tts_credentials.json")
    print("Follow the steps above, then run the generator!")
