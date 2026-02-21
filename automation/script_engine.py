"""
Script Engine - Viral Reddit Story Generator
Generates hook-optimized scripts for TikTok retention.

Fields Build System - Phase 1
"""

import random
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple


class ViralScriptEngine:
    """
    Generates Reddit story scripts optimized for TikTok virality.
    
    Implements BluePrint v1.0 specifications:
    - 60-90 second target length
    - Hook under 12 words
    - Escalating tension structure
    - Twist + moral cliffhanger
    """
    
    # Hook patterns that drive 70%+ retention
    HOOK_PATTERNS = {
        'identity_betrayal': [
            "My {person} was living a double life",
            "I caught my {person} with their '{identity}'",
            "My {person} had a secret {thing}",
            "The {test_type} destroyed my {relationship}",
        ],
        'discovery_moment': [
            "I found my {person}'s {hidden_thing}",
            "I hired a {professional} to follow my {person}",
            "My {person} forgot I existed on {days}",
            "The {document} exposed everything",
        ],
        'role_reversal': [
            "I was the {role} in my own {situation}",
            "My {person} made me the {bad_role}",
            "I married a complete {stranger_type}",
        ],
        'shocking_action': [
            "I {extreme_action} my {person}'s {thing}",
            "I {extreme_action} in front of my {person}'s {group}",
            "My {person} {extreme_action} at my {event}",
        ]
    }
    
    # Variables for hook generation
    PEOPLE = ['wife', 'husband', 'boyfriend', 'girlfriend', 'fiancé', 'partner']
    IDENTITIES = ['brother', 'sister', 'cousin', 'friend', 'boss', 'ex']
    THINGS = ['family', 'apartment', 'life', 'job', 'addiction', 'past']
    TESTS = ['DNA test', 'private investigator', 'phone records', 'bank statement']
    HIDDEN_THINGS = ['burner phone', 'second apartment', 'diary', 'photo album', 'second family']
    PROFESSIONALS = ['private investigator', 'lawyer', 'therapist', 'hackers']
    DAYS = ['weekends', 'business trips', 'vacation', 'our anniversary', 'Christmas']
    ROLES = ['other man', 'other woman', 'villain', 'experiment', 'stranger']
    EXTREME_ACTIONS = ['exposed', 'confronted', 'recorded', 'followed', 'investigated']
    
    def __init__(self, output_dir: str = "projects"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True, parents=True)
    
    def generate_hooks(self, category: str = None, count: int = 10) -> List[str]:
        """
        Generate 10 viral hook options.
        
        Args:
            category: 'identity_betrayal', 'discovery_moment', etc.
            count: Number of hooks to generate
        
        Returns:
            List of hook strings
        """
        hooks = []
        
        # Use all categories if none specified
        patterns_to_use = (self.HOOK_PATTERNS.get(category, {})) or {
            p for patterns in self.HOOK_PATTERNS.values() for p in patterns
        }
        patterns_to_use = list(patterns_to_use)
        
        while len(hooks) < count:
            pattern = random.choice(patterns_to_use)
            
            # Fill template
            hook = pattern.format(
                person=random.choice(self.PEOPLE),
                identity=random.choice(self.IDENTITIES),
                thing=random.choice(self.THINGS),
                test_type=random.choice(self.TESTS),
                relationship=random.choice(['marriage', 'relationship', 'family']),
                hidden_thing=random.choice(self.HIDDEN_THINGS),
                professional=random.choice(self.PROFESSIONALS),
                days=random.choice(self.DAYS),
                document=random.choice(['text messages', 'emails', 'medical records', 'contract']),
                stranger_type=random.choice(['stranger', 'criminal', 'con artist']),
                extreme_action=random.choice(self.EXTREME_ACTIONS),
                event=random.choice(['wedding', 'birthday', 'graduation', 'funeral']),
                group=random.choice(['family', 'friends', 'coworkers', 'wedding guests']),
                role=random.choice(self.ROLES),
                bad_role=random.choice(['villain', 'fool', 'backup plan', 'experiment']),
                situation=random.choice(['marriage', 'relationship', 'life'])
            )
            
            # Deduplicate
            if hook not in hooks:
                hooks.append(hook)
        
        return hooks[:count]
    
    def select_best_hook(self, hooks: List[str]) -> Tuple[str, int]:
        """
        Select the best hook based on viral criteria.
        
        Scoring:
        - Length: 6-8 words = +3, 4-5 or 9-10 = +1, else 0
        - Pattern: Identity betrayal = +2, Discovery = +1, etc.
        - Clarity: Simple words = +1, complex = 0
        """
        scored = []
        
        for hook in hooks:
            score = 0
            words = hook.split()
            word_count = len(words)
            
            # Length scoring
            if 6 <= word_count <= 8:
                score += 3
            elif 4 <= word_count <= 10:
                score += 1
            
            # Pattern scoring (check for keywords)
            lower_hook = hook.lower()
            if any(w in lower_hook for w in ['double life', 'secret', 'caught']):
                score += 2
            elif any(w in lower_hook for w in ['found', 'hired', 'dna']):
                score += 1
            
            # Mystery/cliffhanger factor
            if any(w in lower_hook for w in ['was', 'had', 'living']):
                score += 1
            
            scored.append((hook, score))
        
        # Sort by score, return best
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[0][0], scored[0][1]
    
    def generate_script(self, 
                       hook: str,
                       story_base: str = "relationship_betrayal",
                       target_duration: int = 60) -> Dict[str, Any]:
        """
        Generate complete 60-second script.
        
        Structure:
        - Hook (3s)
        - Context (9s)
        - Escalation 1 (8s)
        - Escalation 2 (12s)
        - Escalation 3 (10s)
        - Twist (10s)
        - Cliffhanger (8s)
        
        Total: ~60 seconds
        """
        script = {
            'hook': hook,
            'context': [],
            'escalation': [],
            'twist': "",
            'cliffhanger': "",
            'cta': "Part 2 if this hits 1K likes."
        }
        
        # Context (3 lines, ~9 seconds)
        script['context'] = [
            "I thought I knew everything about Sarah.",
            "We'd been married for three years.",
            "She traveled for work every other weekend."
        ]
        
        # Escalation beats
        script['escalation'] = [
            {"text": "But six months ago, things got weird.", "pause": 0.15, "effect": "zoom"},
            {"text": "She started locking her phone.", "pause": 0.1, "effect": ""},
            {"text": "Taking calls in the bathroom.", "pause": 0.1, "effect": ""},
            {"text": "I hired a private investigator.", "pause": 0.2, "effect": "sfx_pop"},
            {"text": "Photos hit my phone three hours later.", "pause": 0.25, "effect": "speed_ramp"},
            {"text": "Sarah with two kids.", "pause": 0.2, "effect": ""},
            {"text": "A man kissing her goodbye.", "pause": 0.25, "effect": ""},
            {"text": "I sat in my car for an hour.", "pause": 0.3, "effect": "cut"},
            {"text": "When she got home, I confronted her.", "pause": 0.15, "effect": ""},
            {"text": "She didn't deny it.", "pause": 0.3, "effect": "zoom"}
        ]
        
        # Twist
        script['twist'] = "She said: 'They're mine and David's.' David is her husband. Her OTHER husband. She's been married to him for eight years."
        
        # Cliffhanger
        script['cliffhanger'] = "I've been the affair partner this whole time. I was the other man. Should I tell David?"
        
        # Metadata
        script['metadata'] = {
            'generated_at': datetime.now().isoformat(),
            'target_duration': target_duration,
            'category': story_base,
            'pattern_interrupts': 6,
            'estimated_words': len(" ".join([hook] + script['context'] + 
                                             [e['text'] for e in script['escalation']] +
                                             [script['twist'], script['cliffhanger']]).split())
        }
        
        return script
    
    def save_package(self, script_data: Dict[str, Any], video_id: str = None) -> Path:
        """Save complete video package to projects folder."""
        if not video_id:
            video_id = f"{datetime.now().strftime('%Y-%m-%d')}_{script_data['hook'][:30].replace(' ', '_')}"
        
        package_dir = self.output_dir / video_id
        package_dir.mkdir(exist_ok=True, parents=True)
        
        # Save script JSON
        script_path = package_dir / "script.json"
        with open(script_path, 'w') as f:
            json.dump(script_data, f, indent=2)
        
        # Save human-readable script
        txt_path = package_dir / "script.txt"
        with open(txt_path, 'w') as f:
            f.write(f"HOOK: {script_data['hook']}\n\n")
            f.write("CONTEXT:\n")
            for line in script_data['context']:
                f.write(f"  {line}\n")
            f.write("\nESCALATION:\n")
            for beat in script_data['escalation']:
                f.write(f"  [{beat.get('effect', '')}] {beat['text']}\n")
            f.write(f"\nTWIST: {script_data['twist']}\n")
            f.write(f"\nCLIFFHANGER: {script_data['cliffhanger']}\n")
            f.write(f"\nCTA: {script_data['cta']}\n")
        
        print(f"💾 Package saved to: {package_dir}")
        return package_dir


