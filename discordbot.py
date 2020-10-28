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
    
# 時報
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    minute = datetime.now().strftime('%M')
    hour = datetime.now().strftime('%-H')
    day = datetime.now().strftime('%-d')
    month = datetime.now().strftime('%-m')
    year = datetime.now().strftime('%Y')
    channel = bot.get_channel(417245684656373768)
    value = randint(0, 0xffffff)
    if month == '1' and day == '1' and hour == '0' and minute == '00':
        embed = discord.Embed(title=year+'年になりました！🎊',description='HAPPY NEW YEAR!今年もよろしくお願いします！',colour=value)
        embed.set_thumbnail(url='https://66.media.tumblr.com/4d768eea88b070685a5615f43e58cf52/a22fe641331c8834-e0/s640x960/53e850aca21fa632806b209c77bf0724c4f3c0d4.gif')
        await channel.send(embed)
    elif day == '1' and hour == '0' and minute == '00':
        images = [
            'https://stat.ameba.jp/user_images/20170724/22/kiyoharu-satou/81/3a/j/o0526039413989829466.jpg',
            'https://ure.pia.co.jp/mwimgs/a/0/-/img_a0b4613722bb705c1c7348c701fd2cc142038.jpg',
            'https://i1.wp.com/www.hatsune.info/wp-content/uploads/2020/04/EWAixS5UYAADW4d.jpg?fit=512%2C512&ssl=1',
            'https://r.r10s.jp/ran/img/1001/0004/562/153/116/183/10010004562153116183_1.jpg',
            'https://stat.ameba.jp/user_images/20120310/02/nigoki-eva/ee/bd/j/o0480032011842387297.jpg?caw=800',
            'https://images-na.ssl-images-amazon.com/images/I/61F5NSQW%2BrL._AC_SY445_.jpg',
            'https://cdn-ak.f.st-hatena.com/images/fotolife/c/cevid_cpp/20151031/20151031002242.jpg',
            'https://nijimen.net/wp-content/uploads/2020/04/samune-236.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Jack-o%27-Lantern_2003-10-31.jpg/225px-Jack-o%27-Lantern_2003-10-31.jpg',
            'https://www.midori-japan.co.jp/letter/wp-content/uploads/2019/09/jikou_11gatu_02.jpg',
            'https://i.pinimg.com/originals/4a/71/7f/4a717f87d47c7db44c887c25ccd48b82.jpg'
]
        messages = [
            '鬼は外ー福は内ー！みんなで鬼を退治しよう！鬼は…お前の後ろだぁ！！！',
            '別れの季節！その別れはきっとあなたを成長させます。さよおなら、ぶっ。',
            '新年度！新たな出会いが見つかりますように！(笑)',
            'こいのぼり立ててる家あんまり見なくなったよね。お前がこいのぼりになるんだよ！！！！WWWWWWWW',
            '雨、憂鬱な気分。僕の気分みたいだ。好きじゃない。',
            '千年に一度の彗星の夜、君の願いはかなう。劇場版ポケットモンスターアドバンスジェネレーション 七夜の願い星ジラーチ',
            '今年も夏がやってきた！佐久間「夏といえば、スイカと花火と女だろ。」',
            '月に代わってお仕置きよ！HIKAKINTV everyday HIKAKINTV everyday HIKAKINTV everyday',
            'トリックオアトリート！お菓子をくれなきゃ＊＊＊するぞ！',
            '紅葉！でも寒いし乾燥するし、gm',
            'やあ！サンタクロースだよ！金でも女でもなんでもくれてやる！ガハハハハハ！'
]
        number = month-2
        embed = discord.Embed(title=month+'月になりました📅', description=messages[number],colour=value)
        embed.set_thumbnail(url=images[number])
        await channel.send(embed)
    elif hour == '0' and minute == '00':
        embed = discord.Embed(title=month+'月'+day+'日になりました🕛',description='いい子は寝る時間だよ！おやすみなさい！',colour=value)
        embed.set_thumbnail(url='https://chigai-allguide.com/wp-content/uploads/2925381982.jpg')
        await channel.send(embed)
    elif hour == ['3','6','9','12','15','18','21'] and minute == '00':
        emojis = ['🕒','🕕','🕘','🕛','🕒','🕕','🕘']
        images = [
            'https://gimon-sukkiri.jp/wp-content/uploads/2018/06/midnight-e1529802941264.jpeg',
            'https://www.in-natural.style/wp/wp-content/uploads/2018/12/Fotolia_220032068_Subscription_Monthly_M.jpg',
            'https://intheearlyafternoon.link/wp-content/uploads/2017/02/20140920082919.jpg',
            'https://montecito.jp/wp-content/uploads/2018/10/sun-image.jpg',
            'https://blogimg.goo.ne.jp/user_image/3d/1a/46bc2bc64ed4149cccb5a1cd447d9879.jpg',
            'https://image.ganref.jp/photos/members/ma3aki/9d6ceb0ac36933ba2be31ab4c9df4be6_3.jpg',
            'https://s3-ap-northeast-1.amazonaws.com/static.lovely-media.jp/production/posts/eyecatches/000/001/249/original.jpg?1502080673'
        ]
        messages = [
            'こんな時間まで夜更かししてる子だーれだ！寝ないと…',
            'おはようございます！今日も目玉焼き食べて元気モーリモーリ！'
            '今日もいい天気～！鳥は歌い、花は咲き誇る！こんな日にはお前さんのような糞がきは地獄の業火に焼かれてもらう。',
            'こんにちは！お昼ご飯はオムレツにする？スクランブルエッグにする？それとも…ワ・タ・シ？',
            'おやつの時間だ！卵プリン食ぁべましょう！',
            'こんばんは！今日も一日お疲れ様！夜ご飯はもちろんオムライス！',
            'みんなで仲良くお風呂に入ろう！あったかいんだからぁ～！'
        ]
        number = hour/3-1
        embed = discord.Embed(title=hour+'時になりました'+emojis[number],description=messages[number],colour=value)
        embed.set_thumbnail(url=images[number])
        await channel.send(embed)  
    
loop.start()
bot.run(token)
