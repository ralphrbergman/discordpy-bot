from random import choice
from typing import Optional, Tuple

from discord import Member
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
    
    @hybrid_command()
    async def greet(self, ctx: Context, person: Optional[Member] = None) -> None:
        if not person:  person = ctx.author
        greeting = choice(GREETINGS)

        await ctx.send(f"{greeting} {person.name}")


async def setup(bot: Bot) -> None:
    await bot.add_cog(GreetingCog(bot))
