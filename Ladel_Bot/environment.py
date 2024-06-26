import os

DISCORD_KEY = os.environ.get("DISCORD_KEY")
try:
    GUILD_ID = int(os.environ.get("GUILD_ID"))
except TypeError:
    GUILD_ID = None
try:
    ASH_ID = int(os.environ.get("ASH_ID"))
except TypeError:
    ASH_ID = None
try:
    TAY_ID = int(os.environ.get("TAY_ID"))
except TypeError:
    TAY_ID = None
