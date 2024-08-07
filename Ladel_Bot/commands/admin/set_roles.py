import discord
import enums, utils


async def set_mod_role(interaction: discord.Interaction, role: discord.Role):
    utils.update_role(interaction.guild.id, role.id, enums.GuildConfig.moderator_role)
    message = f"moderator role set to {role.name}"
    await utils.log_action(interaction.guild, message)
    await interaction.response.send_message(message, ephemeral=True)


async def set_random_color_role(interaction: discord.Interaction, role: discord.Role):
    utils.update_role(
        interaction.guild.id, role.id, enums.GuildConfig.color_rotation_role
    )
    message = f"color rotation role set to {role.name}"
    await utils.log_action(interaction.guild, message)
    await interaction.response.send_message(message, ephemeral=True)


async def set_unverified_role(interaction: discord.Interaction, role: discord.Role):
    utils.update_role(interaction.guild.id, role.id, enums.GuildConfig.unverified_role)
    message = f"unverified role set to {role.name}"
    await utils.log_action(interaction.guild, message)
    await interaction.response.send_message(message, ephemeral=True)


async def set_verified_role(interaction: discord.Interaction, role: discord.Role):
    utils.update_role(interaction.guild.id, role.id, enums.GuildConfig.verified_role)
    message = f"verified role set to {role.name}"
    await utils.log_action(interaction.guild, message)
    await interaction.response.send_message(message, ephemeral=True)
