from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='&')
token = os.environ['DISCORD_BOT_TOKEN']

#ステータス
@bot.event
async def on_ready(): # botが起動したときに動作する処理
    await bot.change_presence(activity=discord.ActivityType.streaming(name="&help | Pornhub" , type=1))
      
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def rrr(ctx, arg1, arg2):
    cha = bot.get_channel(int(arg1))
    await cha.send(arg2)


bot.run(token)
