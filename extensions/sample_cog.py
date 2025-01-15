from discord.ext.commands import Cog, Bot


class SampleCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot


async def setup(bot: Bot) -> None:
    await bot.add_cog(SampleCog(bot))
