from os import getenv
from pathlib import Path
from typing import Tuple

from discord import Intents, Object
from dotenv import load_dotenv


load_dotenv()


# Path to Bot's extensions
EXTENSIONS = Path("extensions")
# Path to Bot's assets
ASSETS = Path("assets")
# Both of the above declared Paths are relative to "config.py" file location

# Tuple of extensions to not have loaded
BLACKLIST: Tuple[str] = ("sample_cog")

# Gateway Privileged Intents
# used to throttle down on what events can a Bot receive and also aid in privacy of users
# 
# Make sure to consult the documentation and only subscribe to Intents you actually need
# at the time of development, and require when you need them
# 
# Docs for Intents:
# https://discord.com/developers/docs/events/gateway#gateway-intents
INTENTS = Intents.all()

# Ordinary message command prefix
PREFIX = "~"

# Guild ID of the Testing Server
GUILD_ID = int(getenv("GUILD_ID"))

# This is required for "Slash Commands" to update in the UI faster than with no testing Guild
TEST_GUILD = Object(id = GUILD_ID)
