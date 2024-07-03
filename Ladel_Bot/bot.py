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
            await ladel_commands.rotate_random_color_role(
                interaction.guild, interaction.user
            )
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

        @self.tree.command(
            name="rock_paper_scissors",
            description="Play rock-paper-scissors with me!",
            guild=self.TMP_GUILD,
        )
        async def rock_paper_scissors(interaction: discord.Interaction, choice: str):
            await ladel_commands.rock_paper_scissors(interaction, choice)

        @self.tree.command(
            name="roll_dice",
            description="Roll some dice formatted '#d#', default rolls 1d6",
            guild=self.TMP_GUILD,
        )
        async def roll_dice(interaction: discord.Interaction, dice: str):
            await ladel_commands.roll_dice(interaction, dice)

    async def on_ready(self):
        print(f"{self.user} syncing command tree...")
        await self.tree.sync(guild=self.TMP_GUILD)
        print(f"{self.user} starting tasks...")
        self.start_tasks()
        print(f"{self.user} ready")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        await ladel_commands.respond_not_valid_message(message)
        await ladel_commands.colon_three(message)

    def start_tasks(self):
        tasks = [
            self.task_rotate_random_color_role,
        ]
        for task in tasks:
            task.start()

    @tasks.loop(minutes=15)
    async def task_rotate_random_color_role(self):
        await ladel_commands.rotate_random_color_role(
            self.get_guild(environment.GUILD_ID)
        )
