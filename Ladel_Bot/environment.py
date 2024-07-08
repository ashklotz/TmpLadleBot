import os

DBNAME = os.environ.get("DBNAME")
DBHOST = os.environ.get("DBHOST")
DBPORT = os.environ.get("DBPORT")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DISCORD_KEY = os.environ.get("DISCORD_KEY")
GUILD_ID = int(os.environ.get("GUILD_ID")) if os.environ.get("GUILD_ID") else None
ASH_ID = int(os.environ.get("ASH_ID")) if os.environ.get("ASH_ID") else None
TAY_ID = int(os.environ.get("TAY_ID")) if os.environ.get("TAY_ID") else None
