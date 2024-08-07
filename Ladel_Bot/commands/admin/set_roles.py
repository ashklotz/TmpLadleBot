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
