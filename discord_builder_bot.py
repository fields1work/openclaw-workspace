# Discord Server Builder Bot
# Token: YOUR_BOT_TOKEN_HERE

import discord
from discord.ext import commands
import asyncio
import os

# Bot configuration
TOKEN = "YOUR_BOT_TOKEN_HERE"
GUILD_ID = 1353449434620502046  # AI Income HQ

# Server blueprint structure
CATEGORIES = [
    {
        "name": "📌 START HERE",
        "channels": [
            {"name": "👋｜welcome", "type": "text", "topic": "Welcome to AI Income HQ! Read the rules and get started here."},
            {"name": "📜｜rules", "type": "text", "topic": "Server rules and guidelines"},
            {"name": "🚀｜getting-started", "type": "text", "topic": "How to get started with your AI side hustle"},
            {"name": "❓｜faq", "type": "text", "topic": "Frequently asked questions"},
            {"name": "🎉｜announcements", "type": "text", "topic": "Important updates and announcements"},
        ]
    },
    {
        "name": "📊 PROGRESS TRACKING",
        "channels": [
            {"name": "🎯｜daily-goals", "type": "text", "topic": "Share your daily goals and targets"},
            {"name": "✅｜wins", "type": "text", "topic": "Celebrate your wins, big or small!"},
            {"name": "📈｜milestones", "type": "text", "topic": "Track important milestones"},
            {"name": "💵｜revenue-log", "type": "text", "topic": "Log your earnings and revenue progress"},
        ]
    },
    {
        "name": "🤖 AI OPERATIONS",
        "channels": [
            {"name": "🧠｜prompt-engineering", "type": "text", "topic": "Share and discuss AI prompts"},
            {"name": "🔄｜automation", "type": "text", "topic": "Automation workflows and tools"},
            {"name": "🎨｜content-generation", "type": "text", "topic": "AI-generated content discussion"},
            {"name": "🛠️｜tools-resources", "type": "text", "topic": "Useful AI tools and resources"},
        ]
    },
    {
        "name": "🎥 CONTENT MACHINE",
        "channels": [
            {"name": "📝｜script-ideas", "type": "text", "topic": "TikTok/video script ideas and brainstorming"},
            {"name": "📹｜video-feedback", "type": "text", "topic": "Get feedback on your videos"},
            {"name": "🔥｜viral-strategies", "type": "text", "topic": "Discuss viral content strategies"},
            {"name": "📱｜platform-tips", "type": "text", "topic": "Tips for TikTok, YouTube, Instagram, Twitter"},
        ]
    },
    {
        "name": "💰 MONETIZATION",
        "channels": [
            {"name": "💡｜money-ideas", "type": "text", "topic": "Monetization strategies and ideas"},
            {"name": "🤝｜collaborations", "type": "text", "topic": "Find collaboration opportunities"},
            {"name": "📊｜analytics-review", "type": "text", "topic": "Review and analyze your performance"},
            {"name": "💬｜sponsorships", "type": "text", "topic": "Sponsorship deals and brand partnerships"},
        ]
    },
    {
        "name": "🧠 STRATEGY LAB",
        "channels": [
            {"name": "🎯｜niche-selection", "type": "text", "topic": "Choosing and refining your content niche"},
            {"name": "📚｜case-studies", "type": "text", "topic": "Learn from successful creators"},
            {"name": "🔬｜experiments", "type": "text", "topic": "A/B testing and growth experiments"},
            {"name": "💭｜mindset", "type": "text", "topic": "Entrepreneurial mindset and motivation"},
        ]
    },
    {
        "name": "👥 COMMUNITY",
        "channels": [
            {"name": "💬｜general-chat", "type": "text", "topic": "General discussion"},
            {"name": "🤝｜introductions", "type": "text", "topic": "Introduce yourself!"},
            {"name": "❓｜help-desk", "type": "text", "topic": "Ask questions and get help"},
            {"name": "🎙️｜general-vc", "type": "voice", "topic": "General voice chat"},
            {"name": "🎙️｜office-hours", "type": "voice", "topic": "Office hours and focused work"},
            {"name": "🎙️｜collab-room", "type": "voice", "topic": "Collaboration and brainstorming"},
        ]
    },
]

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot logged in as {bot.user}")
    
    guild = bot.get_guild(GUILD_ID)
    if not guild:
        print(f"❌ Guild {GUILD_ID} not found")
        return
    
    print(f"🎯 Building server: {guild.name}")
    print(f"📊 Current channels: {len(guild.channels)}")
    print(f"📊 Current categories: {len(guild.categories)}")
    
    # Create categories and channels
    for category_data in CATEGORIES:
        try:
            # Check if category exists
            existing_cat = discord.utils.get(guild.categories, name=category_data["name"])
            if existing_cat:
                print(f"  ⏭️ Category '{category_data['name']}' already exists, skipping")
                category = existing_cat
            else:
                # Create category
                category = await guild.create_category(category_data["name"])
                print(f"  ✅ Created category: {category.name}")
                await asyncio.sleep(0.5)
            
            # Create channels in category
            for channel_data in category_data["channels"]:
                try:
                    existing_channel = discord.utils.get(category.channels, name=channel_data["name"].replace("｜", "-").lower())
                    if existing_channel:
                        print(f"    ⏭️ Channel '{channel_data['name']}' already exists")
                        continue
                    
                    if channel_data["type"] == "text":
                        await guild.create_text_channel(
                            name=channel_data["name"],
                            category=category,
                            topic=channel_data.get("topic", "")
                        )
                        print(f"    ✅ Created text channel: {channel_data['name']}")
                    elif channel_data["type"] == "voice":
                        await guild.create_voice_channel(
                            name=channel_data["name"],
                            category=category
                        )
                        print(f"    ✅ Created voice channel: {channel_data['name']}")
                    
                    await asyncio.sleep(0.5)
                    
                except Exception as e:
                    print(f"    ❌ Error creating channel {channel_data['name']}: {e}")
                    continue
                    
        except Exception as e:
            print(f"  ❌ Error creating category {category_data['name']}: {e}")
            continue
    
    print("\n🎉 Server build complete!")
    
    # Send welcome message to welcome channel
    try:
        welcome_channel = discord.utils.get(guild.text_channels, name="👋｜welcome")
        if welcome_channel:
            welcome_embed = discord.Embed(
                title="Welcome to AI Income HQ! 🚀",
                description="""
Welcome to the community of hustlers building AI-powered income streams.

**What you'll find here:**
📊 Daily progress tracking
🤖 AI automation workflows  
🎥 Content creation strategies
💰 Monetization tactics
🧠 Growth mindset development

**To get started:**
1. Read the #📜｜rules
2. Introduce yourself in #🤝｜introductions
3. Set your goals in #🎯｜daily-goals

Let's build something great together!
                """,
                color=0xFF5A36
            )
            welcome_embed.set_footer(text="Powered by OpenClaw | Built by Aneko 🐾")
            await welcome_channel.send(embed=welcome_embed)
            print("📨 Welcome message sent")
    except Exception as e:
        print(f"⚠️ Could not send welcome message: {e}")
    
    print("\n✨ Bot setup complete! You can close this script.")
    await bot.close()

# Run the bot
print("🔌 Connecting to Discord...")
bot.run(TOKEN)
