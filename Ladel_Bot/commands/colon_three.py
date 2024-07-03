import discord, random


async def colon_three(message: discord.Message):
    if random.randint(0, 15) == 0:
        print(f"Sent :3 in response to {message.author.display_name}")
        await message.channel.send(":3")
