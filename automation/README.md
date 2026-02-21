# 🚀 TikTok Reddit Story Automation System

**Full automation pipeline for viral Reddit story TikTok videos.**

Built by Aneko (ViralOps) for Fields. Reduces video production time from 70 minutes to 5 minutes (93% reduction).

---

## 📊 What This Does

**Before (Manual):**
- Find story: 15 min
- Write script: 20 min
- Record TTS: 10 min
- Edit in CapCut: 20 min
- Export: 5 min
- **Total: 70 min/video**

**After (Automated):**
- Generate script: 10 seconds
- Generate TTS: 2 min (API call)
- Render video: 2 min
- **Total: ~5 min/video**

**Result:** You can produce **10-20 videos/day** instead of 3-4.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    AUTOMATION PIPELINE                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌─────────────┐ │
│  │ Script       │───▶│ TTS          │───▶│ Video         │ │
│  │ Engine       │    │ Generator    │    │ Renderer      │ │
│  └──────────────┘    └──────────────┘    └─────────────┘ │
│         │                   │                   │           │
│         ▼                   ▼                   ▼           │
│  ┌─────────────────────────────────────────────────────┐ │
│  │              OUTPUT: Ready-to-Upload MP4            │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 File Structure

```
automation/
├── automation.py          # Main orchestrator CLI
├── script_engine.py       # Viral script generator
├── tts_generator.py       # ElevenLabs API integration
├── renderer.py            # MoviePy video compositor
├── requirements.txt       # Python dependencies
└── outputs/               # Generated content
    ├── projects/          # Script packages
    └── final/             # Rendered MP4s

assets/
├── gameplay/              # Subway Surfers, Minecraft footage
├── sfx/                   # Button pop, whoosh sounds
└── fonts/                 # Custom fonts (optional)

projects/                  # Individual video packages
└── 2026-02-20_caught_wife/
    ├── script.json        # Structured script data
    ├── script.txt         # Human-readable script
    └── VIDEO_PACKAGE.md   # Full production spec

exports/                   # Final TikTok-ready videos
logs/                      # Performance tracking
```

---

## 🚀 Quick Start

### Step 1: Install Dependencies

```bash
cd automation
pip install -r requirements.txt
```

**Required packages:**
- `moviepy` - Video editing engine
- `elevenlabs` - TTS API client
- `pillow` - Image/text rendering
- `pydub` - Audio processing

### Step 2: Add API Key

Get your ElevenLabs API key:
1. Go to https://elevenlabs.io
2. Sign up (free tier: 10K chars/month)
3. Copy API key from dashboard

Set environment variable:
```bash
# Windows
set ELEVENLABS_API_KEY=your_key_here

# Mac/Linux
export ELEVENLABS_API_KEY=your_key_here
```

### Step 3: Add Gameplay Footage

Download Subway Surfers gameplay:
1. YouTube search: "Subway Surfers no copyright gameplay"
2. Download with 4K Video Downloader or yt-dlp
3. Save to: `assets/gameplay/subway_surfers_001.mp4`

### Step 4: Generate Videos

**Generate 3 scripts only:**
```bash
python automation.py --scripts 3
```

**Generate 1 complete package with TTS:**
```bash
python automation.py --full 1
```

**Check system status:**
```bash
python automation.py --status
```

---

## 🎬 Usage Examples

### Example 1: Generate Daily Batch

```bash
# Generate 3 videos for tomorrow
python automation.py --full 3

# Output:
# 🎬 TikTok Automation System initialized
# 📝 Generating 3 scripts...
# Video 1: My wife was living a double life
# Video 2: I caught my husband with his 'sister'
# Video 3: The DNA test destroyed my engagement
# 🎙️  Generating TTS...
# ✅ Generated 3 complete packages in automation/outputs/projects/
```

### Example 2: Review and Select

```bash
# Generate 10 hooks, pick best
python -c "
from automation.script_engine import ViralScriptEngine
engine = ViralScriptEngine()
hooks = engine.generate_hooks(count=10)
for i, h in enumerate(hooks, 1):
    print(f'{i}. {h}')
"
```

