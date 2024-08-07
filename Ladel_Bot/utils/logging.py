import discord
from sqlalchemy import select
from sqlalchemy.orm import Session
from Ladel_Bot import environment, enums
from Ladel_Bot.models import GuildConfig


def log_action(guild_id: int, messsage: str):
    guild: discord.Guild = None

    with Session(environment.DB_ENGINE) as session:
        statement = (
            select(GuildConfig)
            .where(GuildConfig.guild_id == guild_id)
            .where(GuildConfig.config_type == enums.GuildConfig.log_channel)
        )
        config = session.scalar(statement)
        if not config:
            pass

        log_channel_id = config.config_id
        # TODO the rest
