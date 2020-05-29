from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

ANDROMEDA_ID = 417245684656373766

# ボイスチャットと聞き専の対応関係
voice_text = {
    672045034316759092: 539722428671328257,
    698362136900141076: 589773641701392385,
    712976812237651969: 715429871907504195,
    672049440177258506: 534725550011318282,
    698361989889654864: 704586168439799809,
}

# カオス雑談
chaos_channel = 417245684656373768
# ピース雑談
piece_channel = 585739143229734913
# 認証時につくrole
chaos_roles_id = 712598474574528573
piece_role_id = 712598559224102922
# 認証のため、リアクションをつけるメッセージ（とチャンネル）
chaos_authorize_message = 713278562983215104
piece_authorize_message = 712638362896564305
authorize_message_channel = 712608688543891507

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

# 自己紹介テンプレート固定
introduction_channels = [559228832968736809,713312999577747527,713314722274869279]
@bot.events
global introduction_channels
async def on_message(message):
  if message.channel.id in introduction_channels:
    embed = discord.Embed(title='自己紹介テンプレート', description='【名前】\n【年齢】\n【趣味】\n【一言】', color=0x64ffff)
    await message.channel.send(embed=embed)
    
bot.run(token)
