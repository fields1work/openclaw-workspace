# Discord Server Builder - Fixed Version
import discord
import asyncio

TOKEN = "YOUR_BOT_TOKEN_HERE"  # Get from discord.com/developers
GUILD_ID = 1474950545704747010

intents = discord.Intents.default()
intents.guilds = True
client = discord.Client(intents=intents)

CATEGORIES = [
    ("📌 START HERE", ["👋｜welcome", "📜｜rules", "🚀｜getting-started", "❓｜faq", "🎉｜announcements"]),
    ("📊 PROGRESS TRACKING", ["🎯｜daily-goals", "✅｜wins", "📈｜milestones", "💵｜revenue-log"]),
    ("🤖 AI OPERATIONS", ["🧠｜prompt-engineering", "🔄｜automation", "🎨｜content-generation", "🛠️｜tools-resources"]),
    ("🎥 CONTENT MACHINE", ["📝｜script-ideas", "📹｜video-feedback", "🔥｜viral-strategies", "📱｜platform-tips"]),
    ("💰 MONETIZATION", ["💡｜money-ideas", "🤝｜collaborations", "📊｜analytics-review", "💬｜sponsorships"]),
    ("🧠 STRATEGY LAB", ["🎯｜niche-selection", "📚｜case-studies", "🔬｜experiments", "💭｜mindset"]),
    ("👥 COMMUNITY", ["💬｜general-chat", "🤝｜introductions", "❓｜help-desk"])
]

VOICE_CHANNELS = ["🎙️｜general-vc", "🎙️｜office-hours", "🎙️｜collab-room"]

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    guild = client.get_guild(GUILD_ID)
    
    if not guild:
        print(f"❌ Guild {GUILD_ID} not found")
        await client.close()
        return
    
    print(f"🎯 Building: {guild.name}")
    print(f"📊 Starting with {len(guild.channels)} channels")
    
    # Create categories and text channels
    for cat_name, channels in CATEGORIES:
        try:
            # Check if category exists
            existing = discord.utils.get(guild.categories, name=cat_name)
            if existing:
                category = existing
                print(f"  ⏭️ Category '{cat_name}' exists")
            else:
                category = await guild.create_category(cat_name)
                print(f"  ✅ Created category: {cat_name}")
                await asyncio.sleep(1)
            
            # Create channels
            for ch_name in channels:
                try:
                    existing_ch = discord.utils.get(guild.channels, name=ch_name.replace("｜", "-").lower())
                    if existing_ch:
                        print(f"    ⏭️ Channel '{ch_name}' exists")
                        continue
                    
                    await guild.create_text_channel(ch_name, category=category)
                    print(f"    ✅ Created: {ch_name}")
                    await asyncio.sleep(0.5)
                except Exception as e:
                    print(f"    ❌ {ch_name}: {e}")
                    
        except Exception as e:
            print(f"  ❌ Category {cat_name}: {e}")
    
    # Create voice channels in COMMUNITY category
    community_cat = discord.utils.get(guild.categories, name="👥 COMMUNITY")
    if community_cat:
        for vc_name in VOICE_CHANNELS:
            try:
                await guild.create_voice_channel(vc_name, category=community_cat)
                print(f"    ✅ Created voice: {vc_name}")
                await asyncio.sleep(0.5)
            except Exception as e:
                print(f"    ❌ {vc_name}: {e}")
    
    # Send welcome message
    welcome = discord.utils.get(guild.text_channels, name="👋｜welcome".replace("｜", "-").lower())
    if welcome:
        embed = discord.Embed(
            title="Welcome to AI Income HQ! 🚀",
            description="Building AI-powered income streams together.\n\nCheck #🚀｜getting-started to begin!",
            color=0xFF5A36
        )
        await welcome.send(embed=embed)
        print("📨 Welcome message sent")
    
    print("\n🎉 BUILD COMPLETE!")
    print(f"📊 Now has {len(guild.channels)} channels")
    await client.close()

print("🔌 Connecting...")
client.run(TOKEN)
