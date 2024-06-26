import random
import discord

import environment


async def respond_greeting(interaction: discord.Interaction):
    greetings = [
        "Hello!",
    ]
    greeting_index = random.randint(0, len(greetings) - 1)
    greeting = greetings[greeting_index]
    user_id = interaction.user.id
    if user_id in {
        environment.ASH_ID,
        environment.TAY_ID,
    }:
        greeting = "Greetings, oh high and mighty overlord"
    await interaction.response.send_message(greeting)
