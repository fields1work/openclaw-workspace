@echo off
REM TikTok Automation Quick Start for Windows
REM Fields Build System - ViralOps

echo ==========================================
echo  TikTok Reddit Story Automation System
echo  ViralOps v1.0
echo ==========================================
echo.

REM Check if Python is installed
python --version > nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found!
    echo    Install Python from: https://python.org/downloads
    pause
    exit /b 1
)

echo ✅ Python found

REM Check if in automation directory
if not exist "automation.py" (
    echo ❌ Not in automation directory!
    echo    Please run from: workspace/automation/
    pause
    exit /b 1
)

REM Check for API key
if "%ELEVENLABS_API_KEY%"=="" (
    echo ⚠️  ELEVENLABS_API_KEY not set!
    echo    Get key at: https://elevenlabs.io
    echo    Then run: set ELEVENLABS_API_KEY=your_key
    echo.
    echo    Continuing in script-only mode (no TTS)...
    echo.
)

:menu
echo ==========================================
echo  MAIN MENU
echo ==========================================
echo.
echo  1. Check System Status
echo  2. Generate 3 Scripts Only
echo  3. Generate 1 Complete Package (with TTS)
echo  4. Generate 5 Scripts (Batch)
echo  5. View Generated Projects
echo  6. Open Documentation
echo  7. Exit
echo.
set /p choice="Enter choice (1-7): "

if "%choice%"=="1" goto status
if "%choice%"=="2" goto scripts3
if "%choice%"=="3" goto full1
if "%choice%"=="4" goto scripts5
if "%choice%"=="5" goto view
if "%choice%"=="6" goto docs
if "%choice%"=="7" goto end
goto menu

:status
echo.
echo Checking system status...
python automation.py --status
echo.
pause
goto menu

:scripts3
echo.
echo Generating 3 viral scripts...
python automation.py --scripts 3
echo.
echo ✅ Scripts saved to: automation/outputs/projects/
pause
goto menu

:full1
echo.
if "%ELEVENLABS_API_KEY%"=="" (
    echo ❌ Cannot generate TTS without API key!
    echo    Set ELEVENLABS_API_KEY first.
    pause
    goto menu
)
echo Generating 1 complete package (script + TTS)...
python automation.py --full 1
echo.
echo ✅ Package saved to: automation/outputs/projects/
pause
goto menu

:scripts5
echo.
echo Generating 5 viral scripts (batch mode)...
python automation.py --scripts 5
echo.
echo ✅ Scripts saved to: automation/outputs/projects/
pause
goto menu

:view
echo.
echo Opening projects folder...
start automation\outputs\projects
pause
goto menu

:docs
echo.
echo Opening documentation...
start automation\README.md
pause
goto menu

:end
echo.
echo ==========================================
echo  Thanks for using ViralOps Automation!
echo  Built by Aneko for Fields 🐾
echo ==========================================
echo.
pause
exit /b 0
