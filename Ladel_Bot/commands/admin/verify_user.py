import discord

from sqlalchemy import select
from sqlalchemy.orm import Session

import environment, enums
from models import RoleConfig


async def verify_user(interaction: discord.Interaction, member: discord.Member):
    with Session(environment.DB_ENGINE) as session:
        statement = (
            select(RoleConfig)
            .where(RoleConfig.guild_id == interaction.guild.id)
            .where(RoleConfig.config_type == enums.RoleConfig.unverified_role)
        )
        unverified_role_config = session.scalar(statement)
        statement = (
            select(RoleConfig)
            .where(RoleConfig.guild_id == interaction.guild.id)
            .where(RoleConfig.config_type == enums.RoleConfig.verified_role)
        )
        verified_role_config = session.scalar(statement)

        if unverified_role_config and verified_role_config:
            introduction_channel = None
            general_channel = None
            unverified_role = interaction.guild.get_role(unverified_role_config.role_id)
            verified_role = interaction.guild.get_role(verified_role_config.role_id)
            await member.remove_roles(unverified_role)
            await member.add_roles(verified_role)
            return await interaction.response.send_message(
                f"{member.mention} welcome to the server! {'Drop an introduction in ' + introduction_channel +' and start chatting in '+ general_channel if introduction_channel and general_channel else ''}"
            )
        else:
            return await interaction.response.send_message(
                "unverified or verified role not set, please have an administrator set these",
                ephemeral=True,
            )
