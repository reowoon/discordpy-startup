import random

import discord
from discord.ext import commands

from .general import (
    ANDROMEDA_ID,
    chaos_authorize_message,
    piece_authorize_message,
    authorize_message_channel,
    chaos_roles_id,
    piece_roles_id,
    chaos_channel,
    piece_channel
)


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
        await member.add_roles(*self.piece_roles)
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
