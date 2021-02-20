import discord
from discord.ext import commands
import os
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
    await ctx.send(arg.mention+'を出禁にしました！')



#ステータス変更
@bot.command()
async def stats(ctx, arg):
    if ctx.author.id == 275574408372944897:
        arg1 = arg.replace('影','禿').replace('か','は').replace('カ','ハ').replace('k','h').replace('K','H').replace('Ｋ','Ｈ').replace('ｋ','ｈ')
        activity = discord.Activity(name='&help | '+arg1,type=discord.ActivityType.streaming)
        await bot.change_presence(activity=activity)
        await ctx.send('ステータスを '+arg1+'を配信中 にしました！')
    activity = discord.Activity(name='&help | '+arg,type=discord.ActivityType.streaming)
    await bot.change_presence(activity=activity)
    await ctx.send('ステータスを '+arg+'を配信中 にしました！')
        
#上級VC変更
@bot.command()
async def cname(ctx, arg):
    if ctx.author in guild.member.premium_subscribers:
    channel = bot.get_channel(801398685828382751)
        await channel.edit(name=arg)
        await ctx.send('固定チャンネル名を'+arg+'にしました！')
    else:
        await ctx.send('君には使えないよ！')

        
bot.run(token)
