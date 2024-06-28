import random
import discord
import enums

import environment


async def respond_greeting(interaction: discord.Interaction, user: discord.User):
    user_mention_str = f" {user.mention}" if user else ""
    greetings = {
        f"Hello{user_mention_str}!": enums.GreetingRarity.COMMON,
        f"Hey there{user_mention_str}": enums.GreetingRarity.COMMON,
        f"How is your :bee:{user_mention_str}?": enums.GreetingRarity.UNCOMMON,
        f"Haiiiiiiii{user_mention_str}!!!!! Hai hai hai hai haaaaai >w< haiiii{user_mention_str} ^w^ Haiiii hai hai hai{user_mention_str} hai hai hai haaaaaaiiiii :D How is the be of the you of the be of the you of the be of the you of the be of the you of the be of the you of the be of the you  of the be of the you of the be of the you of the be of the you of the be of the you of the be of the you of the be of the you of the be of the you of the be of the you of the be of the you of the be of the doings is{user_mention_str}? :3": enums.GreetingRarity.LEGENDARY,
    }
    if user and user.id in {
        environment.ASH_ID,
        environment.TAY_ID,
    }:
        greetings |= {
            "Greetings, oh high and mighty overlord": 100,
        }
    greeting = random.choices(list(greetings.keys()), list(greetings.values()))
    await interaction.response.send_message(greeting)
