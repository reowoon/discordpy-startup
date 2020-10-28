import discord
from discord.ext import commands
import os
import traceback
from discord.ext import tasks
from datetime import datetime 

bot = commands.Bot(command_prefix='&')
token = os.environ['DISCORD_BOT_TOKEN']
guild = bot.get_guild(417245684656373766)

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
    channel = bot.get_channel(int(arg1))
    await channel.send(arg2)

#アウト
@bot.command()
async def out(ctx, arg:discord.Member):
    if ctx.author.id != 540536805099831299:
        await ctx.send('君には使えないよ！')
        return 
    role = guild.get_role(769452198588579850)  
    await arg.add_roles(role)
    await ctx.send(arg.mention+'が脱落！乙！')
    
#ニックネーム
@bot.command()
async def name(ctx, arg):
    await guild.members.edit(nick=arg)
    
# 時報

        
@tasks.loop(seconds=60)
async def loop():
    channel = bot.get_channel(417245684656373768)
    await channel.send('あ') 
    
loop.start()
bot.run(token)
