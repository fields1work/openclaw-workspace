# 📋 SOP v1.0 - REDDIT STORY TIKTOK PRODUCTION
**Standard Operating Procedure | CapCut Desktop**
**Last Updated:** Feb 20, 2026 | **BluePrint Version:** 1.0

---

## 🎯 PURPOSE
Convert Reddit story + gameplay footage into viral TikTok video in 15-20 minutes.

---

## 📁 PRE-PRODUCTION CHECKLIST

### Files Required:
- [ ] Gameplay video (Subway Surfers or Minecraft, 2-3min, MP4)
- [ ] Reddit story script (formatted per Script Engine)
- [ ] TTS audio file (MP3/WAV, generated from script)
- [ ] SFX files (optional: button pop, whoosh)

### Assets Location:
```
workspace/
├── assets/
│   ├── gameplay/
│   │   └── subway_surfers_001.mp4
│   ├── sfx/
│   │   ├── button_pop.wav
│   │   └── whoosh.wav
│   └── fonts/
│       └── (CapCut built-in fonts used)
├── projects/
│   └── 2026-02-20_caught_partner/
├── exports/
│   └── (final MP4 output)
└── logs/
    └── optimization_log.md
```

---

## 🎬 CAPCUT EDITING RECIPE (Exact Steps)

### PHASE 1: PROJECT SETUP (2 min)

**Step 1.1: Create Project**
1. Open CapCut Desktop
2. Click **"New Project"**
3. Set **Aspect Ratio: 9:16** (vertical)
4. Click **"Create"**

**Step 1.2: Import Assets**
1. Click **"Import"** button
2. Select your gameplay video file
3. Select your TTS audio file
4. (Optional) Import SFX files

**Step 1.3: Add to Timeline**
1. Drag gameplay video to **Video Track (V1)**
2. Drag TTS audio to **Audio Track (A1)**
3. Trim gameplay to match TTS length + 2 seconds buffer

---

### PHASE 2: GAMEPLAY SETUP (3 min)

**Step 2.1: Position Gameplay**
1. Click gameplay clip on timeline
2. In Preview window, ensure gameplay fills frame
3. If needed: Click **"Transform"** → adjust scale/position
4. **Critical:** Leave lower third clear for captions

**Step 2.2: Trim to Match Audio**
1. Play timeline to verify sync
2. Trim gameplay end to match TTS end (±1s)
3. Cut tool: **Ctrl/Cmd + B** or click scissors icon
4. Delete excess footage

---

### PHASE 3: ADD HOOK TEXT (3 min)

**Step 3.1: Create Hook Text**
1. Click **"Text"** in left panel
2. Click **"Add Text"**
3. Type your hook (max 8 words)
4. Position at **0:00** on timeline

