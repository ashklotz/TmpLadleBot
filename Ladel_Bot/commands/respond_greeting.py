import random
import discord
import enums

import environment


async def respond_greeting(interaction: discord.Interaction, user: discord.User):
    user_mention_str = f" {user.mention}" if user else ""
    greetings = {
        f"Hello{user_mention_str}!": enums.GreetingRarity.COMMON,
        f"Hey there{user_mention_str}": enums.GreetingRarity.COMMON,
        f"Hiya{user_mention_str}": enums.GreetingRarity.COMMON,
        f"Heyo{user_mention_str}": enums.GreetingRarity.COMMON,
        f"Hello{user_mention_str} fren :3": enums.GreetingRarity.COMMON,
        f"How is your :bee:{user_mention_str}?": enums.GreetingRarity.COMMON,
        f"GOOD MORNING{user_mention_str}!": enums.GreetingRarity.UNCOMMON,
        f"Hey there cutie patootie{user_mention_str}": enums.GreetingRarity.UNCOMMON,
        f"OMG HELLO{user_mention_str} FREN!!": enums.GreetingRarity.RARE,
        f"Hey{user_mention_str}, whats shakin bacon?": enums.GreetingRarity.RARE,
        f"you're awake{user_mention_str} :3": enums.GreetingRarity.RARE,
        f"Well hello there darlin{user_mention_str}, you're just in time for breakfast": enums.GreetingRarity.LEGENDARY,
        f"Haiiiiiiii{user_mention_str}!!!!! Hai hai hai hai haaaaai >w< haiiii{user_mention_str} ^w^ Haiiii hai hai hai{user_mention_str} hai hai hai haaaaaaiiiii :D How is the be of the you of the be of the you of the be of the you of the be of the you of the be of the you of the be of the you  of the be of the you of the be of the you of the be of the you of the be of the you of the be of the you of the be of the you of the be of the you of the be of the you of the be of the you of the be of the doings is{user_mention_str}? :3": enums.GreetingRarity.LEGENDARY,
    }
    if user and user.id in {
        environment.ASH_ID,
        environment.TAY_ID,
    }:
        greetings |= {
            f"Greetings{user_mention_str}, oh high and mighty overlord": 100,
        }
    greeting = random.choices(list(greetings.keys()), list(greetings.values()))[0]
    await interaction.response.send_message(greeting)
