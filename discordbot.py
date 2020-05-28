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

# CHAOS・PIECEの選択通知

class Authorize(commands.Cog):

    def __init__(self, bot, name=None):
        self.bot: commands.Bot = bot
        self.name = name if name is not None else type(self).__name__

    def get_member(self, _id):
        return self.bot.get_guild(ANDROMEDA_ID).get_member(_id)

    @property
    def piece_roles(self):
        guild = self.bot.get_guild(ANDROMEDA_ID)
        return [guild.get_role(i) for i in piece_roles_id]

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if (
            payload.channel_id != authorize_message_channel
            or payload.message_id != piece_authorize_message
            or payload.emoji.name != "\U0001F33F"
        ):
            return
        member = self.get_member(payload.user_id)
        if self.piece_roles[0] in member.roles:
            return
        name = member.display_name
        des1 = format(name, member.guild.me.display_name)
        embed = discord.Embed(
            title='{0}さんが参加しました。'.format(name),
            colour=0x2E2EFE,
            description=(
                '```\n{3}\n```\n'
                '{0}！\n'
                '{1}。\n'
                '{2}'
            ).format(name, member.guild.member_count, member.created_at, des1)
        )
        embed.set_thumbnail(url=member.avatar_url)

        await self.bot.get_channel(piece_channel).send(embed=embed)


bot.run(token)
