# 🎬 Python TikTok Video Generator

**Fully automated Reddit-style video production**  
**Status:** Framework complete, full generation ready after dependencies installed

---

## 🚀 QUICK START

### 1. Install Dependencies

```bash
# Install Python packages
pip install -r requirements.txt

# Install ffmpeg (required for video processing)
# Windows (with chocolatey):
choco install ffmpeg

# Mac:
brew install ffmpeg

# Linux:
sudo apt-get install ffmpeg
```

### 2. Download Gameplay Footage

Download 60-second gameplay video (no copyright):
- **Subway Surfers:** YouTube search "subway surfers gameplay no copyright 60 seconds"
- **GTA Driving:** YouTube search "gta driving gameplay no copyright"
- **Minecraft Parkour:** YouTube search "minecraft parkour no copyright"

Save to: `content/gameplay/subway_surfers.mp4`

### 3. Generate Voiceover

Option A: **ElevenLabs (Recommended)**
- Use script from `VIRAL_TEST_SCRIPT_001.md`
- Voice: "Adam" or "Josh"
- Export MP3
- Save to: `content/voiceovers/voiceover_girlfriend_sister.mp3`

Option B: **System TTS (Free)**
- Script will auto-generate placeholder

### 4. Generate Video

```bash
python tiktok_video_generator.py
```

**Output:** `content/videos/auto_generated/viral_girlfriend_sister_v1.mp4`

---

## 📁 File Structure

```
content/
├── gameplay/
│   └── subway_surfers.mp4        # Download this
├── voiceovers/
│   └── voiceover_girlfriend_sister.mp3  # Generate this
├── videos/
│   └── auto_generated/
│       └── viral_girlfriend_sister_v1.mp4  # Output
└── scripts/
    └── VIRAL_TEST_SCRIPT_001.md  # Source script
```

---

## 🎨 Customization

### Change Gameplay Type

Edit the script data in `tiktok_video_generator.py`:

```python
"gameplay_type": "gta_driving"  # or "minecraft_parkour"
```

### Change Caption Style

```python
# In generate_video() method:
if style == 'hook':
    fontsize = 70  # Bigger!
    color = '#ff0000'  # Red instead of orange
```

### Add New Scripts

1. Create new script function (copy `create_viral_script_girlfriend_sister()`)
2. Change title, scenes, captions
3. Call in `main()`

---

## 📊 Video Specs

| Spec | Value |
|------|-------|
| **Resolution** | 1080x1920 (9:16 vertical) |
| **Duration** | 60 seconds |
| **FPS** | 30 |
| **Format** | MP4 (H.264) |
| **Audio** | AAC |

---

## 🎯 What The Script Does

1. ✅ Loads 60-second gameplay footage
2. ✅ Adds voiceover audio track
3. ✅ Creates captions for each scene
4. ✅ Applies styling (hook = big orange, body = white, cliffhanger = dramatic)
5. ✅ Adds end card with CTA
6. ✅ Exports MP4 ready for TikTok

---

## 🔥 Next Features (Coming)

- [ ] Auto-download gameplay from YouTube
- [ ] ElevenLabs API integration (auto voiceover)
- [ ] Multiple video batch generation
- [ ] Auto-upload to TikTok (API)
- [ ] Thumbnail auto-generation

---

**Built with 🐍 by Aneko**  
**Figure It Out Mode: ENGAGED** 💪
