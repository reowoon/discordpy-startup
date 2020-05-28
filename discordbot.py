from discord.ext import commands
import os
import traceback
from egg import ANDROMEDA_EGG

loop = asyncio.get_event_loop()
client = ANDROMEDA_EGG(loop=loop)
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

bot.run(token)
