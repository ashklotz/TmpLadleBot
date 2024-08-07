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


def update_role(guild_id, role_id, config_type):
    with Session(environment.DB_ENGINE) as session:
        statement = (
            select(GuildConfig)
            .where(GuildConfig.guild_id == guild_id)
            .where(GuildConfig.config_type == config_type)
        )
        config = session.scalar(statement)
        if not config:
            config = GuildConfig(
                guild_id=guild_id,
                config_type=config_type,
                config_id=role_id,
            )
        else:
            config.config_id = role_id
        session.add(config)
        session.commit()
