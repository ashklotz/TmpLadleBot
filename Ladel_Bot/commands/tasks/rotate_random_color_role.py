import random
import discord

import utils


async def rotate_random_color_role(guild: discord.Guild, user: discord.User = None):
    role_name = "Random Color"
    role = discord.utils.get(guild.roles, name=role_name)
    if not role:
        print(f"no role found with name: {role_name}")
        return
    color = discord.Color(random.randint(0, 0xFFFFFF))
    await role.edit(color=color)
    log_message = (
        f"{user.name if user else 'Ladle'} updated {role_name} color to {color}"
    )
    print(log_message)
    await utils.log_action(guild, log_message)
