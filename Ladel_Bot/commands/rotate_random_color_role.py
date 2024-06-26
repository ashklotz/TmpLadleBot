import random
import discord


async def rotate_random_color_role(guild: discord.Guild, bypass_chance=False):
    if not bypass_chance and random.randint(0, 3) == 0:
        print("failed roll to change color")
        return
    role_name = "Random Color"
    role = discord.utils.get(guild.roles, name=role_name)
    if not role:
        print(f"no role found with name: {role_name}")
        return
    color = discord.Color(random.randint(0, 0xFFFFFF))
    print(f"updated {role_name} color to {color}")
    await role.edit(color=color)
