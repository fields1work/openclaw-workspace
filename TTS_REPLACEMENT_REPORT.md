# 🎙️ TTS REPLACEMENT REPORT
## ElevenLabs Alternative for TikTok Reddit Stories
**Research Date:** Feb 20, 2026 | **Status:** COMPLETE ✅

---

## 🎯 EXECUTIVE SUMMARY

**Problem:** ElevenLabs tokens exhausted, need free TTS alternative

**Solution Found:** **Edge-TTS** - Python module using Microsoft Edge's online TTS service

**Cost:** **100% FREE** - No API key, no account, no limits

**Quality:** Neural voices, natural sounding, multiple options

**Speed:** 1.10x-1.25x adjustable (perfect for viral TikTok pacing)

**Winner:** Edge-TTS (en-US-GuyNeural or en-US-JennyNeural)

---

## 📊 PHASE 1: MARKET MAP - 10 TTS CANDIDATES

### Category A: Online/Cloud-Based (Free)

#### 1. **Edge-TTS** ⭐ WINNER
- **Cost:** FREE (no API key, no account)
- **Source:** Microsoft Edge online TTS service
- **Voices:** 300+ voices, 70+ languages
- **Quality:** Neural, natural, excellent
- **Speed:** Adjustable (0.5x - 2.0x)
- **Output:** MP3, WAV, SRT subtitles
- **License:** Microsoft's service (fair use for content creation)
- **Pros:** No setup, no limits, high quality, fast
- **Cons:** Requires internet, not local
- **Setup:** `pip install edge-tts`
- **Best For:** TikTok Reddit stories (FAST, FREE, QUALITY)

#### 2. **gTTS (Google Text-to-Speech)**
- **Cost:** FREE
- **Source:** Google Translate TTS
- **Voices:** Limited (few languages)
- **Quality:** Basic, robotic
- **Speed:** Not adjustable
- **License:** Google Terms (personal use)
- **Pros:** Simple, no API key
- **Cons:** Robotic voice, limited customization
- **Verdict:** ❌ Too robotic for viral content

#### 3. **Azure TTS Free Tier**
- **Cost:** FREE tier (500K chars/month)
- **Source:** Microsoft Azure
- **Voices:** Neural, high quality
- **License:** Azure terms (requires account)
- **Pros:** Professional quality
- **Cons:** Requires Azure account, API key, limits
- **Verdict:** ❌ Requires account/setup

---

### Category B: Local/Open Source

#### 4. **Piper** ⭐ RUNNER-UP
- **Cost:** FREE (open source)
- **Source:** Local neural TTS
- **Voices:** 20+ voices (English, etc.)
- **Quality:** Very good, natural
- **Speed:** Adjustable
- **License:** MIT (commercial use OK)
- **Pros:** Local (no internet), fast, private, open source
- **Cons:** Requires voice model download (~50-100MB each), setup complexity
- **Setup:** Download + install Piper + download voice models
- **Best For:** Privacy-conscious, offline use, long-term scaling

#### 5. **Coqui TTS**
- **Cost:** FREE (open source)
- **Source:** Local deep learning TTS
- **Voices:** Multiple models
- **Quality:** Good, but requires GPU for best performance
- **License:** MPL 2.0
- **Pros:** Highly customizable, can train own voices
- **Cons:** Complex setup, requires technical knowledge, slower than Piper
- **Verdict:** ❌ Too complex for immediate use

#### 6. **eSpeak / eSpeak-NG**
- **Cost:** FREE (open source)
- **Source:** Local TTS
- **Quality:** Robotic, outdated
- **License:** GPL
- **Verdict:** ❌ Too robotic for viral content

---

### Category C: Browser/OS Built-in

#### 7. **Windows Natural Voices (SAPI5)**
- **Cost:** FREE (Windows built-in)
- **Source:** Windows TTS
- **Voices:** 8+ voices (David, Zira, Mark, etc.)
- **Quality:** Good (David is decent)
- **License:** Windows license
- **Pros:** No install, built-in
- **Cons:** Limited voices, requires NaturalVoiceSAPIAdapter for neural
- **Best For:** Quick testing, no setup

#### 8. **Microsoft Edge Read Aloud**
- **Cost:** FREE (Edge browser)
- **Source:** Edge browser feature
- **Voices:** Neural voices (Sonia, Emma, etc.)
- **Quality:** Excellent
- **License:** Microsoft terms
- **Pros:** High quality, natural
- **Cons:** Requires manual browser use, not automatable
- **Verdict:** ❌ Not suitable for automation

