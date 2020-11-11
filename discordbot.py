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
    if arg1.id == 714776261410553907:
        await ctx.send('やめてください！')
        return
    if arg1.id == 540536805099831299:
        await ctx.send('変えられません！')
        return
    await ctx.send(arg1.name+' の名前を '+arg2+' にしました！')
    await arg1.edit(nick=arg2)

#ニックネーム変更拒否
@bot.command()
async def nick_b(ctx):
    channel = bot.get_channel(775983131399946241)
    await ctx.send('nickコマンドをブロックしました！')
    await channel.send(str(ctx.author.id))

    
    
    
#ステータス
@bot.command()
async def stats(ctx, arg):
    activity = discord.Activity(name='&help | '+arg,type=discord.ActivityType.streaming)
    await bot.change_presence(activity=activity)
    await ctx.send('ステータスを '+arg+'を配信中 にしました！')

#メッセージを取得した時に実行される
@bot.event
async def on_message(message): 

    #Botのメッセージは除外
    if message.author.bot:
        return

    #条件に当てはまるメッセージかチェックし正しい場合は返す
    def check(msg):
        return msg.author == message.author

    #/getとチャンネル上に打ち込むとBotが反応を示す
    if message.content.startswith("/get"):

        #/getと打ち込まれたチャンネル上に下記の文章を出力
        await message.channel.send("こんにちは！保存したいメッセージを入力してね！")
    
        #ユーザーからのメッセージを待つ
        wait_message = await client.wait_for("message", check=check)

        #メッセージを打ち込まれたのを確認すると下記の文章を出力
        await message.channel.send("保存したメッセージはこちらになるよ！")

        #取得したメッセージを書き込まれたチャンネルへ送信
        await message.channel.send(wait_message.content)
        
        
bot.run(token)
