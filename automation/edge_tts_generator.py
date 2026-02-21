"""
Edge-TTS Integration for TikTok Automation
Replaces ElevenLabs with free Microsoft Edge TTS

Fields Build System - TTS Migration
"""

import asyncio
import edge_tts
import os
from pathlib import Path
from typing import Optional, Dict, Any, List


class EdgeTTSGenerator:
    """
    Free TTS generator using Microsoft Edge's online service.
    
    No API key required. No limits. Neural quality voices.
    
    Best voices for TikTok Reddit stories:
    - en-US-GuyNeural: Male, conversational, natural (RECOMMENDED)
    - en-US-JennyNeural: Female, clear, engaging
    - en-GB-SoniaNeural: Female, UK accent (stands out)
    - en-US-AriaNeural: Female, expressive
    """
    
    # Best voices for viral TikTok content
    RECOMMENDED_VOICES = {
        'male_conversational': 'en-US-GuyNeural',
        'female_clear': 'en-US-JennyNeural',
        'female_uk': 'en-GB-SoniaNeural',
        'female_expressive': 'en-US-AriaNeural',
        'male_deep': 'en-US-DavisNeural',
        'female_calm': 'en-US-AnaNeural',
    }
    
    # Speed settings for viral content
    SPEED_SETTINGS = {
        'normal': '+0%',      # 1.0x
        'viral': '+10%',      # 1.1x (RECOMMENDED)
        'fast': '+20%',       # 1.2x
        'ultra': '+30%',      # 1.3x
    }
    
    def __init__(self, output_dir: str = "assets/tts"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True, parents=True)
        print("✅ Edge-TTS Generator initialized (FREE - no API key needed)")
    
    async def generate_tts(
        self,
        text: str,
        output_path: str,
        voice: str = "en-US-GuyNeural",
        rate: str = "+10%",
        volume: str = "+0%",
        pitch: str = "+0Hz",
        write_subtitles: bool = True
    ) -> str:
        """
        Generate TTS audio using Microsoft Edge's free service.
        
        Args:
            text: Text to synthesize
            output_path: Output MP3 file path
            voice: Voice ID (default: en-US-GuyNeural)
            rate: Speed adjustment (+10% = 1.1x)
            volume: Volume adjustment
            pitch: Pitch adjustment
            write_subtitles: Also generate SRT file
        
        Returns:
            Path to generated MP3 file
        """
        print(f"🎙️  Generating TTS with Edge...")
        print(f"   Voice: {voice}")
        print(f"   Rate: {rate}")
        print(f"   Length: {len(text)} chars")
        
        try:
            # Generate with subtitles if requested
            if write_subtitles:
                srt_path = str(Path(output_path).with_suffix('.srt'))
                communicate = edge_tts.Communicate(text, voice, rate=rate, volume=volume, pitch=pitch)
                await communicate.save(output_path)
                
                # Generate SRT separately
                submaker = edge_tts.SubMaker()
                communicate = edge_tts.Communicate(text, voice, rate=rate, volume=volume, pitch=pitch)
                async for chunk in communicate.stream():
                    if chunk["type"] == "audio":
                        submaker.feed(chunk["data"])
                
                with open(srt_path, 'w', encoding='utf-8') as f:
                    f.write(submaker.get_srt())
                
                print(f"✅ TTS saved: {output_path}")
                print(f"✅ Subtitles saved: {srt_path}")
            else:
                communicate = edge_tts.Communicate(text, voice, rate=rate, volume=volume, pitch=pitch)
                await communicate.save(output_path)
                print(f"✅ TTS saved: {output_path}")
            
            return output_path
            
        except Exception as e:
            print(f"❌ TTS generation failed: {e}")
            raise
    
    def generate_script_audio(
        self,
        script_data: Dict[str, Any],
        output_dir: Optional[str] = None,
        voice: str = "en-US-GuyNeural",
        rate: str = "+10%"
    ) -> str:
        """
        Generate audio for full script with pauses.
        
        Args:
            script_data: Dict with 'hook', 'body_lines', 'cliffhanger'
            output_dir: Directory to save MP3
            voice: Voice ID
            rate: Speed adjustment
        
        Returns:
            Path to generated MP3
        """
        if output_dir is None:
            output_dir = self.output_dir
        
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True, parents=True)
        
        # Build full text with pauses
        parts = []
        
        # Hook (3 seconds, then pause)
        parts.append(script_data['hook'])
        parts.append(". ")  # Natural pause
        
        # Body lines
        for line in script_data['body_lines']:
            parts.append(line)
            if line.endswith('.'):
                parts.append(" ")
            elif line.endswith('?'):
                parts.append(" ")
        
        # Cliffhanger
        parts.append(script_data['cliffhanger'])
        
        full_text = " ".join(parts)
        
        # Generate filename
        safe_hook = script_data['hook'].replace(' ', '_').replace('?', '').replace('!', '')[:30]
        output_file = output_dir / f"{safe_hook}_edge.mp3"
        
        # Run async generation
        asyncio.run(self.generate_tts(
            text=full_text,
            output_path=str(output_file),
            voice=voice,
            rate=rate,
            write_subtitles=True
        ))
        
        return str(output_file)
    
    def list_recommended_voices(self):
        """Display recommended voices for TikTok content."""
        print("\n🎙️  Recommended Edge-TTS Voices for TikTok:\n")
        
        voices = {
            'en-US-GuyNeural': 'Male, conversational, natural (BEST)',
            'en-US-JennyNeural': 'Female, clear, engaging',
            'en-GB-SoniaNeural': 'Female, UK accent (stands out)',
            'en-US-AriaNeural': 'Female, expressive',
            'en-US-DavisNeural': 'Male, deep, authoritative',
            'en-US-AnaNeural': 'Female, calm, soothing',
        }
        
        for voice, description in voices.items():
            marker = "✅" if "BEST" in description else "  "
            print(f"{marker} {voice}")
            print(f"   {description}\n")
        
        print("\nTo test a voice:")
        print('  edge-tts --voice en-US-GuyNeural --text "Hello world" --write-media test.mp3')


