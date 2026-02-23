import discord
import asyncio

TOKEN = "YOUR_BOT_TOKEN"  # Get from discord.com/developers
GUILD_ID = 1474950545704747010

intents = discord.Intents.default()
intents.guilds = True
client = discord.Client(intents=intents)

MESSAGES = [
    ("👋｜welcome", "🎉 **WELCOME TO AI INCOME HQ!** 🎉\n\nThis is where hustlers build AI-powered income streams.\n\n**Quick Start:**\n1️⃣ Read #📜｜rules\n2️⃣ Introduce yourself in #🤝｜introductions\n3️⃣ Set goals in #🎯｜daily-goals\n\nLet's build! 🚀"),
    
    ("📜｜rules", "📜 **SERVER RULES**\n\n1️⃣ **Build In Public** - Share progress, wins, losses\n2️⃣ **No Spam** - Provide value first\n3️⃣ **Help Each Other** - We're all figuring this out\n4️⃣ **Document Everything** - Screenshots, metrics, lessons\n5️⃣ **No Get-Rich-Quick BS** - Real strategies only\n6️⃣ **Respect the Grind** - Everyone's at different stages\n7️⃣ **Have Fun** - Marathon, not a sprint"),
    
    ("🚀｜getting-started", "🚀 **GETTING STARTED**\n\n**Phase 1 (Week 1):** Choose niche, set up TikTok, post first video\n**Phase 2 (Week 2-4):** Daily posting habit, cross-platform\n**Phase 3 (Month 2):** First $1 → $100\n\n**Tools:** CapCut, ElevenLabs, AI prompting\n\nNeed help? Ask in #❓｜help-desk"),
    
    ("❓｜faq", "❓ **FAQ**\n\n**Q: Do I need money to start?**\nA: Nope. TikTok is free. Start with $0.\n\n**Q: How long until I make money?**\nA: 2-4 weeks for first $1, 2-3 months for consistent income.\n\n**Q: Do I need to show my face?**\nA: Nope. Faceless channels do great.\n\n**Q: How many videos until I blow up?**\nA: Could be 1, could be 100. Consistency beats luck."),
    
    ("🎉｜announcements", "🎉 **AI INCOME HQ IS LIVE!** 🎉\n\n✅ 7 categories\n✅ 29 channels\n✅ Complete system for tracking your AI side hustle\n\n**This Week:** Get everyone to post their first TikTok.\n\nDrop a 🚀 if you're ready to build!"),
    
    ("🎯｜daily-goals", "🎯 **DAILY GOALS TEMPLATE**\n\nCopy this:\n```\n📅 Date: [Date]\n🎯 Goal: [One big thing]\n📋 Tasks:\n- [ ] Task 1\n- [ ] Task 2\n💰 Revenue Target: $[amount]\n🎥 Content: [videos]\n```\n\nAccountability is everything. Post daily!"),
    
    ("✅｜wins", "🏆 **WIN OF THE DAY**\n\nFirst win: @Fields built this entire Discord server during his Amazon break!\n\nBuilding infrastructure WHILE working 9-5. That's hustle. 🐾\n\n**Drop your wins here:**\n• First follower? POST IT.\n• First dollar? POST IT.\n• First 1K views? POST IT.\n\nNo win too small!"),
    
    ("💬｜general-chat", "🎉 Server is live! Welcome to AI Income HQ! Drop a 👋 to say hi!"),
]

@client.event
async def on_ready():
    print(f"✅ Bot: {client.user}")
    guild = client.get_guild(GUILD_ID)
    
    if not guild:
        print("❌ Guild not found")
        await client.close()
        return
    
    print(f"\n📤 Sending messages to channels...")
    
    for channel_name, message in MESSAGES:
        try:
            # Find channel
            ch = discord.utils.get(guild.text_channels, name=channel_name)
            if not ch:
                print(f"  ❌ Channel '{channel_name}' not found")
                continue
            
            # Send message
            await ch.send(message)
            print(f"  ✅ Sent to #{channel_name}")
            
            # Wait to avoid rate limits
            await asyncio.sleep(2)
            
        except Exception as e:
            print(f"  ❌ Error in #{channel_name}: {e}")
            await asyncio.sleep(5)  # Longer delay on error
    
    print("\n🎉 Done!")
    await client.close()

print("🔌 Starting...")
client.run(TOKEN)
