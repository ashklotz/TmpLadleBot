import discord

import enums, utils


async def set_log_channel(
    interaction: discord.Interaction, channel: discord.TextChannel
):
    utils.update_channel(
        interaction.guild.id, channel.id, enums.GuildConfig.log_channel
    )
    message = f"log channel set to {channel.name}"
    await utils.log_action(interaction.guild, message)
    await interaction.response.send_message(message, ephemeral=True)
