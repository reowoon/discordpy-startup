import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='&')
token = os.environ['DISCORD_BOT_TOKEN']

#ステータス
@bot.event
async def on_ready():
    activity = discord.Activity(name='&help | Pornhub',activity=streaming)
    await bot.change_presence(activity=activity)
      
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def rrr(ctx, arg1, arg2):
    cha = bot.get_channel(int(arg1))
    await cha.send(arg2)


bot.run(token)
