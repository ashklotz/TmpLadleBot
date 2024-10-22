from sqlalchemy import select
from sqlalchemy.orm import Session
import discord
import enums, utils, environment
from models import ChannelConfig, RoleConfig, MessageConfig


async def set_role(
    interaction: discord.Interaction,
    role_type: enums.RoleConfig,
    role: discord.Role,
):
    with Session(environment.DB_ENGINE) as session:
        statement = (
            select(RoleConfig)
            .where(RoleConfig.guild_id == interaction.guild.id)
            .where(RoleConfig.config_type == role_type)
        )
        config = session.scalar(statement)
        if not config:
            config = RoleConfig(
                guild_id=interaction.guild.id,
                config_type=role_type,
                role_id=role.id,
            )
        else:
            config.role_id = role.id
        session.add(config)
        session.commit()

    message = f"{interaction.user.name} updated {role_type.value} to {role.name}"
    await utils.log_action(interaction.guild, message)
    await interaction.response.send_message(message, ephemeral=True)


async def set_channel(
    interaction: discord.Interaction,
    channel_type: enums.ChannelConfig,
    channel: discord.TextChannel,
):
    with Session(environment.DB_ENGINE) as session:
        statement = (
            select(ChannelConfig)
            .where(ChannelConfig.guild_id == interaction.guild.id)
            .where(ChannelConfig.config_type == channel_type)
        )
        config = session.scalar(statement)
        if not config:
            config = ChannelConfig(
                guild_id=interaction.guild.id,
                config_type=channel_type,
                channel_id=channel.id,
            )
        else:
            config.channel_id = channel.id
        session.add(config)
        session.commit()

    message = f"{interaction.user.name} updated {channel_type.value} to {channel.name}"
    await utils.log_action(interaction.guild, message)
    await interaction.response.send_message(message, ephemeral=True)


async def set_message(
    interaction: discord.Interaction,
    message_type: enums.MessageConfig,
    message: str,
):
    with Session(environment.DB_ENGINE) as session:
        statement = (
            select(MessageConfig)
            .where(MessageConfig.guild_id == interaction.guild.id)
            .where(MessageConfig.config_type == message_type)
        )
        config = session.scalar(statement)
        if not config:
            config = MessageConfig(
                guild_id=interaction.guild.id,
                config_type=message_type,
                message=message,
            )
        else:
            config.message = message
        session.add(config)
        session.commit()

    log_message = f"{interaction.user.name} updated {message_type.value} to `{message}`"
    await utils.log_action(interaction.guild, log_message)
    await interaction.response.send_message(log_message, ephemeral=True)
