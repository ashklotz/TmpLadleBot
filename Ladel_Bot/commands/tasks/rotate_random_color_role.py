import random
import discord

from sqlalchemy import select
from sqlalchemy.orm import Session

import utils, environment, enums
from models import GuildConfig


async def rotate_random_color_role(guild: discord.Guild, user: discord.User = None):
    with Session(environment.DB_ENGINE) as session:
        statement = (
            select(GuildConfig)
            .where(GuildConfig.guild_id == guild.id)
            .where(GuildConfig.config_type == enums.GuildConfig.color_rotation_role)
        )
        color_role_config = session.scalar(statement)
        if not color_role_config:
            return

        role = guild.get_role(color_role_config.config_id)
        color = discord.Color(random.randint(0, 0xFFFFFF))
        await role.edit(color=color)
        log_message = (
            f"{user.name if user else 'Ladle'} updated {role.name} color to {color}"
        )
        print(log_message)
        await utils.log_action(guild, log_message)
