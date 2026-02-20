# Quick ffmpeg fix - Run this in PowerShell
Write-Host "🔍 Searching for ffmpeg..." -ForegroundColor Yellow

# Check common locations
$paths = @(
    "C:\ffmpeg\bin\ffmpeg.exe",
    "C:\ffmpeg\ffmpeg-6.1.1-essentials_build\bin\ffmpeg.exe",
    "C:\Program Files\ffmpeg\bin\ffmpeg.exe",
    "C:\Users\$env:USERNAME\ffmpeg\bin\ffmpeg.exe"
)

$found = $false
foreach ($path in $paths) {
    if (Test-Path $path) {
        Write-Host "✅ Found ffmpeg at: $path" -ForegroundColor Green
        $binPath = Split-Path $path -Parent
        
        # Add to PATH for current session
        $env:Path += ";$binPath"
        
        # Add to PATH permanently
        [Environment]::SetEnvironmentVariable("Path", $env:Path, "User")
        
        Write-Host "✅ Added to PATH! Restart PowerShell and test with: ffmpeg -version" -ForegroundColor Green
        $found = $true
        break
    }
}

if (-not $found) {
    Write-Host "❌ ffmpeg not found in common locations" -ForegroundColor Red
    Write-Host "Let's check where it was downloaded..." -ForegroundColor Yellow
    
    # Search for it
    $result = Get-ChildItem -Path "C:\" -Filter "ffmpeg.exe" -Recurse -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($result) {
        Write-Host "✅ Found at: $($result.FullName)" -ForegroundColor Green
        $binPath = $result.DirectoryName
        $env:Path += ";$binPath"
        [Environment]::SetEnvironmentVariable("Path", $env:Path, "User")
        Write-Host "✅ Added to PATH!" -ForegroundColor Green
    } else {
        Write-Host "❌ ffmpeg.exe not found. Let's download it properly..." -ForegroundColor Red
        Write-Host "Run: choco install ffmpeg" -ForegroundColor Cyan
    }
}