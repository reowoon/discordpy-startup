import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='a')
token = os.environ['DISCORD_BOT_TOKEN']

#ステータス
@bot.event
async def on_ready(): # botが起動したときに動作する処理
    await bot.change_presence(activity=discord.Game(name="&help | ロメダ最強！" , type=1))
    
@bot.commands
async def ranking(ctx)
    embed = 
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


bot.run(token)
