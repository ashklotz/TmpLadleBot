import discord
from sqlalchemy import select
from sqlalchemy.orm import Session
import environment, enums
from models import GuildConfig


async def log_action(guild: discord.Guild, messsage: str):
    with Session(environment.DB_ENGINE) as session:
        statement = (
            select(GuildConfig)
            .where(GuildConfig.guild_id == guild.id)
            .where(GuildConfig.config_type == enums.GuildConfig.log_channel)
        )
        config = session.scalar(statement)
        if not config:
            return

        log_channel_id = config.config_id
        log_channel = guild.get_channel(log_channel_id)
        await log_channel.send(messsage)


def update_role(guild_id: int, role_id: int, config_type: enums.GuildConfig):
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


def update_channel(guild_id: int, channel_id: int, config_type: enums.GuildConfig):
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
                config_id=channel_id,
            )
        else:
            config.config_id = channel_id
        session.add(config)
        session.commit()


async def call_admin_command(command_func, interaction, *args):
    if not interaction.user.guild_permissions.administrator:
        return await interaction.response.send_message(
            "You do not have permission to use this command", ephemeral=True
        )
    await command_func(*args)
