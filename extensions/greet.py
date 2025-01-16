from random import choice
from typing import Optional, Tuple

from discord import Member, TextChannel
from discord.ext.commands import Cog, Bot, Context
from discord.ext.commands import hybrid_command


GREETINGS: Tuple[str] = (
    "What's up?",
    "Hello",
    "Howdy",
    "Hiya",
    "Hey"
)


class GreetingCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_member_join(self, member: Member) -> None:
        # if member.bot:  return

        channels = self.bot.permissive_channels(member.guild)
        channel: TextChannel | None

        try:
            channel = channels[0]
        except IndexError:
            # TODO:
            # Handle a Guild not having any Text Channels
            # Most likely it would just be an error in logs
            # which will be implemented, and the logging, after this commit
            pass

        await channel.send(f"Welcome to the server, {member.mention}")

    @hybrid_command()
    async def greet(self, ctx: Context, person: Optional[Member] = None) -> None:
        if not person:  person = ctx.author
        greeting = choice(GREETINGS)

        await ctx.send(f"{greeting} {person.name}")


async def setup(bot: Bot) -> None:
    await bot.add_cog(GreetingCog(bot))
