import discord
from discord.ext import commands
import os
import traceback
from discord.ext import tasks
from datetime import datetime 
from discord import File
from PIL import Image, ImageDraw, ImageFont
import io

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
    
# 歓迎
@bot.command(name='canvas')
async def canvas(ctx, text=None):

    IMAGE_WIDTH = 600
    IMAGE_HEIGHT = 300

    # create empty image 600x300 
    image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT)) # RGB, RGBA (with alpha), L (grayscale), 1 (black & white)

    # or load existing image
    #image = Image.open('/home/furas/images/lenna.png')

    # create object for drawing
    draw = ImageDraw.Draw(image)

    # draw red rectangle with green outline from point (50,50) to point (550,250) #(600-50, 300-50)
    draw.rectangle([50, 50, IMAGE_WIDTH-50, IMAGE_HEIGHT-50], fill=(255,0,0), outline=(0,255,0))

    # draw text in center
    text = f'Hello {ctx.author.name}'

    font = ImageFont.truetype('Arial.ttf', 30)

    text_width, text_height = draw.textsize(text, font=font)
    x = (IMAGE_WIDTH - text_width)//2
    y = (IMAGE_HEIGHT - text_height)//2

    draw.text( (x, y), text, fill=(0,0,255), font=font)

    # create buffer
    buffer = io.BytesIO()

    # save PNG in buffer
    image.save(buffer, format='PNG')    

    # move to beginning of buffer so `send()` it will read from beginning
    buffer.seek(0) 

    # send image
    await ctx.send(file=File(buffer, 'myimage.png'))


    
loop.start()
bot.run(token)
