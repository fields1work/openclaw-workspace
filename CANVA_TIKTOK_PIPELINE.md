# 🎬 CANVA TIKTOK AUTOMATION PIPELINE
*Semi-automated Reddit-style video production system*
**Engineer:** Aneko | **Operator:** Fields | **Platform:** Canva Video

---

## 🎯 SYSTEM OVERVIEW

**Goal:** Produce 1 TikTok video in 10-15 minutes (down from 45+ min manual editing)
**Method:** Browser automation + repeatable Canva templates
**Output:** 1080x1920 MP4, 45-75 seconds, optimized for retention

---

## 📐 TEMPLATE STRUCTURE — "Reddit Drama Standard"

### Base Template Name: `TIKTOK_REDDIT_V1_MASTER`

**Canvas Settings:**
- **Dimensions:** 1080 x 1920 pixels (9:16 vertical)
- **Duration:** 60 seconds (adjustable per script)
- **Background:** Subtle animated gradient OR dark mode (#1a1a2e)

---

## 🎨 DESIGN SPECIFICATIONS

### 1. TYPOGRAPHY SYSTEM

**Hook Text (First 3 seconds):**
- **Font:** League Spartan (Bold, 72pt)
- **Color:** #ff6b35 (Orange — brand match) OR white with orange glow
- **Animation:** "Typewriter" or "Pop" — fast, punchy
- **Position:** Center, upper 1/3 of screen
- **Effect:** Slight drop shadow for readability

**Body/Caption Text:**
- **Font:** Inter (Medium, 36-48pt depending on length)
- **Color:** #ffffff (white)
- **Animation:** "Fade up" or "Slide from bottom"
- **Position:** Lower 2/3, centered
- **Line length:** Max 8 words per line (easy reading)

**Subtle Accent Text (optional):**
- **Font:** Inter (Light, 24pt)
- **Color:** #aaaaaa (muted gray)
- **Use for:** Timestamps, "Part 1/3", usernames

### 2. BACKGROUND VIDEO LAYER

**Type:** Stock looping footage (no sound)
- **Option A:** Subtle office/workspace B-roll (typing, coffee, papers)
- **Option B:** Abstract dark gradient animation
- **Option C:** Bedroom/night scene (relatable for drama stories)
- **Option D:** "Subway surfers" style gameplay (if using that retention hack)

**Settings:**
- **Opacity:** 40-60% (text must be readable)
- **Blur:** 0-2px (subtle, not distracting)
- **Speed:** Normal or 0.8x (slightly slow = more loops)

### 3. AUDIO LAYER

**Voiceover:**
- **Format:** MP3 from ElevenLabs
- **Volume:** 100%
- **Position:** Full duration of video

**Background Music:**
- **Type:** Lo-fi or subtle drama underscore
- **Volume:** 15-20% (must not compete with voice)
- **Canva search:** "lofi", "ambient", "subtle"

### 4. HOOK ARCHITECTURE (Critical — First 3 Seconds)

**Scroll-Stopper Formats:**

| Hook Type | Text Example | Animation |
|-----------|--------------|-----------|
| **Question** | "AITA for telling my boss the truth?" | Typewriter fast |
| **Number** | "3 red flags I ignored (big mistake)" | Pop + bounce |
| **Story** | "My sister's BF hit on me at the wedding" | Fade in dramatic |
| **Curiosity** | "I found out why they really fired me" | Reveal left-to-right |

**Visual Hook Element:**
- Add subtle animated border glow (orange #ff6b35)
- OR add small emoji in corner (💀, 😱, 🚩)
- OR add "PART 1" badge in top corner

---

## 🤖 AUTOMATION STEPS — PLAYWRIGHT ACTIONS

### PHASE 1: Setup (One-time)

```
1. Open Chrome/Edge
2. Navigate to: https://www.canva.com/video/
3. Login with Fields' credentials ( Fields must do this once )
4. Create base template "TIKTOK_REDDIT_V1_MASTER"
5. Save template to "Your Projects" folder
```

### PHASE 2: Production (Per Video — Repeatable)

```
AUTOMATION SEQUENCE:

STEP 1: Open Template
- URL: https://www.canva.com/design/XXX/edit (template URL)
- Action: Click "Use template" or "Duplicate"
- Wait: 3 seconds for load

STEP 2: Rename Project
- Click: Title at top
- Clear: Current name
- Type: "TT_[SCRIPT_NAME]_[DATE]" (e.g., "TT_BOSS_AFFAIR_0220")
- Press: Enter

STEP 3: Edit Hook Text
- Click: Hook text element (first 3 sec)
- Triple-click: Select all text
- Type: New hook (from script)
- Click: Outside to deselect

STEP 4: Edit Body Text Blocks
- Click: First body text element
- Triple-click: Select all
- Type: Script part 1
- Repeat for each text block (usually 3-4 blocks per 60s video)

STEP 5: Insert Voiceover
- Click: "Uploads" (left sidebar)
- Click: "Upload files"
- Select: MP3 from `content/voiceovers/`
- Wait: Upload complete (5-10 sec)
- Drag: MP3 to timeline (bottom)
- Align: Voiceover starts at 0:00

STEP 6: Adjust Timing
- Click: First text element
- Drag: Right edge to match voiceover timing
- Match: Each text block to corresponding audio segment
- Shortcut: Use "Show timings" feature

STEP 7: Preview & Export
- Click: Play button (preview)
- Check: Audio sync, text readability
- Click: "Share" → "Download"
- Format: MP4 Video
- Quality: 1080p (Recommended)
- Click: "Download"
- Wait: 30-60 seconds processing
- Save: To `content/videos/`
```

---

## 📦 REQUIRED ASSETS CHECKLIST

### Pre-staged in Canva (Upload once, use forever):

- [ ] **Logo/Watermark:** FieldsBuildsAI logo (PNG, bottom corner)
- [ ] **Profile Pic:** For end screen (circular crop)
- [ ] **Background Videos:** 5-10 stock clips (office, bedroom, abstract)
- [ ] **Music Tracks:** 3-4 lo-fi background songs (15-20% volume)

### Per Video (Dynamic):

- [ ] **Script text:** Broken into 3-4 segments
- [ ] **Voiceover MP3:** From ElevenLabs
- [ ] **Hook:** Scroll-stopper first 3 seconds
- [ ] **Thumbnail:** SVG/PNG from `content/thumbnails/`

---

## ⚡ OPTIMIZATION NOTES

### Speed Hacks:

1. **Template Duplication:** Never start from scratch — always duplicate
2. **Keyboard Shortcuts:**
   - `Ctrl+D` = Duplicate element
   - `Ctrl+Z` = Undo
   - `Space` = Play/pause preview
3. **Batch Uploads:** Upload all voiceovers at once, use as needed
4. **Preset Animations:** Save "favorite" animations to brand kit

### Retention Optimization:

| Timestamp | Optimization |
|-----------|--------------|
| **0:00-0:03** | HOOK — Biggest text, highest contrast |
| **0:03-0:15** | Fast cuts, 2-3 text blocks, keep momentum |
| **0:15-0:30** | Story buildup, slower pace |
| **0:30-0:45** | Climax/twist reveal |
| **0:45-0:60** | Resolution + CTA ("Follow for Part 2") |

### Canva Pro Features (Use if available):

- ✅ **Brand Kit:** Save fonts, colors, logos
- ✅ **Resize Magic:** Auto-adjust to 9:16
- ✅ **Background Remover:** For profile pics
- ✅ **Premium Stock:** Higher quality footage

---

## 🎓 QUICK-START WORKFLOW (For Fields)

**Each Video = 10-15 Minutes:**

```
MINUTE 1: Open Canva, duplicate template
MINUTE 2-3: Paste hook text, format
MINUTE 4-6: Paste body script (3-4 text blocks)
MINUTE 7: Upload voiceover, add to timeline
MINUTE 8-9: Sync text timing to voice
MINUTE 10: Preview, adjust, export
MINUTE 11-15: Upload to TikTok, write caption, post
```

**With Aneko's prep:**
- I write the script ✍️
- I generate the voiceover 🎙️
- I design the thumbnail 🎨
- You: 10 min in Canva + post 🚀

---

## 🔗 NEXT STEPS

1. **Fields:** Login to Canva Video, create base template
2. **Aneko:** Write 5 scripts optimized for this template
3. **Fields:** Record screen of one video creation (for automation notes)
4. **Together:** Refine timing, test 3 videos, optimize

**Goal:** 3 videos this week → 1 video/day by Week 2

---

*Built with ☕ by Aneko 🐾 for Fields*  
*Template Version: 1.0 | Date: 2026-02-19*
