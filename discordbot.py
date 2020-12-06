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
    await ctx.send(arg.mention+'が脱落！')

#ニックネーム
@bot.command()
async def nick(ctx, arg1:discord.Member, *, arg2):
    if arg1.id == 714776261410553907:
        await ctx.send('やめてください！')
        return
    if arg1.id == 540536805099831299:
        await ctx.send('れおうーん様は変えられません！')
        return
    await ctx.send(arg1.name+' の名前を '+arg2+' にしました！')
    await arg1.edit(nick=arg2)
 

#ステータス
@bot.command()
async def stats(ctx, arg):
    activity = discord.Activity(name='&help | '+arg,type=discord.ActivityType.streaming)
    await bot.change_presence(activity=activity)
    await ctx.send('ステータスを '+arg+'を配信中 にしました！')
        
#鯖名
@bot.command()
async def sname(ctx,arg):
    await ctx.guild.edit(name='&ROMEDA-'+arg)
    await ctx.send('サーバー名を &ROMEDA-'+arg+' にしました！')
    
#チャンネル名
@bot.command()
async def cname(ctx,arg):
    channel1 = bot.get_channel(417245684656373768)
    channel2 = bot.get_channel(710474736169254952)
    await channel1.edit(name='┏💥┇'+arg+'-❶')
    await channel2.edit(name='┣💥┇'+arg+'-❷')
    await ctx.send('メインチャンネル名を 💥┇'+arg+' にしました!')
    
#VC
# テキストチャンネルの先頭につける文字
CHANNEL_PREFIX = "👂┇聞き専-"
# botたちのロール名 (botはテキストチャンネルに参加していてほしい)
BOT_ROLE_NAME = "manaho"


# ボイスチャンネル内の状態が変化したときに実行される
@bot.event
async def on_voice_state_update(member, before, after):
    # チャンネルを移動していない場合処理をしない
    if before.channel == after.channel:
        return
    if before.channel.id == 764709330213273612:
        return

    # チャンネルから退出してきた場合
    if before.channel is not None:
        # ボイスチャンネルに誰もいなくなった場合
        if len(before.channel.members) == 0:
            # テキストチャンネルを削除する
            await _channel_delete(member, before.channel)
        else:
            # テキストチャンネルから退出させる
            await _channel_exit(member, before.channel)

    # ボイスチャンネルに参加してきた場合
    if after.channel is not None:
        # 参加したチャンネルの1人目だった場合
        if len(after.channel.members) == 1:
            # テキストチャンネルを作成する
            await _channel_create(member, after.channel)
        else:
            # テキストチャンネルに参加させる
            await _channel_join(member, after.channel)

        # 入室時にメンションでチャンネルに案内
        await _channel_send_join(member, after.channel)

# テキストチャンネルを検索する関数
def _channel_find(voiceChannel):
    text_channels = voiceChannel.guild.text_channels
    channel_name = CHANNEL_PREFIX + str(voiceChannel.id)
    # 名前からチャンネルオブジェクトを取得する
    return discord.utils.get(text_channels, name=channel_name)


# チャンネル作成時の権限リストを返す
def _init_overwrites(guild, member):
    overwrites = {
        # デフォルトのユーザーはメッセージを見れないように
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        # 参加したメンバーは見ることができるように
        member: discord.PermissionOverwrite(read_messages=True)
    }

    bots_role = discord.utils.get(guild.roles, name=BOT_ROLE_NAME)
    if bots_role is not None:
        # Botもメッセージを見れるように
        bot_overwrite = {
            bots_role: discord.PermissionOverwrite(read_messages=True)
        }
        overwrites.update(bot_overwrite)

    return overwrites


# テキストチャンネルを作成する関数
async def _channel_create(member, voiceChannel):
    guild = voiceChannel.guild

    channel_name = CHANNEL_PREFIX + str(voiceChannel.id)
    overwrites = _init_overwrites(guild, member)
    category = voiceChannel.category

    # テキストチャンネルを作成
    await guild.create_text_channel(
        channel_name, overwrites=overwrites, category=category)


# テキストチャンネルを削除する関数
async def _channel_delete(member, voiceChannel):
    target = _channel_find(voiceChannel)
    if target is not None:
        await target.delete()


# テキストチャンネルに参加させる関数
async def _channel_join(member, voiceChannel):
    target = _channel_find(voiceChannel)
    if target is not None:
        overwrites = discord.PermissionOverwrite(read_messages=True)
        # 該当メンバーに読み取り権限を付与
        await target.set_permissions(member, overwrite=overwrites)


# テキストチャンネルから退出させる関数
async def _channel_exit(member, voiceChannel):
    target = _channel_find(voiceChannel)
    if target is not None:
        # 該当メンバーの読取権限を取り消し
        await target.set_permissions(member, overwrite=None)


# 入室時にメンションを飛ばして案内したい
async def _channel_send_join(member, voiceChannel):
    target = _channel_find(voiceChannel)
    if target is not None:
        await target.send(member.mention + "さん、聞き専はこちらです！")

        
bot.run(token)
