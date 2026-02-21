# 🚀 Quick Start Guide
## TikTok Reddit Story Automation

**Get from zero to viral videos in 10 minutes.**

---

## ⚡ TL;DR (For the Impatient)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set API key
set ELEVENLABS_API_KEY=your_key_here

# 3. Generate 3 scripts
python automation.py --scripts 3

# 4. Generate 1 complete video package
python automation.py --full 1
```

---

## 📋 Detailed Setup

### Step 1: Check Python

Open Command Prompt and type:
```bash
python --version
```

**If you see a version (e.g., Python 3.10.0):** ✅ Good to go

**If "not recognized":**
1. Download Python: https://python.org/downloads
2. Install (check "Add to PATH")
3. Restart Command Prompt

---

### Step 2: Install Dependencies

Navigate to automation folder:
```bash
cd automation
```

Install all packages:
```bash
pip install -r requirements.txt
```

This will install:
- moviepy (video editing)
- elevenlabs (TTS)
- pillow (image/text)
- And 10+ more...

**Takes:** 2-5 minutes

---

### Step 3: Get ElevenLabs API Key

1. Go to: https://elevenlabs.io
2. Sign up (free tier: 10,000 chars/month)
3. Click your profile (top right)
4. Copy "API Key"

Set the key:
```bash
set ELEVENLABS_API_KEY=sk_xxxxxxxxxxxxxxxxxxxx
```

**To verify:**
```bash
python automation.py --status
```

Should show: ✅ ElevenLabs configured

---

### Step 4: Add Gameplay Footage

**Option A: Download from YouTube**
1. Search: "Subway Surfers no copyright gameplay"
2. Use 4K Video Downloader or yt-dlp
3. Save to: `assets/gameplay/subway_surfers_001.mp4`

**Option B: Use existing footage**
- Copy your existing gameplay to `assets/gameplay/`

**Requirements:**
- Format: MP4
- Length: 2-3 minutes (will be trimmed)
- Quality: 1080p or higher
- Content: Subway Surfers, Minecraft Parkour, or similar

---

### Step 5: Generate Content

**Generate 3 scripts (no API needed):**
```bash
python automation.py --scripts 3
```

**Output location:** `automation/outputs/projects/`

Each folder contains:
- `script.json` - Structured data
- `script.txt` - Human-readable
- Ready for TTS generation

**Generate 1 complete package (requires API key):**
```bash
python automation.py --full 1
```

This will:
1. Generate script
2. Call ElevenLabs API for TTS
3. Save audio file
4. Create complete package ready for video render

---

## 🎮 Windows Quick Start (Double-Click)

For non-technical users:

1. Double-click `start.bat`
2. Follow menu prompts
3. Select option 1-7

**Menu Options:**
- 1: Check system status
- 2: Generate 3 scripts
- 3: Generate 1 complete package
- 4: Generate 5 scripts (batch)
- 5: View generated projects
- 6: Open documentation
- 7: Exit

---

## 📂 Output Structure

After running, you'll have:

```
automation/outputs/
└── projects/
    └── 2026-02-20_my_wife_was_living_a_double_life/
        ├── script.json          # Machine-readable
        ├── script.txt           # Human-readable
        ├── tts_audio.mp3        # Generated voice (if --full)
        └── VIDEO_PACKAGE.md     # Full production spec
```

---

## 🎯 Next Steps

### After Generating Scripts:

1. **Review scripts** in `projects/<video_id>/script.txt`
2. **Edit if needed** (change names, adjust timing)
3. **Generate TTS** with `python automation.py --full 1`
4. **Add gameplay** to `assets/gameplay/`
5. **Render video** (Phase 2 - coming soon)

### Current Limitations (MVP):

- ✅ Script generation: **FULLY AUTOMATED**
- ✅ TTS generation: **FULLY AUTOMATED** (requires API key)
- 🔄 Video rendering: **MANUAL** (CapCut) or **SEMI-AUTO** (MoviePy - needs gameplay)
- ❌ Upload: **MANUAL** (TikTok requires mobile app)

**Phase 2 will add:**
- Full MoviePy video rendering (no CapCut needed)
- Word-level caption timing (AssemblyAI)
- Pattern interrupt automation
- Batch processing (5 videos at once)

---

## 🐛 Troubleshooting

### "pip is not recognized"
**Fix:** Reinstall Python and check "Add to PATH"

### "No module named 'moviepy'"
**Fix:** Run `pip install -r requirements.txt` from automation folder

### "ELEVENLABS_API_KEY not set"
**Fix:** 
1. Get key from https://elevenlabs.io
2. Run: `set ELEVENLABS_API_KEY=your_key`

### "No gameplay footage found"
**Fix:** Download Subway Surfers gameplay and save to `assets/gameplay/`

### Video renders but text is blurry
**Fix:** Ensure export settings are 1080x1920 @ 30fps with HIGH bitrate

---

## 📚 Documentation

- `VIRAL_FORMAT_BLUEPRINT.md` - Research and viral patterns
- `logs/SOP_Current.md` - Manual CapCut guide (backup)
- `automation/README.md` - This file
- `projects/*/VIDEO_PACKAGE.md` - Individual video specs

---

## 💪 Built For Success

This system was built by **Aneko (ViralOps)** for **Fields**.

**Mission:** Turn a 20-year-old Amazon worker into a TikTok content empire owner.

**Current Status:** MVP complete. Ready for Phase 2.

**Next Milestone:** First auto-generated video posted to TikTok.

---

**Questions? Issues?**
Fields knows where to find me. 🐾

**Now go generate some viral content.** 🔥