**Step 3.2: Style the Hook**
1. With text selected, click **"Style"** panel
2. **Font:** Montserrat Bold (or Arial Bold)
3. **Size:** 64-72pt
4. **Color:** Orange (#FF6B35)
5. **Stroke:** ON, Black, 5pt thickness
6. **Shadow:** OFF
7. **Position:** Center screen (not lower third — this is the HOOK)

**Step 3.3: Set Duration**
1. Drag text clip edges on timeline
2. **Duration: Exactly 3.0 seconds**
3. No fade in/out (cut only)

---

### PHASE 4: ADD BODY CAPTIONS (6 min)

**Step 4.1: Create Caption Template**
1. Click **"Text"** → **"Add Text"**
2. Type first caption chunk (max 10 words)
3. Start at 0:03 (after hook ends)

**Step 4.2: Style Caption**
1. **Font:** Montserrat Bold
2. **Size:** 54-60pt
3. **Color:** White (#FFFFFF)
4. **Stroke:** ON, Black, 4pt thickness
5. **Position:** Lower third, centered
   - X: 50% (center)
   - Y: 75-80% (lower third)

**Step 4.3: Sync to TTS**
1. Play audio, pause at exact word timing
2. Position caption start at that timestamp
3. Duration: Until next caption starts (no gaps)

**Step 4.4: Duplicate for Next Captions**
1. Select caption layer
2. **Ctrl/Cmd + C** then **Ctrl/Cmd + V**
3. Move to next timing position
4. Edit text for next chunk
5. Repeat until TTS is fully captioned

**Caption Chunking Rules:**
- Max 10 words per caption
- Break at natural pauses
- One sentence = 1-2 captions max
- Sync timing tight to speech

---

### PHASE 5: PATTERN INTERRUPTS (3 min)

**Step 5.1: Identify Interrupt Points**
Mark timestamps every 5-7 seconds for visual pulse:
- 0:08s, 0:15s, 0:22s, 0:29s, 0:36s...

**Step 5.2: Add Micro Zoom**
1. At interrupt timestamp, split gameplay clip (**Ctrl/Cmd + B**)
2. Select the 1-second segment
3. Click **"Transform"** → **"Scale"**
4. Add keyframe at start: 100%
5. Add keyframe at middle: 105%
6. Add keyframe at end: 100%
7. Result: Subtle 1-second zoom pulse

**Step 5.3: Quick Cut (Alternative)**
1. Split gameplay at interrupt point
2. Replace second half with different gameplay segment
3. Match action/flow for seamless cut

---

### PHASE 6: CTA / CLIFFHANGER (2 min)

**Step 6.1: Add End Text**
1. At story conclusion (10s before end), add text
2. **Text:** "Part 2 at 100 followers!" or "Should I expose them?"
3. **Style:** Yellow or Orange, 48pt, center screen
4. **Duration:** 3-5 seconds

**Step 6.2: (Optional) Add Top Bar**
1. Add text at top of screen: "r/AmItheAsshole" or "Reddit Story"
2. **Style:** White, 36pt, semi-transparent black background
3. **Position:** Top center (Y: 10%)
4. **Duration:** Entire video

---

### PHASE 7: AUDIO FINALIZATION (1 min)

**Step 7.1: Adjust TTS Volume**
1. Click TTS audio track
2. **Volume:** 85-90%

**Step 7.2: Add SFX (Optional)**
1. Drag SFX to timeline at key moments
2. **Volume:** 40-50%
3. Position: Hook reveal, twist moment

**Step 7.3: Gameplay Audio**
1. If gameplay has audio: **Volume: 8-12%**
2. OR mute gameplay audio completely
3. Background gameplay should be barely perceptible

---

### PHASE 8: FINAL QA CHECK (2 min)

**Visual Check:**
- [ ] Hook appears instantly at 0:00 (no fade)
- [ ] Hook is ORANGE and center screen
- [ ] Captions are WHITE, lower third
- [ ] No caption exceeds 2 lines
- [ ] Gameplay fills frame but doesn't obstruct text
- [ ] Pattern interrupts visible but not jarring

**Audio Check:**
- [ ] TTS is clear and synchronized with captions
- [ ] No silent gaps > 0.15s
- [ ] Total length 45-75 seconds

**Play Through:**
- Watch entire video once
- Note any typos, sync issues, or dead air
- Fix immediately

---

## 📤 EXPORT SETTINGS (Exact)

**Step 8.1: Open Export Panel**
1. Click **"Export"** button (top right)

**Step 8.2: Configure Video**
- **Resolution:** 1080x1920
- **FPS:** 30
- **Bitrate:** High (CapCut's high = ~10-12 Mbps)
- **Codec:** H.264
- **Format:** MP4

**Step 8.3: Configure Audio**
- **Codec:** AAC
- **Bitrate:** 192kbps (or highest available)

**Step 8.4: Export**
1. Click **"Export"**
2. Save to: `/exports/YYYYMMDD_storyname.mp4`
3. Wait for full render

---

## ✅ POST-EXPORT QA

**Verify File:**
- [ ] Plays smoothly in media player
- [ ] Audio synced correctly
- [ ] Text appears sharp (not pixelated)
- [ ] File size 30-60MB
- [ ] Duration matches target (45-75s)

**Transfer to Phone:**
1. AirDrop (Mac/iPhone)
2. USB cable + file transfer
3. Cloud storage (Google Drive, Dropbox)
4. **Critical:** Do NOT compress during transfer

---

## 📱 TIKTOK UPLOAD

**Step 9.1: Mobile Upload**
1. Open TikTok app on phone
2. Tap **+** → **Upload**
3. Select exported video from gallery

**Step 9.2: Add Caption**
```
I scammed my scammer back

Part 2 if this hits 1K likes 👀

#redditstories #reddit #storytime #viral #fyp #aita
```

**Step 9.3: Settings**
- Enable "High Quality Uploads" (in TikTok settings, if available)
- Allow Stitch/Duet (increases reach)
- Disable downloads (optional, for exclusivity)

**Step 9.4: Post**
- Tap **"Post"**
- Do NOT delete from drafts until confirmed live

---

## 🔄 BATCH WORKFLOW

**For Multiple Videos:**
1. Complete Video 001 export
2. Save project as template: **"Reddit_Template_v1"**
3. For Video 002: Duplicate project, replace assets
4. Same process, faster execution (muscle memory)

**Target:** 3-4 videos per 60-minute session

---

## 🆘 TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Text blurry after export | Export at HIGH bitrate, ensure 30fps, upload from gallery |
| TTS out of sync | Re-import audio, check gameplay framerate |
| Export fails | Close other apps, free up storage, lower preview quality |
| Video too long | Trim gameplay or tighten script |
| Gameplay too distracting | Mute game audio, reduce opacity to 85% |
| Caption timing off | Split captions into smaller chunks |

---

## 📊 SUCCESS METRICS

**Time Targets:**
- First video: 20-25 minutes
- After 5 videos: 15 minutes
- After 10 videos: 12 minutes

**Quality Targets:**
- 3-second retention: >70%
- Watch time: >50%
- Comments: 1-2% of views

---

**END OF SOP v1.0**

*Execute without deviation. Measure results. Iterate.*
