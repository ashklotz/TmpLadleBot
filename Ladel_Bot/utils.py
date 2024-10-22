import discord
from sqlalchemy import select
from sqlalchemy.orm import Session
import environment, enums
from models import RoleConfig, ChannelConfig


async def log_action(guild: discord.Guild, message: str, is_ladle: bool = False):
    print(message)
    if is_ladle:
        return

    with Session(environment.DB_ENGINE) as session:
        statement = (
            select(ChannelConfig)
            .where(ChannelConfig.guild_id == guild.id)
            .where(ChannelConfig.config_type == enums.ChannelConfig.log_channel)
        )
        config = session.scalar(statement)
        if not config:
            return

        log_channel_id = config.channel_id
        log_channel = guild.get_channel(log_channel_id)
        await log_channel.send(message)


async def call_admin_command(
    command_func, interaction: discord.Interaction, *args, allow_moderator_role=False
):
    is_moderator_user = False
    if allow_moderator_role:
        with Session(environment.DB_ENGINE) as session:
            statement = (
                select(RoleConfig)
                .where(RoleConfig.guild_id == interaction.guild_id)
                .where(RoleConfig.config_type == enums.RoleConfig.moderator_role)
            )
            config = session.scalar(statement)
            if config:
                role_id = config.role_id
                user_role_ids = [r.id for r in interaction.user.roles]
                is_moderator_user = role_id in user_role_ids
    if not (interaction.user.guild_permissions.administrator or is_moderator_user):
        return await interaction.response.send_message(
            "You do not have permission to use this command", ephemeral=True
        )
    await command_func(*args)
