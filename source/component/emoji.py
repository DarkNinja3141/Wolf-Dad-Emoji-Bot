import datetime
import json
import urllib.request
from typing import Optional, Union

from discord import Emoji, TextChannel, Embed, User
from discord.ext import commands
from discord.ext.commands import Bot, Context


class EmojiEmbed(Embed):
    def __init__(self, emoji: Emoji,
                 user: Optional[User] = None,
                 source: Optional[str] = None,
                 timestamp: Union[datetime.datetime, Embed] = Embed.Empty):
        title = r"\:" + emoji.name + r"\:"
        super().__init__(title=title, timestamp=timestamp)
        super().set_thumbnail(url=emoji.url)
        if user:
            super().add_field(name="Suggested by:", value=user.mention, inline=True)
        if source:
            with urllib.request.urlopen("http://www.housepetscomic.com/wp-json/oembed/1.0/embed?url=" + source) as http:
                response = json.load(fp=http)
            super().add_field(name="Comic source:",
                              value="[{text}]({url})".format(text=response["title"], url=source),
                              inline=True)


class Timestamp(commands.Converter):
    async def convert(self, ctx, argument: str):
        if argument == "now":
            return datetime.datetime.utcnow()
        return datetime.datetime.fromisoformat(argument)


class EmojiCommands(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(name="emoji", aliases=["e"], pass_context=True)
    async def cmd_emoji(self, ctx: Context,
                        emoji: Emoji,
                        channel: Optional[TextChannel],
                        source: Optional[str],
                        user: Optional[User],
                        time_str: Optional[Timestamp]):
        if not channel:
            channel = ctx.channel
        timestamp: Union[datetime, Embed] = time_str if time_str else Embed.Empty
        await channel.send(embed=EmojiEmbed(emoji, user=user, source=source, timestamp=timestamp))
