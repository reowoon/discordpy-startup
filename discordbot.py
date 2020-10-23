from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='&')
token = os.environ['DISCORD_BOT_TOKEN']

#ステータス
@bot.event
async def on_ready(): # botが起動したときに動作する処理
    await bot.change_presence(activity=discord.Game(name="&help | ロメダ最強！" , type=1))
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def rrr(ctx, arg1, arg2):
    channel = bot.get_channel(int(arg1))
    await channel.send(arg2)

bot.run(token)
