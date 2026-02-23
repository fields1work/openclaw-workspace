import discord

TOKEN = "YOUR_BOT_TOKEN_HERE"  # Get from discord.com/developers

intents = discord.Intents.default()
intents.guilds = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot: {client.user}")
    print(f"📊 In {len(client.guilds)} servers:\n")
    for guild in client.guilds:
        print(f"  • {guild.name} (ID: {guild.id})")
    await client.close()

client.run(TOKEN)
