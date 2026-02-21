"""
TikTok Reddit Story Automation System
Main orchestrator - runs the entire pipeline.

Fields Build System - MVP Phase 1
"""

import argparse
import sys
from pathlib import Path

# Add automation folder to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from script_engine import ViralScriptEngine
    from tts_generator import ElevenLabsTTS
except ImportError as e:
    print(f"⚠️  Import error: {e}")
    print("Run: pip install -r requirements.txt")
    sys.exit(1)


class TikTokAutomation:
    """
    Full automation pipeline for Reddit Story TikTok videos.
    
    Phases:
    1. Generate viral script
    2. Generate TTS audio (requires API key)
    3. Render video (requires gameplay footage)
    4. Output ready-to-upload MP4
    """
    
    def __init__(self, output_dir: str = "automation/outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True, parents=True)
        
        self.script_engine = ViralScriptEngine(output_dir=str(output_dir / "projects"))
        self.tts_generator = ElevenLabsTTS()
        
        print("🚀 TikTok Automation System initialized")
        print(f"   Output: {self.output_dir.absolute()}")
    
    def generate_only(self, count: int = 3):
        """Phase 1: Generate scripts only (no API calls needed)."""
        print(f"\n📝 Generating {count} scripts...\n")
        
        packages = []
        for i in range(count):
            hooks = self.script_engine.generate_hooks(count=10)
            best_hook, score = self.script_engine.select_best_hook(hooks)
            
            print(f"Video {i+1}: {best_hook}")
            
            script = self.script_engine.generate_script(best_hook)
            package_dir = self.script_engine.save_package(script)
            packages.append(package_dir)
        
        print(f"\n✅ Generated {len(packages)} script packages")
        print(f"   Location: {self.output_dir / 'projects'}")
        print("\nNext steps:")
        print("  1. Review scripts in projects/<video_id>/script.txt")
        print("  2. Run: python automation.py --tts <video_id>")
        
        return packages
    
    def generate_with_tts(self, count: int = 1):
        """Phase 2: Generate script + TTS audio."""
        if not self.tts_generator.api_key:
            print("\n❌ ELEVENLABS_API_KEY not set")
            print("   Get key at: https://elevenlabs.io")
            print("   Then: set ELEVENLABS_API_KEY=your_key")
            return
        
        packages = self.generate_only(count=count)
        
        print(f"\n🎙️  Generating TTS for {len(packages)} videos...\n")
        
        for package_dir in packages:
            # Load script
            import json
            with open(package_dir / "script.json") as f:
                script_data = json.load(f)
            
            # Convert to TTS format
            tts_input = {
                'hook': script_data['hook'],
                'body_lines': (
                    script_data['context'] + 
                    [e['text'] for e in script_data['escalation']]
                ),
                'cliffhanger': script_data['cliffhanger']
            }
            
            # Generate audio
            try:
                audio_path = self.tts_generator.generate_script_audio(
                    tts_input,
                    output_dir=str(package_dir)
                )
                print(f"   ✅ Audio: {audio_path}")
            except Exception as e:
                print(f"   ❌ Failed: {e}")
    
    def check_status(self):
        """Check system status."""
        print("\n📊 System Status:\n")
        
        # Check requirements
        print("Dependencies:")
        deps = ['moviepy', 'elevenlabs', 'pillow']
        for dep in deps:
            try:
                __import__(dep)
                print(f"  ✅ {dep}")
            except ImportError:
                print(f"  ❌ {dep} - Run: pip install {dep}")
        
        print()
        
        # Check API keys
        print("API Keys:")
        if self.tts_generator.api_key:
            print(f"  ✅ ELEVENLABS_API_KEY (ends with ...{self.tts_generator.api_key[-4:]})")
        else:
            print("  ❌ ELEVENLABS_API_KEY not set")
        
        print()
        
        # Check folders
        print("Folder Structure:")
        folders = ['automation/outputs', 'automation/projects', 'assets/gameplay']
        for folder in folders:
            path = Path(folder)
            if path.exists():
                print(f"  ✅ {folder}")
            else:
                print(f"  ❌ {folder} - Missing")


def main():
    parser = argparse.ArgumentParser(
        description='TikTok Reddit Story Automation'
    )
    parser.add_argument('--scripts', type=int, default=0,
                       help='Generate N scripts only')
    parser.add_argument('--full', type=int, default=0,
                       help='Generate N complete packages with TTS')
    parser.add_argument('--status', action='store_true',
                       help='Check system status')
    parser.add_argument('--tts', help='Generate TTS for specific video ID')
    
    args = parser.parse_args()
    
    automation = TikTokAutomation()
    
    if args.status:
        automation.check_status()
    elif args.scripts > 0:
        automation.generate_only(count=args.scripts)
    elif args.full > 0:
        automation.generate_with_tts(count=args.full)
    else:
        print("\n🎬 TikTok Reddit Story Automation")
        print("\nCommands:")
        print("  python automation.py --scripts 3      # Generate 3 scripts")
        print("  python automation.py --full 1         # Generate 1 complete package")
        print("  python automation.py --status         # Check system")
        print("\nWorkflow:")
        print("  1. Review generated scripts")
        print("  2. Add gameplay footage to assets/gameplay/")
        print("  3. Set ELEVENLABS_API_KEY")
        print("  4. Run --full to generate video packages")


if __name__ == "__main__":
    main()
