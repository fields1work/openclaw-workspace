"""
ElevenLabs TTS Integration
Generates viral-optimized voiceovers for Reddit stories

Fields Build System - Phase 1
"""

import os
import time
from pathlib import Path
from typing import Optional, Dict, Any

try:
    from elevenlabs import ElevenLabs, VoiceSettings
except ImportError:
    print("⚠️  elevenlabs not installed. Run: pip install elevenlabs")
    ElevenLabs = None


class ElevenLabsTTS:
    """
    TTS generator optimized for TikTok viral retention.
    
    Voice Profile (per BluePrint v1.0):
    - Voice: Josh or Adam (Male, conversational)
    - Speed: 1.10x (faster than normal, retains attention)
    - Stability: 0.50
    - Clarity: +0.30
    """
    
    # Viral-optimized settings
    DEFAULT SPEED = 1.10
    DEFAULT_STABILITY = 0.50
    DEFAULT_CLARITY = 0.30
    
    # Voice IDs from ElevenLabs
    VOICES = {
        'josh': 'TxGEqnHWrfWFTfGW9XjX',  # Male, 30s, American
        'adam': 'pNInz6obpgDQGcFmaJgB',  # Male, deep
        'bella': 'EXAVITQu4vr4xnSDxMaL',  # Female, young
        'rachel': '21m00Tcm4TlvDq8ikWAM',  # Female, mature
        'antoni': 'ErXwobaYiN019PkySvjV',  # Male, energetic
    }
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("ELEVENLABS_API_KEY")
        self.client = None
        
        if self.api_key and ElevenLabs:
            self.client = ElevenLabs(api_key=self.api_key)
            print("✅ ElevenLabs TTS initialized")
        else:
            print("⚠️  ElevenLabs not configured. Set ELEVENLABS_API_KEY")
    
    def generate_tts(self, 
                     text: str, 
                     voice_key: str = 'josh',
                     output_path: str = "tts_output.mp3",
                     speed: float = DEFAULT_SPEED,
                     stability: float = DEFAULT_STABILITY,
                     clarity: float = DEFAULT_CLARITY) -> str:
        """
        Generate TTS audio optimized for TikTok.
        
        Args:
            text: Script text to synthesize
            voice_key: Key from VOICES dict
            output_path: Where to save MP3
            speed: 1.0 = normal, 1.10 = viral sweet spot
            stability: 0.5 = balanced emotion
            clarity: 0.3 = enhanced clarity
        
        Returns:
            Path to generated audio file
        """
        if not self.client:
            raise RuntimeError("ElevenLabs not configured. Set API key.")
        
        voice_id = self.VOICES.get(voice_key, self.VOICES['josh'])
        
        print(f"🎙️  Generating TTS with voice: {voice_key}")
        print(f"   Length: {len(text)} chars")
        print(f"   Settings: speed={speed}, stability={stability}, clarity={clarity}")
        
        # ElevenLabs API call
        settings = VoiceSettings(
            stability=stability,
            similarity_boost=0.75,
            style=0.20,
            use_speaker_boost=True
        )
        
        try:
            audio = self.client.generate(
                text=text,
                voice=voice_id,
                model="eleven_turbo_v2",  # Fast, good quality
                voice_settings=settings,
                output_format="mp3_44100_192"  # High quality
            )
            
            # Save to file
            with open(output_path, 'wb') as f:
                for chunk in audio:
                    f.write(chunk)
            
            print(f"✅ TTS saved: {output_path}")
            return output_path
            
        except Exception as e:
            print(f"❌ TTS generation failed: {e}")
            raise
    
    def generate_script_audio(self, 
                               script_data: Dict[str, Any],
                               output_dir: str = "assets/tts") -> str:
        """
        Generate audio for full script with pauses.
        
        Args:
            script_data: Dict with 'hook', 'body_lines', 'cliffhanger'
            output_dir: Directory to save MP3
        
        Returns:
            Path to generated audio
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True, parents=True)
        
        # Build full text with pauses (in milliseconds)
        # BluePrint v1.0 specifications
        parts = []
        
        # Hook (3 seconds, then pause)
        parts.append(script_data['hook'])
        parts.append('<break time="300ms"/>')
        
        # Body lines
        for line in script_data['body_lines']:
            parts.append(line)
            # Vary pause based on punctuation
            if line.endswith('.'):
                parts.append('<break time="150ms"/>')
            elif line.endswith('?'):
                parts.append('<break time="250ms"/>')
            else:
                parts.append('<break time="100ms"/>')
        
        # Cliffhanger with dramatic pause
        parts.append(script_data['cliffhanger'])
        parts.append('<break time="400ms"/>')
        parts.append("Part 2 if this hits 1K likes.")
        
        full_text = " ".join(parts)
        
        # Generate filename from hook
        safe_hook = script_data['hook'].replace(' ', '_').replace('?', '').replace('!', '')[:30]
        output_file = output_dir / f"{safe_hook}_{int(time.time())}.mp3"
        
        return self.generate_tts(full_text, output_path=str(output_file))
    
    def estimate_duration(self, text: str) -> float:
        """Estimate audio duration based on word count."""
        words = len(text.split())
        # At 1.10x speed, roughly 3 words per second
        return words / 3.0 * self.DEFAULT_SPEED


def test_generation():
    """Test TTS generation."""
    tts = ElevenLabsTTS()
    
    test_script = {
        'hook': 'My wife was living a double life',
        'body_lines': [
            'I thought I knew everything about Sarah.',
            "We'd been married for three years.",
            'But six months ago, things got weird.',
        ],
        'cliffhanger': "I've been the affair partner this whole time."
    }
    
    print("\n🧪 Testing TTS generation...")
    print(f"Estimated duration: {tts.estimate_duration(' '.join(test_script['body_lines'])):.1f}s")
    print("\n(Requires ELEVENLABS_API_KEY to actually generate)")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='ElevenLabs TTS Generator')
    parser.add_argument('--text', help='Text to synthesize')
    parser.add_argument('--voice', default='josh', help='Voice to use')
    parser.add_argument('--output', default='tts_output.mp3', help='Output file')
    parser.add_argument('--test', action='store_true', help='Run test')
    
    args = parser.parse_args()
    
    if args.test:
        test_generation()
    elif args.text:
        tts = ElevenLabsTTS()
        tts.generate_tts(args.text, voice_key=args.voice, output_path=args.output)
    else:
        print("Usage:")
        print("  python tts_generator.py --test")
        print('  python tts_generator.py --text "Hello world" --voice josh')