### Example 3: Custom Script

```python
from automation.script_engine import ViralScriptEngine

engine = ViralScriptEngine()

# Generate specific category
hooks = engine.generate_hooks(category='discovery_moment', count=5)
best_hook, score = engine.select_best_hook(hooks)

# Generate full script
script = engine.generate_script(best_hook)

# Save package
package_dir = engine.save_package(script)
print(f"Ready for production: {package_dir}")
```

---

## 🔧 Configuration

### Environment Variables

```bash
# Required
ELEVENLABS_API_KEY=your_key_here

# Optional
ELEVENLABS_VOICE=josh          # Default voice
TTS_SPEED=1.10                 # Default speed
OUTPUT_DIR=automation/outputs    # Output location
```

### Customization

**Change voice:**
Edit `automation/tts_generator.py`:
```python
VOICES = {
    'josh': 'TxGEqnHWrfWFTfGW9XjX',  # Male, 30s
    'bella': 'EXAVITQu4vr4xnSDxMaL',  # Female, young
    # Add more...
}
```

**Change caption style:**
Edit `automation/renderer.py`:
```python
CAPTION_FONT_SIZE = 60  # Larger
CAPTION_COLOR = (255, 255, 0)  # Yellow
HOOK_COLOR = (255, 0, 0)  # Red
```

---

## 📊 Performance Targets

Based on BluePrint v1.0 research:

| Metric | Target | Measurement |
|--------|--------|-------------|
| 3-Second Retention | >70% | Hook effectiveness |
| Watch Time | >55% | Story engagement |
| Likes | 6-8% | Content quality |
| Comments | 2-3% | Controversy/cliffhanger |
| Production Time | <5 min | Automation efficiency |

---

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'moviepy'`
**Fix:** `pip install moviepy`

### Issue: `FFmpeg not found`
**Fix:** 
1. Download FFmpeg from https://ffmpeg.org/download.html
2. Add to PATH
3. Or: `pip install imageio[ffmpeg]`

### Issue: `ELEVENLABS_API_KEY not set`
**Fix:**
```bash
set ELEVENLABS_API_KEY=your_key_here
```

### Issue: `No gameplay footage found`
**Fix:** Download Subway Surfers gameplay and save to `assets/gameplay/`

---

## 🚀 Roadmap

### Phase 1: MVP (COMPLETE ✅)
- ✅ Script generation
- ✅ TTS integration
- ✅ Video rendering
- ✅ CLI interface

### Phase 2: Smart Features (Next)
- [ ] Reddit API integration (auto-fetch stories)
- [ ] Word-level caption timing (AssemblyAI)
- [ ] Pattern interrupt automation (zooms, cuts)
- [ ] Thumbnail generation
- [ ] Batch processing (5 videos at once)

### Phase 3: Full Autonomy (Future)
- [ ] Auto-schedule TikTok posts
- [ ] Performance tracking integration
- [ ] A/B test automation
- [ ] Self-improving hooks based on metrics

---

## 💡 Pro Tips

1. **Start small:** Generate 1 script, review it, then scale
2. **Test TTS:** Try different voices (Josh, Adam, Antoni)
3. **Gameplay matters:** Satisfying gameplay = better retention
4. **Hook is everything:** Spend time picking the best of 10
5. **Iterate fast:** Post, measure, adjust, repeat

---

## 📞 Support

**Documentation:**
- `VIRAL_FORMAT_BLUEPRINT.md` - Research and specs
- `logs/SOP_Current.md` - Manual editing guide
- `projects/*/VIDEO_PACKAGE.md` - Individual video specs

**Commands:**
```bash
python automation.py --status      # Check everything
python automation.py --scripts 5     # Generate 5 scripts
python automation.py --full 3        # Generate 3 complete packages
```

---

**Built with ❤️ by Aneko (ViralOps)**  
**For Fields' TikTok Empire** 🐾🔥

*Last updated: Feb 20, 2026*
