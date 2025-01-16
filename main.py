from os import getenv
from typing import List

from discord import Guild, Permissions, TextChannel
from discord.ext.commands import Bot

from dotenv import load_dotenv

import config


load_dotenv()


TOKEN: str = getenv('TOKEN')


class DiscordBot(Bot):
    def permissive_channels(self, guild: Guild) -> List[TextChannel]:
        """
        Returns a List of TextChannel[s] the Bot can send messages in
        and read messages.
        """
        # Permissions needed for the Bot to fully access a Text Channel
        required = Permissions.none()
        required.read_message_history = True
        required.read_messages = True
        required.send_messages = True
        required.send_messages_in_threads = True

        channels = []
        me = guild.get_member(self.user.id)

        for channel in guild.text_channels:
            if channel.permissions_for(me) >= required:
                channels.append(channel)

        return channels

    async def setup_hook(self) -> None:
        tree = self.tree
        extensions = config.EXTENSIONS

        for file in extensions.glob("*"):
            name = file.stem

            # Ignore any file that isn't Python source
            if file.is_dir() or file.suffix != ".py":   continue

            if name in config.BLACKLIST:   continue

            cog_name = f"{extensions.name}.{name}"

            await self.load_extension(cog_name)

        # Sync application command tree
        # For now this happens to testing Guild only
        tree.copy_global_to(guild = config.TEST_GUILD)
        await tree.sync(guild = config.TEST_GUILD)


def main() -> None:
    bot = DiscordBot(
        command_prefix = config.PREFIX,
        # Disables the default provided ugly help command
        help_command = None,
        intents = config.INTENTS
    )
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
