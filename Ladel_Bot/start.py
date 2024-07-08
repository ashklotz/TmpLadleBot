import discord

from bot import LadelBot
import environment


def start_bot(request=None):
    environment.start_engine()
    intents = discord.Intents.default()
    intents.message_content = True
    bot = LadelBot(intents=intents, command_prefix="/")

    bot.run(environment.DISCORD_KEY)


start_bot()