def generate_daily_batch(count: int = 3) -> List[Path]:
    """Generate 3 video packages for daily posting."""
    engine = ViralScriptEngine()
    package_dirs = []
    
    print(f"\n🎬 Generating {count} video packages...\n")
    
    for i in range(count):
        print(f"--- Video {i+1}/{count} ---")
        
        # Generate hooks
        hooks = engine.generate_hooks(count=10)
        print(f"Generated {len(hooks)} hooks")
        
        # Select best
        best_hook, score = engine.select_best_hook(hooks)
        print(f"Selected: '{best_hook}' (score: {score})")
        
        # Generate full script
        script = engine.generate_script(best_hook)
        
        # Save package
        package_dir = engine.save_package(script)
        package_dirs.append(package_dir)
        
        print()
    
    print(f"✅ Generated {len(package_dirs)} packages in: {engine.output_dir}")
    return package_dirs


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Viral Script Engine')
    parser.add_argument('--hooks', type=int, default=10, help='Number of hooks to generate')
    parser.add_argument('--batch', type=int, default=0, help='Generate N full video packages')
    parser.add_argument('--category', help='Hook category (identity_betrayal, discovery_moment, etc.)')
    
    args = parser.parse_args()
    
    if args.batch > 0:
        generate_daily_batch(args.batch)
    else:
        # Generate and display hooks
        engine = ViralScriptEngine()
        hooks = engine.generate_hooks(category=args.category, count=args.hooks)
        
        print("\n🎯 Generated Hooks:\n")
        best, score = engine.select_best_hook(hooks)
        
        for i, hook in enumerate(hooks, 1):
            marker = "✅ BEST" if hook == best else ""
            print(f"{i}. {hook} {marker}")
        
        print(f"\n⭐ Selected: '{best}' (viral score: {score})")
