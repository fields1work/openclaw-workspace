# 🔧 FFMPEG TROUBLESHOOTING GUIDE

## Problem
ffmpeg downloaded but PowerShell can't find it (PATH issue)

## SOLUTION 1: Add ffmpeg to PATH Manually

**Step 1: Check if ffmpeg exists**
```powershell
Test-Path "C:\ffmpeg\bin\ffmpeg.exe"
```

**Step 2: If YES, add to PATH**
```powershell
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\ffmpeg\bin", "User")
```

**Step 3: Restart PowerShell, then test**
```powershell
ffmpeg -version
```

## SOLUTION 2: If ffmpeg not in C:\ffmpeg

**Find where it was extracted:**
```powershell
Get-ChildItem -Path "C:\" -Name "ffmpeg*" -Directory
```

**Then add that location's `bin` folder to PATH**

## SOLUTION 3: Quick Check Command

Run this to see if ffmpeg is anywhere:
```powershell
where.exe ffmpeg
```

Or:
```powershell
Get-Command ffmpeg
```

## SOLUTION 4: Download via Direct Link

If all else fails, use this direct installer:
```powershell
# Download and extract to known location
$url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
$output = "$env:TEMP\ffmpeg.zip"
Invoke-WebRequest -Uri $url -OutFile $output
Expand-Archive $output -DestinationPath "C:\ffmpeg" -Force

# Add to PATH
$env:Path += ";C:\ffmpeg\ffmpeg-6.1.1-essentials_build\bin"
[Environment]::SetEnvironmentVariable("Path", $env:Path, "User")
```

## VERIFICATION

After fixing, test with:
```powershell
ffmpeg -version
python "C:\Users\field\.openclaw\workspace\tiktok_video_generator.py"
```

**Expected output:**
- ✅ "ffmpeg found - video generation possible"
- ✅ "moviepy found"
- ✅ "VIDEO GENERATED: content/videos/..."

---

## QUICK WORKAROUND (If PATH issues persist)

Edit the Python script to use full path:
```python
# In tiktok_video_generator.py, add at top:
os.environ["PATH"] += ";C:\ffmpeg\bin"
```

Or specify ffmpeg path directly in moviepy config.

---

**Aneko will implement automatic PATH detection in next update!** 🐾