def test_edge_tts():
    """Test Edge-TTS generation."""
    print("\n🧪 Testing Edge-TTS...")
    
    generator = EdgeTTSGenerator()
    
    # Test basic generation
    test_text = "My wife was living a double life. I thought I knew everything about Sarah."
    
    print(f"\nGenerating TTS for: '{test_text}'")
    print("Voice: en-US-GuyNeural")
    print("Rate: +10% (1.1x)")
    
    try:
        output_path = asyncio.run(generator.generate_tts(
            text=test_text,
            output_path="test_output.mp3",
            voice="en-US-GuyNeural",
            rate="+10%",
            write_subtitles=True
        ))
        
        print(f"\n✅ Test successful!")
        print(f"   Audio: {output_path}")
        print(f"   Subtitles: {output_path.replace('.mp3', '.srt')}")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        print("   Make sure edge-tts is installed: pip install edge-tts")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Edge-TTS Generator')
    parser.add_argument('--test', action='store_true', help='Run test generation')
    parser.add_argument('--text', help='Text to synthesize')
    parser.add_argument('--voice', default='en-US-GuyNeural', help='Voice ID')
    parser.add_argument('--rate', default='+10%', help='Speed adjustment')
    parser.add_argument('--output', default='output.mp3', help='Output file')
    parser.add_argument('--list-voices', action='store_true', help='List recommended voices')
    
    args = parser.parse_args()
    
    if args.test:
        test_edge_tts()
    elif args.list_voices:
        generator = EdgeTTSGenerator()
        generator.list_recommended_voices()
    elif args.text:
        generator = EdgeTTSGenerator()
        asyncio.run(generator.generate_tts(
            text=args.text,
            output_path=args.output,
            voice=args.voice,
            rate=args.rate,
            write_subtitles=True
        ))
    else:
        print("Edge-TTS Generator for TikTok")
        print("\nUsage:")
        print("  python edge_tts_generator.py --test")
        print("  python edge_tts_generator.py --list-voices")
        print('  python edge_tts_generator.py --text "Hello world" --voice en-US-GuyNeural')
        print("\nRecommended voice: en-US-GuyNeural (male, conversational)")
        print("Recommended speed: +10% (1.1x for viral pacing)")
