# Discord AI Integration - CEO (Fields) monitoring via CTO (Aneko) + Junior Analyst (Bot)
# Hierarchy: Fields (CEO) → Aneko (CTO) → Bot (Junior Analyst)
# The Junior Analyst never fucks up the coffee order.

import discord
import asyncio
import json
from datetime import datetime

TOKEN = "YOUR_BOT_TOKEN"  # Get from discord.com/developers
GUILD_ID = 1474950545704747010

# What the Junior Analyst monitors
MONITOR_CHANNELS = [
    "❓｜help-desk",
    "💬｜general-chat", 
    "✅｜wins",
    "🎯｜daily-goals",
    "📈｜milestones"
]

# Where CTO reports to CEO
EXECUTIVE_SUMMARY_CHANNEL = "📊｜analytics-review"

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True  # Privileged intent

client = discord.Client(intents=intents)

# Message log for CEO (Fields) review via CTO (Aneko)
message_queue = []

@client.event
async def on_ready():
    print(f"🤖 Junior Analyst (Bot) reporting for duty!")
    print(f"   Discord: {client.user}")
    print(f"   Server: AI Income HQ")
    print(f"   🎯 CEO: Fields (Vision, Strategy, Public Face)")
    print(f"   ⚙️ CTO: Aneko (Technical, Automation, Infrastructure)")
    print(f"   📊 Junior Analyst: Bot (Monitoring, Data, 24/7)")
    print(f"\n📡 Monitoring channels: {MONITOR_CHANNELS}")
    print(f"📊 Executive summaries to: {EXECUTIVE_SUMMARY_CHANNEL}")
    print(f"⏰ Standing by for messages...\n")

@client.event
async def on_message(message):
    # Skip bot's own messages
    if message.author.bot:
        return
    
    # Only monitor specific channels
    if message.channel.name not in MONITOR_CHANNELS:
        return
    
    # Log for CEO (Fields) review via CTO (Aneko)
    entry = {
        "timestamp": datetime.now().isoformat(),
        "channel": message.channel.name,
        "author": str(message.author),
        "content": message.content
    }
    message_queue.append(entry)
    
    # Junior Analyst auto-responses
    await auto_respond(message)
    
    # Log to file for CTO review
    with open("discord_activity_log.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")

async def auto_respond(message):
    """Junior Analyst auto-responses (basic competence, no creativity)"""
    content_lower = message.content.lower()
    
    # Help trigger - Junior Analyst escalates to CTO if needed
    if content_lower in ["!help", "help", "how do i", "how to"]:
        await asyncio.sleep(1)
        await message.channel.send(
            f"Hey {message.author.mention}! Check #🚀｜getting-started or ask in #❓｜help-desk. "
            "I'm the Junior Analyst — I track data. "
            "For strategic questions, our CTO @Aneko reviews hourly. 🐾"
        )
        return
    
    # Win celebration - Junior Analyst flags for CEO
    if "!win" in content_lower or any(word in content_lower for word in ["first dollar", "first sale", "made money", "hit 1k"]):
        await asyncio.sleep(1)
        await message.add_reaction("🎉")
        await message.add_reaction("🔥")
        await message.channel.send(
            f"🎉 **WIN ALERT!** {message.author.mention} posted a win! "
            "CEO @Fields reviews all wins daily. Everyone drop 👏 in #✅｜wins!"
        )
        # Notify CTO to alert CEO
        print(f"[CEO ALERT] Win posted by {message.author} — CEO Fields should review")
        return
    
    # Accountability check
    if message.channel.name == "🎯｜daily-goals":
        await message.add_reaction("✅")
        return

async def executive_summary():
    """CTO (Aneko) generates hourly report for CEO (Fields)"""
    while True:
        await asyncio.sleep(3600)  # Every hour
        
        if not message_queue:
            continue
        
        # Analyze data (CTO work)
        channels_activity = {}
        user_activity = {}
        questions_asked = []
        wins_reported = []
        
        for entry in message_queue.copy():
            channels_activity[entry["channel"]] = channels_activity.get(entry["channel"], 0) + 1
            user_activity[entry["author"]] = user_activity.get(entry["author"], 0) + 1
            
            # Categorize for CEO
            if entry["channel"] == "❓｜help-desk":
                questions_asked.append(entry)
            elif entry["channel"] == "✅｜wins":
                wins_reported.append(entry)
        
        # Clear queue
        message_queue.clear()
        
        # Send executive summary to CEO
        guild = client.get_guild(GUILD_ID)
        if not guild:
            continue
        
        summary_ch = discord.utils.get(guild.text_channels, name=EXECUTIVE_SUMMARY_CHANNEL)
        if not summary_ch:
            continue
        
        summary = f"""📊 **EXECUTIVE SUMMARY FOR CEO Fields**

**Report from CTO Aneko** | Hourly Update

**📈 Activity Overview:**
• Channels Active: {len(channels_activity)}
• Total Messages: {sum(channels_activity.values())}
• Active Members: {len(user_activity)}

**❓ Questions Requiring CEO/CTO Attention:** {len(questions_asked)}
{chr(10).join(f"   • {q['author']}: {q['content'][:60]}..." for q in questions_asked[:3]) if questions_asked else "   • None this hour"}

**🏆 Wins Reported:** {len(wins_reported)}
{chr(10).join(f"   • {w['author']}: {w['content'][:60]}..." for w in wins_reported) if wins_reported else "   • None this hour"}

**💡 CTO Recommendation:**
{"Review #❓｜help-desk for strategic responses" if questions_asked else "Community engaged, no action required"}

_— Reported by Junior Analyst, Analyzed by CTO Aneko_ 🐾
        """
        
        await summary_ch.send(summary)
        print(f"[CTO→CEO] Executive summary sent to #{EXECUTIVE_SUMMARY_CHANNEL}")

async def post_as_cto(channel_name, content):
    """CTO (Aneko) posting through Junior Analyst (Bot)"""
    guild = client.get_guild(GUILD_ID)
    if not guild:
        return False
    
    ch = discord.utils.get(guild.text_channels, name=channel_name)
    if not ch:
        return False
    
    await ch.send(f"⚙️ **CTO Update:** {content}")
    return True

# Start background tasks
@client.event
async def setup_hook():
    client.loop.create_task(executive_summary())

print("🔌 Initializing Organization Hierarchy...")
print("CEO Fields → CTO Aneko → Junior Analyst Bot")
print("\n🚀 Bot is LIVE and Monitoring!")
print("⏰ Executive summaries every hour to #📊｜analytics-review")
print("📡 Command '\\!help' now works in Discord")

# ACTUALLY START THE BOT
client.run(TOKEN)