---

### Category D: Hybrid/Multi-Engine

#### 9. **RealtimeTTS**
- **Cost:** FREE (wrapper library)
- **Source:** Python library supporting multiple TTS engines
- **Engines:** Edge TTS, Piper, Coqui, Azure, ElevenLabs, etc.
- **License:** MIT
- **Pros:** Switch between engines easily
- **Cons:** Adds complexity layer
- **Best For:** Future-proofing, testing multiple engines

#### 10. **pyttsx3**
- **Cost:** FREE
- **Source:** Python wrapper for system TTS
- **Engines:** Windows SAPI5, NSSpeechSynthesizer (Mac), espeak (Linux)
- **Quality:** System dependent
- **Verdict:** ❌ Limited quality, system dependent

---

## 🏆 PHASE 2: TOP 3 FINALISTS

### 🥇 WINNER: Edge-TTS

**Why it wins:**
- ✅ **100% FREE** - No API key, no account, no limits
- ✅ **Neural quality** - Microsoft Edge voices are excellent
- ✅ **300+ voices** - 70+ languages, multiple English options
- ✅ **Speed control** - Adjustable 0.5x to 2.0x (perfect for 1.10x viral pacing)
- ✅ **Easy setup** - `pip install edge-tts`
- ✅ **Outputs SRT** - Auto-generates subtitle files
- ✅ **Legal** - Uses Microsoft's public Edge service

**Best voices for TikTok:**
- `en-US-GuyNeural` - Male, conversational, natural
- `en-US-JennyNeural` - Female, clear, engaging
- `en-GB-SoniaNeural` - Female, UK accent (stands out)
- `en-US-AriaNeural` - Female, expressive

**Setup complexity:** EASY (1 minute)
**Automation potential:** EXCELLENT
**Quality:** 9/10

---

### 🥈 RUNNER-UP: Piper

**Why it's second:**
- ✅ **100% FREE** - Open source, MIT license
- ✅ **Local** - No internet required, fully private
- ✅ **Fast** - Real-time synthesis on CPU
- ✅ **Good quality** - Neural voices, natural sounding
- ✅ **20+ voices** - English and other languages
- ⚠️ **Setup complexity** - Must download voice models (~50-100MB each)
- ⚠️ **Fewer voices** - Limited selection vs Edge-TTS

**Best voices:**
- `en_US-lessac-medium` - Male, natural
- `en_US-amy-medium` - Female, clear
- `en_GB-southern_male-medium` - UK male

**Setup complexity:** MEDIUM (10 minutes)
**Automation potential:** EXCELLENT
**Quality:** 8/10

---

### 🥉 THIRD PLACE: Windows Natural Voices (SAPI5)

**Why it's third:**
- ✅ **100% FREE** - Built into Windows
- ✅ **No install** - Already on your system
- ✅ **Simple** - Works with pyttsx3
- ⚠️ **Limited quality** - Not neural, less natural
- ⚠️ **Few voices** - Only 8 options
- ⚠️ **Requires adapter** - For best quality, need NaturalVoiceSAPIAdapter

**Best voices:**
- `David` - Male, best of built-in
- `Zira` - Female, decent

**Setup complexity:** EASY (already installed)
**Automation potential:** GOOD
**Quality:** 6/10

---

## 📋 PHASE 3: IMPLEMENTATION PLAN

### Winner: Edge-TTS Complete Setup

#### Step 1: Install (1 minute)
```bash
pip install edge-tts
```

#### Step 2: List Available Voices
```bash
edge-tts --list-voices | findstr "en-US en-GB"
```

**Recommended voices for TikTok:**
- `en-US-GuyNeural` - Male, conversational (BEST for Reddit stories)
- `en-US-JennyNeural` - Female, clear and engaging
- `en-GB-SoniaNeural` - Female, UK accent (stands out)
- `en-US-AriaNeural` - Female, expressive

#### Step 3: Generate TTS with Viral Settings
```bash
# Basic usage
edge-tts --voice en-US-GuyNeural --text "Your script here" --write-media output.mp3 --write-subtitles output.srt

# With speed adjustment (1.10x for viral pacing)
edge-tts --voice en-US-GuyNeural --rate=+10% --text "Your script here" --write-media output.mp3

# With volume adjustment
edge-tts --voice en-US-GuyNeural --rate=+10% --volume=+0% --text "Your script here" --write-media output.mp3
```

