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
    channel = bot.get_channel(417245684656373768)
    await bot.change_presence(activity=activity)
    await channel.send('おはようございます！')
      
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#話す
@bot.command()
async def rrr(ctx, arg1, arg2):
    if ctx.author.id != 540536805099831299:
        await ctx.send('君には使えないよ！')
        return 
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
    await ctx.send(arg.mention+'が脱落！')
    
    
#ニックネーム変更
@bot.command()
async def nick(ctx, arg1:discord.Member, *, arg2):
    if ctx.author.roles.id in 777023800746573835:
        await ctx.send('あなたは改名拒否をしているため変えられません！')
        return
    if arg1.roles.id in 777023800746573835:
        await ctx.send('改名拒否されているため変えられません！')
        return
    if arg1.id == 714776261410553907:
        await ctx.send('やめてください！')
        return
    if arg1.id == 540536805099831299:
        await ctx.send('れおうーん様は変えられません！')
        return
    if arg1.roles.id in 696706523560280084:
        await ctx.send('BOTの名前は変えられません！')
        return
    await ctx.send(arg1.name+' の名前を '+arg2+' にしました！')
    await arg1.edit(nick=arg2)

#test
@bot.command()
async def test1(ctx):
    if ctx.author.roles in '701440228476584047':
        await ctx.send('done')

#変更拒否
@bot.command()
async def nick_b(ctx):
    role = guild.get_role(777023800746573835)
    if ctx.author.roles.id in 777023800746573835:
        await ctx.author.remove_roles(role)
        await ctx.send('改名拒否役職を外しました！')
    else:
        await ctx.author.add_roles(role)
        await ctx.send('改名拒否役職を与えました！')
        return


    
#ステータス
@bot.command()
async def stats(ctx, arg):
    activity = discord.Activity(name='&help | '+arg,type=discord.ActivityType.streaming)
    await bot.change_presence(activity=activity)
    await ctx.send('ステータスを '+arg+'を配信中 にしました！')
        
        
bot.run(token)
