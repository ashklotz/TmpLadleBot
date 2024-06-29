import random

import discord
from discord.ext import tasks, commands

import commands as ladel_commands, environment


class LadelBot(commands.Bot):
    TMP_GUILD = discord.Object(id=environment.GUILD_ID)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        @self.tree.command(
            name="change_color",
            description="Manually changes the color of 'Random Color' role",
            guild=self.TMP_GUILD,
        )
        async def rotate_random_color_role(interaction: discord.Interaction):
            print(f"{interaction.user.display_name} updated Random Color")
            await ladel_commands.rotate_random_color_role(interaction.guild, True)
            await interaction.response.send_message("Color changed!", ephemeral=True)

        @self.tree.command(
            name="get_greeted",
            description="Sends a random greeting to another user!",
            guild=self.TMP_GUILD,
        )
        async def respond_greeting(
            interaction: discord.Interaction, user: discord.User = None
        ):
            await ladel_commands.respond_greeting(interaction, user)

    async def on_ready(self):
        await self.tree.sync(guild=self.TMP_GUILD)
        print(f"{self.user} ready")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

    @tasks.loop(seconds=30)  # task runs every 45 mins
    async def task_rotate_random_color_role(self):
        print("task_rotate_random_color_role running")
        await ladel_commands.rotate_random_color_role(self)
