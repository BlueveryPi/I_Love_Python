import discord, asyncio
from discord.ext import commands

token="???"
game=discord.Game("")
intents = discord.Intents().all()
bot=commands.Bot(command_prefix="<><<><><><<<<>", status=discord.Status.online, activity=game, intents=intents)
I="556773669737857025"

@bot.event
async def on_ready():
    global I
    trigger=False
    servers=bot.guilds
    ilp=await bot.fetch_user(int(I))
    for server in servers:
        for member in server.members:
            if member==ilp:
                if trigger==False:
                    await bot.change_presence(activity=member.activity, status=member.status)
                    trigger=True
                await server.me.edit(nick=member.nick)
                
    print("ready")

@bot.event
async def on_message(ctx):
    global I
    if ctx.author==await bot.fetch_user(int(I)):
        await ctx.channel.send(ctx.content)

@bot.event
async def on_typing(channel, user, when):
    global I
    if user==await bot.fetch_user(int(I)):
        async with channel.typing():
            await asyncio.sleep(0.01)

@bot.event
async def on_member_update(before, after):
    global I
    if str(before.id)==str(I):
        await bot.change_presence(activity=after.activity, status=after.status)

bot.run(token)
