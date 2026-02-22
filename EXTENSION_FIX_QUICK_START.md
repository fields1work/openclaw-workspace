# EXTENSION_FIX_QUICK_START.md
## 🚀 Browser Extension Fix — Quick Mobile Reference

---

## WHAT WAS BROKEN
The Chrome extension couldn't connect because OpenClaw v2026.2.14 added authentication that the extension didn't have.

---

## ✅ FIX COMPLETE — DO THIS NOW

### Step 1: Reload Extension
1. Open Chrome on your computer
2. Go to: `chrome://extensions`
3. Find "OpenClaw Browser Relay"
4. Click **"Reload"** button

### Step 2: Add Your Token
1. Click the extension icon (orange claw)
2. Click "Options"
3. **Port:** `18792` (leave default)
4. **Token:** `JoshOpenClawToken_839271_ABCxyz`
5. Click **"Save"**
6. Should show: ✅ "Relay reachable and authenticated"

### Step 3: Test It
1. Open any website
2. Click the extension icon on that tab
3. Badge shows **"ON"** (orange)
4. Done! I can now control the browser

---

## IF IT DOESN'T WORK

| Problem | Fix |
|---------|-----|
| "401 Unauthorized" | Check token is correct: `JoshOpenClawToken_839271_ABCxyz` |
| "Relay not reachable" | Run: `openclaw gateway start` in terminal |
| Extension not showing | Go to `chrome://extensions` → Enable "Developer mode" → "Load unpacked" → Select `~\.openclaw\browser\chrome-extension` |

---

## VERIFICATION COMMAND
Once attached, I'll test with:
```
browser action=snapshot profile=chrome
```

---

**That's it! 3 steps and you'll have full browser control.** 🐾