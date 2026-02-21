#!/usr/bin/env python3
"""
Batch Script Generator for Fields
Generate 3 complete Reddit story scripts for tomorrow's content
"""

import sys
sys.path.insert(0, 'C:\\Users\\field\\.openclaw\\workspace')

import json
import os
from automation.script_engine import ViralScriptEngine, generate_daily_batch

# Create output directory
output_dir = 'projects/2026-02-20_night_batch'
os.makedirs(output_dir, exist_ok=True)

print("🎯 Generating 3 viral Reddit story scripts...\n")

# Generate 3 packages
package_dirs = generate_daily_batch(count=3)

print(f"\n✅ Generated {len(package_dirs)} video packages")
print(f"📁 Saved to: projects/")
print("🚀 Ready for TTS generation!")

# Create summary
summary = {
    "batch_date": "2026-02-20",
    "videos_generated": len(package_dirs),
    "packages": [str(d) for d in package_dirs],
    "status": "READY_FOR_TTS"
}

with open(f"{output_dir}/batch_summary.json", 'w') as f:
    json.dump(summary, f, indent=2)

print(f"\n📋 Summary saved: {output_dir}/batch_summary.json")
