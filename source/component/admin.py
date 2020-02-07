import json
from typing import Optional

from discord import Embed, TextChannel
from discord.ext import commands
from discord.ext.commands import Bot, Context


class AdminCommands(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    # Closes the bot. Can only be used by me.
    # noinspection PyUnusedLocal
    @commands.command(name='logout', pass_context=True)
    @commands.is_owner()
    async def logout(self, ctx: Context):
        print("Logging out")
        await self.bot.logout()
        # nothing past here is executed

    @commands.command(name="say", pass_context=True)
    @commands.is_owner()
    async def cmd_say(self, ctx: Context, channel: Optional[TextChannel], *, text: str = ""):
        if not channel:
            channel = ctx.channel
        await channel.send(text)

    @commands.command(name="embed", pass_context=True)
    @commands.is_owner()
    async def cmd_embed(self, ctx: Context, channel: Optional[TextChannel], *, text: str = ""):
        if not channel:
            channel = ctx.channel
        text = text[3:-3]
        try:
            embed_json: dict = json.loads(text)
            await channel.send(embed=Embed.from_dict(embed_json))
        except json.JSONDecodeError:
            await ctx.send("Error reading JSON")
