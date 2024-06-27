import discord
import environment
from bot import LadelBot


def on_fetch(request=None):
    intents = discord.Intents.default()
    intents.message_content = True
    bot = LadelBot(intents=intents, command_prefix="/")

    bot.run(environment.DISCORD_KEY)


on_fetch()
