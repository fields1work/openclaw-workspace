import discord

TOKEN = "YOUR_BOT_TOKEN"  # Get from discord.com/developers
GUILD_ID = 1474950545704747010

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot: {client.user}")
    guild = client.get_guild(GUILD_ID)
    
    if not guild:
        print("❌ Guild not found")
        await client.close()
        return
    
    print(f"\n📊 Server: {guild.name}")
    print(f"🔧 Bot permissions in server:")
    
    # Check bot's permissions
    me = guild.me
    if me:
        print(f"   - Administrator: {me.guild_permissions.administrator}")
        print(f"   - Send Messages: {me.guild_permissions.send_messages}")
        print(f"   - Manage Channels: {me.guild_permissions.manage_channels}")
        print(f"   - View Channels: {me.guild_permissions.view_channel}")
    
    print(f"\n📋 Channels found ({len(guild.channels)} total):")
    
    text_channels = [ch for ch in guild.channels if isinstance(ch, discord.TextChannel)]
    print(f"\n📝 Text Channels ({len(text_channels)}):")
    for ch in sorted(text_channels, key=lambda c: c.position):
        print(f"   • #{ch.name} (ID: {ch.id})")
        # Check last few messages
        try:
            async for msg in ch.history(limit=3):
                print(f"      Last msg: {msg.author.name}: {msg.content[:50]}...")
        except:
            print(f"      (Can't read history)")
    
    print(f"\n📁 Categories ({len(guild.categories)}):")
    for cat in sorted(guild.categories, key=lambda c: c.position):
        print(f"   • {cat.name}")
        for ch in cat.channels:
            if isinstance(ch, discord.TextChannel):
                print(f"      └─ #{ch.name}")
    
    await client.close()

print("🔍 Diagnosing Discord...")
client.run(TOKEN)