#### Step 4: Python Integration
```python
import asyncio
import edge_tts

async def generate_tts(text, output_file, voice="en-US-GuyNeural", rate="+10%"):
    """Generate TTS with viral settings."""
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(output_file)

# Usage
asyncio.run(generate_tts(
    "My wife was living a double life...",
    "output.mp3",
    voice="en-US-GuyNeural",
    rate="+10%"
))
```

---

## 🎬 PHASE 4: CAPCUT INTEGRATION

### Step-by-Step Editing Recipe

#### Step 1: Import Assets
1. Open CapCut Desktop
2. Click **Import**
3. Select:
   - Gameplay video (Subway Surfers/Minecraft)
   - TTS audio file (from Edge-TTS)
   - (Optional) SRT subtitle file (auto-generated by Edge-TTS)

#### Step 2: Add to Timeline
1. Drag gameplay to **Video Track (V1)**
2. Drag TTS audio to **Audio Track (A1)**
3. Trim gameplay to match TTS length

#### Step 3: Add Captions
**Option A: Use Auto-Captions (Recommended)**
1. Click **Text** → **Auto Captions**
2. Select audio track
3. CapCut generates captions automatically
4. Style captions:
   - Font: **Montserrat Bold** or **Arial Bold**
   - Size: **54pt**
   - Color: **White (#FFFFFF)**
   - Stroke: **Black, 4pt**
   - Position: **Lower third**

**Option B: Import SRT from Edge-TTS**
1. Click **Text** → **Import Subtitles**
2. Select SRT file generated by Edge-TTS
3. Style as above

#### Step 4: Add Hook (First 3 Seconds)
1. At 0:00, add text overlay
2. Type your hook (e.g., "My wife was living a double life")
3. Style:
   - Font: **Montserrat Bold**
   - Size: **72pt**
   - Color: **Orange (#FF6B35)**
   - Stroke: **Black, 5pt**
   - Position: **Center**
4. Duration: **Exactly 3 seconds**

#### Step 5: Pattern Interrupts
Every 5-7 seconds, add subtle effect:
1. **Micro Zoom:** Scale 100% → 105% → 100% over 0.5s
2. **Quick Cut:** Switch to different gameplay segment
3. **Speed Ramp:** 1.5x speed for 1 second

#### Step 6: Export Settings
1. Click **Export** (top right)
2. Settings:
   - Resolution: **1080x1920**
   - FPS: **30**
   - Bitrate: **HIGH** (~10-12 Mbps)
   - Codec: **H.264**
   - Format: **MP4**
3. Click **Export**

#### Step 7: Upload to TikTok
1. Transfer MP4 to phone
2. Open TikTok app
3. Tap **+** → **Upload**
4. Add caption + hashtags
5. Post

---

## ⚙️ PHASE 5: DEFAULT SETTINGS PRESET

### Edge-TTS Viral Settings

```python
# Default configuration for TikTok Reddit stories
TTS_CONFIG = {
    "voice": "en-US-GuyNeural",  # Male, conversational
    "rate": "+10%",              # 1.10x speed (viral sweet spot)
    "volume": "+0%",             # Default volume
    "pitch": "+0Hz",             # Default pitch
}

# Alternative voices
VOICES = {
    "male_conversational": "en-US-GuyNeural",
    "female_clear": "en-US-JennyNeural", 
    "female_uk": "en-GB-SoniaNeural",
    "female_expressive": "en-US-AriaNeural",
    "male_deep": "en-US-DavisNeural",
}

# Speed settings
SPEED_OPTIONS = {
    "normal": "+0%",      # 1.0x
    "viral": "+10%",      # 1.1x (recommended)
    "fast": "+20%",       # 1.2x
    "ultra": "+30%",      # 1.3x
}
```

### Caption Settings (CapCut)

```
Font: Montserrat Bold (or Arial Bold)
Size: 54pt (body), 72pt (hook)
Color: White (#FFFFFF) for body, Orange (#FF6B35) for hook
Stroke: Black, 4pt (body), 5pt (hook)
Position: Lower third (body), Center (hook)
Max Lines: 2
Max Words Per Caption: 10
```

### Export Settings (TikTok)

```
Resolution: 1080x1920 (9:16)
FPS: 30
Bitrate: 10-12 Mbps
Codec: H.264
Audio: AAC, 192kbps
Format: MP4
File Size Target: 30-60MB for 60s video
```

---

## 🐛 PHASE 6: TROUBLESHOOTING

### Edge-TTS Issues

**"Command not found: edge-tts"**
- Fix: `pip install edge-tts`

**"No module named 'edge_tts'"**
- Fix: `pip install edge-tts` (in correct Python environment)

**"Connection error"**
- Fix: Check internet connection (Edge-TTS uses Microsoft's online service)

**"Voice not found"**
- Fix: Run `edge-tts --list-voices` to see available voices

### CapCut Issues

**"Captions not syncing"**
- Fix: Use Auto-Captions feature or import SRT from Edge-TTS

**"Text looks blurry"**
- Fix: Export at HIGH bitrate, ensure 1080p resolution

**"Audio out of sync"**
- Fix: Re-import audio, check gameplay framerate

---

## 🎓 PHASE 7: BATCH WORKFLOW

### Generate 10 Scripts at Once

```bash
# Generate 10 scripts
python automation.py --scripts 10

# Review and select best 3
# (Manual review of script.txt files)

# Generate TTS for selected 3
for script in selected_scripts:
    edge-tts --voice en-US-GuyNeural --rate=+10% --text "$(cat script.txt)" --write-media output.mp3
```

### Daily Production Workflow

**Morning (10 minutes):**
```bash
# Generate 3 scripts
python automation.py --scripts 3

# Auto-generate TTS
python automation.py --full 3
```

**Review (15 minutes):**
- Listen to 3 TTS files
- Select best 2
- Note any pronunciation issues

**Production (30 minutes):**
- Import to CapCut
- Add gameplay
- Edit captions
- Add pattern interrupts
- Export 2 videos

**Upload (10 minutes):**
- Transfer to phone
- Upload to TikTok
- Add captions + hashtags
- Post

**Total: 75 minutes for 2 videos** (vs. 2.5 hours manually)

---

## 📈 SUCCESS METRICS

### TTS Quality Checklist

- [ ] Voice sounds natural (not robotic)
- [ ] Clear pronunciation at 1.10x speed
- [ ] Consistent volume throughout
- [ ] No audio glitches or artifacts
- [ ] Proper emphasis on emotional words
- [ ] Natural pauses at punctuation

### Caption Sync Checklist

- [ ] Captions appear exactly when words are spoken
- [ ] No lag or delay
- [ ] Readable at 1.10x speed
- [ ] Max 2 lines per caption
- [ ] Max 10 words per caption
- [ ] Hook text is orange and centered

### Export Quality Checklist

- [ ] Resolution: 1080x1920
- [ ] FPS: 30
- [ ] Bitrate: 10-12 Mbps
- [ ] File size: 30-60MB
- [ ] Audio synced
- [ ] Text sharp and readable

---

## 🎯 FINAL RECOMMENDATION

### Use Edge-TTS (en-US-GuyNeural)

**Why:**
- Completely free (no tokens, no limits)
- Neural quality (natural sounding)
- No setup (just `pip install`)
- Fast (online service)
- Adjustable speed (1.10x viral sweet spot)
- Outputs MP3 + SRT subtitles
- Legal (Microsoft's public service)

**Command:**
```bash
edge-tts --voice en-US-GuyNeural --rate=+10% --text "Your script here" --write-media output.mp3 --write-subtitles output.srt
```

**Integration:**
Replace ElevenLabs in `automation/tts_generator.py` with Edge-TTS calls.

---

## 🚀 NEXT STEPS

1. **Install Edge-TTS:**
   ```bash
   pip install edge-tts
   ```

2. **Test voice:**
   ```bash
   edge-tts --voice en-US-GuyNeural --text "My wife was living a double life" --write-media test.mp3
   ```

3. **Update automation code:**
   - Modify `automation/tts_generator.py` to use Edge-TTS
   - Remove ElevenLabs dependency
   - Test full pipeline

4. **Generate first video:**
   ```bash
   python automation.py --full 1
   ```

---

## 📚 SOURCES

1. **Edge-TTS GitHub:** https://github.com/rany2/edge-tts
2. **Edge-TTS PyPI:** https://pypi.org/project/edge-tts/
3. **Voice Samples:** https://tts.travisvn.com/
4. **Piper TTS:** https://github.com/rhasspy/piper
5. **Microsoft TTS Docs:** https://support.microsoft.com/en-us/topic/download-languages-and-voices-for-immersive-reader-read-mode-and-read-aloud-4c83a8d8-7486-42f7-8e46-2b0fdf753130

---

**Research Complete.** 🎯

**Recommendation:** Use **Edge-TTS** (en-US-GuyNeural) - completely free, neural quality, no limits.

**Ready to implement.** 🚀

**- Aneko (TTS-Scout + Integrator)** 🐾
