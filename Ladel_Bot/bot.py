import discord
from discord.ext import tasks, commands

import commands as ladel_commands, environment, utils


class LadelBot(commands.Bot):
    TMP_GUILD = discord.Object(id=environment.GUILD_ID)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ###############################
        # FUN COMMANDS
        ###############################
        @self.tree.command(
            name="change_color",
            description="Manually changes the random color role",
            guild=self.TMP_GUILD,
        )
        async def rotate_random_color_role(interaction: discord.Interaction):
            await ladel_commands.tasks.rotate_random_color_role(
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
            await ladel_commands.general.respond_greeting(interaction, user)

        @self.tree.command(
            name="rock_paper_scissors",
            description="Play rock-paper-scissors with me!",
            guild=self.TMP_GUILD,
        )
        async def rock_paper_scissors(interaction: discord.Interaction, choice: str):
            await ladel_commands.general.rock_paper_scissors(interaction, choice)

        @self.tree.command(
            name="roll_dice",
            description="Roll some dice formatted '#d#', default rolls 1d6",
            guild=self.TMP_GUILD,
        )
        async def roll_dice(interaction: discord.Interaction, dice: str):
            await ladel_commands.general.roll_dice(interaction, dice)

        @self.tree.command(
            name="set_reminder",
            description="Set a reminder",
            guild=self.TMP_GUILD,
        )
        async def set_reminder(
            interaction: discord.Interaction, hours: float, message: str
        ):
            # TODO: This needs to suppress all mentions in the user entered message
            # maybe just remove `@` from the message?
            # TODO: also need to implement a way for custom/dynamic time setting rather than integers of hours
            await ladel_commands.general.set_reminder(interaction, hours, message)

        ###############################
        # ADMIN COMMANDS
        ###############################
        @self.tree.command(
            name="set_mod_role",
            description="Sets the role intended for server moderators",
            guild=self.TMP_GUILD,
        )
        async def set_mod_role(interaction: discord.Interaction, role: discord.Role):
            await utils.call_admin_command(
                ladel_commands.admin.set_mod_role, interaction, interaction, role
            )

        @self.tree.command(
            name="set_verified_role",
            description="Set the role intended for verified users",
            guild=self.TMP_GUILD,
        )
        async def set_verified_role(
            interaction: discord.Interaction, role: discord.Role
        ):
            await utils.call_admin_command(
                ladel_commands.admin.set_verified_role,
                interaction,
                interaction,
                role,
            )

        @self.tree.command(
            name="set_unverified_role",
            description="Set the role intended for unverified users",
            guild=self.TMP_GUILD,
        )
        async def set_unverified_role(
            interaction: discord.Interaction, role: discord.Role
        ):
            await utils.call_admin_command(
                ladel_commands.admin.set_unverified_role,
                interaction,
                interaction,
                role,
            )

        @self.tree.command(
            name="set_random_color_role",
            description="Sets the role intended for rotating random colors",
            guild=self.TMP_GUILD,
        )
        async def set_random_color_role(
            interaction: discord.Interaction, role: discord.Role
        ):
            await utils.call_admin_command(
                ladel_commands.admin.set_random_color_role,
                interaction,
                interaction,
                role,
            )

        @self.tree.command(
            name="set_log_channel",
            description="Sets the channel intended for logging actions",
            guild=self.TMP_GUILD,
        )
        async def set_log_channel(
            interaction: discord.Interaction, channel: discord.TextChannel
        ):
            await utils.call_admin_command(
                ladel_commands.admin.set_log_channel,
                interaction,
                interaction,
                channel,
            )

        @self.tree.command(
            name="verify_user",
            description="Verifies and allows a user into the rest of the server",
            guild=self.TMP_GUILD,
        )
        async def verify_user(interaction: discord.Interaction, member: discord.Member):
            await utils.call_admin_command(
                ladel_commands.admin.verify_user,
                interaction,
                interaction,
                member,
                allow_moderator_role=True,
            )

    async def on_ready(self):
        print(f"{self.user} syncing command tree...")
        await self.tree.sync(guild=self.TMP_GUILD)
        print(f"{self.user} starting tasks...")
        self.start_tasks()
        print(f"{self.user} ready")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        await ladel_commands.messages.respond_not_valid_message(message)
        await ladel_commands.messages.colon_three(message)

    def start_tasks(self):
        tasks = [
            self.task_rotate_random_color_role,
            self.task_send_reminders,
        ]
        for task in tasks:
            task.start()

    @tasks.loop(minutes=15)
    async def task_rotate_random_color_role(self):
        await ladel_commands.tasks.rotate_random_color_role(
            self.get_guild(environment.GUILD_ID)
        )

    @tasks.loop(minutes=5)
    async def task_send_reminders(self):
        await ladel_commands.tasks.send_reminders(self)
