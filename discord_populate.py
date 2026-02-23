import discord
import asyncio

TOKEN = "YOUR_BOT_TOKEN_HERE"  # Get from discord.com/developers
GUILD_ID = 1474950545704747010

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Populating {client.user}")
    guild = client.get_guild(GUILD_ID)
    
    if not guild:
        print("Guild not found")
        await client.close()
        return
    
    # Helper to get channel
    def get_ch(name):
        return discord.utils.get(guild.text_channels, name=name.replace("｜", "-").lower())
    
    # WELCOME CHANNEL
    welcome = get_ch("👋｜welcome")
    if welcome:
        embed = discord.Embed(
            title="🚀 Welcome to AI Income HQ!",
            description="""
**This is where hustlers build AI-powered income streams.**

Whether you're starting from $0 or scaling to $10K/month, this is your headquarters.

**🎯 What we do here:**
• Daily accountability & progress tracking
• Share wins (even $0.01 counts!)
• AI automation workflows
• Viral content strategies
• Monetization tactics that actually work

**📋 Quick Start:**
1️⃣ Read #📜｜rules
2️⃣ Introduce yourself in #🤝｜introductions  
3️⃣ Set your goals in #🎯｜daily-goals
4️⃣ Check out #🚀｜getting-started

**💰 First Dollar Mission:**
Our collective goal is simple: **Get everyone here to their first $1.** Then $100. Then $1,000.

Built in public. Growing together.

*— Aneko & Fields* 🐾
            """,
            color=0xFF5A36
        )
        await welcome.send(embed=embed)
        print("✅ Welcome message sent")
        await asyncio.sleep(1)
    
    # RULES CHANNEL
    rules = get_ch("📜｜rules")
    if rules:
        embed = discord.Embed(
            title="📜 Server Rules",
            description="""
**1. Build In Public**
Share your progress, wins, and losses. Transparency builds trust and attracts opportunity.

**2. No Shameless Self-Promotion**
Provide value first. Links are fine when relevant, but don't spam.

**3. Help Each Other**
Answer questions. Share resources. We're all figuring this out together.

**4. Document Everything**
Screenshots, metrics, lessons learned. Your journey helps others.

**5. No Get-Rich-Quick BS**
Real strategies only. If it sounds too good to be true, it probably is.

**6. Respect the Grind**
Everyone's at different stages. Newbies and experts welcome.

**7. Have Fun**
This is a marathon, not a sprint. Enjoy the process.

**Violations = Warning → Kick → Ban**
            """,
            color=0x2D2D2D
        )
        await rules.send(embed=embed)
        print("✅ Rules posted")
        await asyncio.sleep(1)
    
    # GETTING STARTED
    getting = get_ch("🚀｜getting-started")
    if getting:
        await getting.send("""
# 🚀 Getting Started Guide

## Phase 1: Foundation (Week 1)
**Goal:** Get set up and post your first piece of content

**Tasks:**
- [ ] Choose your niche (Reddit stories / finance / motivation)
- [ ] Set up TikTok account
- [ ] Create Linktree with affiliate links
- [ ] Sign up for Amazon Associates
- [ ] Post your first TikTok

## Phase 2: Consistency (Week 2-4)
**Goal:** Daily posting habit

**Tasks:**
- [ ] Post 1 TikTok daily
- [ ] Cross-post to YouTube Shorts
- [ ] Engage with comments (reply to everyone)
- [ ] Track metrics in #📈｜milestones

## Phase 3: Monetization (Month 2)
**Goal:** First $1 → $100

**Tasks:**
- [ ] First affiliate sale
- [ ] Apply for TikTok Creator Fund (10K followers)
- [ ] Launch Twitter/X presence
- [ ] Build email list

## Tools We Use:
**Content:** CapCut, ElevenLabs, Canva
**Automation:** Python scripts, AI APIs
**Analytics:** Native platform stats + manual tracking

**Need help?** Ask in #❓｜help-desk or check #❓｜faq
        """)
        print("✅ Getting started guide posted")
        await asyncio.sleep(1)
    
    # FAQ
    faq = get_ch("❓｜faq")
    if faq:
        await faq.send("""
# ❓ Frequently Asked Questions

**Q: Do I need money to start?**
A: Nope. TikTok is free. CapCut is free. AI tools can be free tier. Start with $0.

**Q: How long until I make money?**
A: Realistically: 2-4 weeks for first $1, 2-3 months for consistent income. Anyone promising faster is lying.

**Q: What niche should I pick?**
A: Something you're genuinely interested in. Reddit stories, finance, fitness motivation work well. Pick something you'll stick with.

**Q: Do I need to show my face?**
A: Nope. Faceless channels do great. Voice + text-to-speech works.

**Q: How many videos until I blow up?**
A: Nobody knows. Could be 1, could be 100. The key: keep posting. Consistency beats luck.

**Q: What's the best time to post?**
A: 8-10 AM and 7-9 PM in your target audience's timezone. Test and track.

**Q: Can I automate everything?**
A: 90% yes. Content generation, posting, replies. But you still need strategy and creativity.

**Q: Is this saturated?**
A: Everything's saturated. The differentiator: YOU. Your angle, your consistency, your community.

**More questions?** Drop them here!
        """)
        print("✅ FAQ posted")
        await asyncio.sleep(1)
    
    # ANNOUNCEMENTS - Pin a message
    announce = get_ch("🎉｜announcements")
    if announce:
        msg = await announce.send("""
🎉 **AI INCOME HQ IS OFFICIALLY LIVE!** 🎉

We've built out 7 categories, 30+ channels, and a complete system for tracking your AI side hustle journey.

**What's new:**
✅ Progress tracking system
✅ Community chat spaces  
✅ Strategy discussion channels
✅ Voice rooms for collabs

**This Week's Focus:**
Get everyone to post their first TikTok. If you haven't started yet, today's the day.

Drop a 🚀 if you're ready to build!
        """)
        await msg.pin()
        print("✅ Announcement pinned")
        await asyncio.sleep(1)
    
    # DAILY GOALS - Template
    goals = get_ch("🎯｜daily-goals")
    if goals:
        await goals.send("""
# 🎯 Daily Goals Template

**Copy this format for your daily post:**

```
📅 Date: [Today's Date]
🎯 Main Goal: [One big thing]
📋 Tasks:
- [ ] Task 1
- [ ] Task 2  
- [ ] Task 3
💰 Revenue Target: $[amount]
🎥 Content Goal: [videos/posts]
```

**Example:**
📅 Date: Feb 23, 2026
🎯 Main Goal: Post first TikTok
📋 Tasks:
- [ ] Edit video in CapCut
- [ ] Write caption with CTA
- [ ] Post at 7 PM
💰 Revenue Target: $0 (focus on content first)
🎥 Content Goal: 1 TikTok

**Accountability is everything.** Post your goals every morning, update at night.
        """)
        print("✅ Goals template posted")
        await asyncio.sleep(1)
    
    # WINS CHANNEL
    wins = get_ch("✅｜wins")
    if wins:
        await wins.send("""
# 🏆 Win of the Day

**First win goes to:** @Fields for setting up this entire Discord server during his Amazon break. 

Building infrastructure WHILE working a 9-5. That's the hustle. 🐾

---

**Drop your wins here:**
- First follower? POST IT.
- First dollar? POST IT.
- First 1K views? POST IT.
- Fixed a bug? POST IT.

**No win is too small.** Document everything.
        """)
        print("✅ First win posted")
        await asyncio.sleep(1)
    
    # AI OPERATIONS
    ai_ops = get_ch("🧠｜prompt-engineering")
    if ai_ops:
        await ai_ops.send("""
# 🧠 Prompt Engineering Resources

**Viral Hook Formulas:**
```
"I [shocking action] and [unexpected result]"
"Nobody is talking about [secret/niche topic]"  
"I found out [surprising fact] and I'm not okay"
"[Authority figure] told me [contrarian advice]"
```

**Content Generation Prompt:**
```
Write a 30-second TikTok script about [topic].
Hook: First 3 seconds must stop the scroll.
Body: 2-3 information beats.
CTA: "Follow for part 2" or "Link in bio."
Tone: Casual, conversational, slightly edgy.
```

**Drop your best prompts below!**
        """)
        print("✅ AI prompts posted")
        await asyncio.sleep(1)
    
    # SCRIPT IDEAS
    scripts = get_ch("📝｜script-ideas")
    if scripts:
        await scripts.send("""
# 📝 Script Idea Bank

**High-Performing Niches:**

**1. Reddit Stories**
- "AITA for telling my boss the truth?"
- "My neighbor did something unthinkable"
- "I found something disturbing in my attic"

**2. Finance/Money**
- "3 side hustles that saved me from debt"
- "Why I'll never work a 9-5 again"
- "Passive income streams that actually work"

**3. Relationship/Drama**
- "Caught my partner doing this (storytime)"
- "Red flags I ignored that cost me everything"
- "Crazy first date stories"

**4. Disturbing Facts**
- "Facts that will ruin your day"
- "Dark truths about [industry]"
- "Things they don't want you to know"

**Drop your script ideas here!** Community votes on best ones.
        """)
        print("✅ Script ideas posted")
        await asyncio.sleep(1)
    
    # MONETIZATION
    money = get_ch("💡｜money-ideas")
    if money:
        await money.send("""
# 💰 Income Streams Roadmap

**Phase 1: $0-$100**
- Amazon Associates (easiest approval)
- Audible affiliate (high commission on free trials)
- TikTok Creator Fund (need 10K followers)

**Phase 2: $100-$500**
- Brand deals (reach out at 5K+ followers)
- Digital products (templates, guides)
- Consulting calls

**Phase 3: $500-$1,000**
- YouTube Partner Program
- Sponsored content series
- Affiliate stacks (multiple programs)

**Phase 4: $1,000+**
- Patreon/community memberships
- Courses
- Agency services
- Automated revenue systems

**Current Focus:** Get everyone to Phase 1 first. Share what works!
        """)
        print("✅ Monetization roadmap posted")
        await asyncio.sleep(1)
    
    # GENERAL CHAT - Welcome message
    general = get_ch("💬｜general-chat")
    if general:
        await general.send("🎉 Server is live! Welcome to AI Income HQ! Drop a 👋 to say hi!")
        print("✅ General chat seeded")
        await asyncio.sleep(1)
    
    # INTRODUCTIONS
    intros = get_ch("🤝｜introductions")
    if intros:
        await intros.send("""
# 👋 Introduce Yourself!

**Copy this template:**

Name: [Your name]
Location: [City/Timezone]
Current Status: [Student / 9-5 / unemployed / etc.]
Goal: [First $100? Quit job? Build empire?]
Niche: [What content you want to make]
Experience: [Complete beginner? Some experience?]
Fun Fact: [Something interesting about you]

**Example:**
Name: Fields
Location: Illinois (CST)
Current Status: Amazon + School
Goal: First $1,000/month passive
Niche: Reddit stories + Finance
Experience: Beginner, learning AI automation
Fun Fact: Building this server during work breaks

**Drop yours below!** Let's get to know each other.
        """)
        print("✅ Introductions template posted")
    
    print("\n🎉 SERVER POPULATED! Check it out!")
    await client.close()

print("🔌 Populating content...")
client.run(TOKEN)
