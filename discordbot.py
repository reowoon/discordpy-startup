import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='&')
token = os.environ['DISCORD_BOT_TOKEN']

#ステータス
@bot.event
async def on_ready():
    activity = discord.Activity(name='&help | Pornhub',type=discord.ActivityType.streaming)
    await bot.change_presence(activity=activity)
      
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#話す
@bot.command()
async def rrr(ctx, arg1, arg2):
    cha = bot.get_channel(int(arg1))
    await cha.send(arg2)

#アウト
@bot.command()
async def out(ctx, arg : discord.Member):
    if message.author.id != 540536805099831299:
        return
    else:
    role = guild.get_role(769452198588579850)  
    await arg.add_roles(role)
    await ctx.send(arg.mention+'が脱落！乙！')
    
bot.run(token)
