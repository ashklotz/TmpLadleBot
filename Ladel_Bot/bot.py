import discord
from discord.ext import tasks, commands

import commands as ladel_commands, environment, utils, enums


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
            # TODO: also need to implement a way for custom/dynamic time setting rather than integers of hours
            await ladel_commands.general.set_reminder(interaction, hours, message)

        @self.tree.command(
            name="check_points",
            description="check points of yourself or someone else",
            guild=self.TMP_GUILD,
        )
        async def check_points(
            interaction: discord.Interaction, user: discord.Member = None
        ):
            member = user or interaction.user
            await ladel_commands.admin.check_points(interaction, member)

        @self.tree.command(
            name="top_points",
            description="check the top points users",
            guild=self.TMP_GUILD,
        )
        async def top_points(interaction: discord.Interaction):
            await ladel_commands.admin.top_points(interaction)

        ###############################
        # ADMIN COMMANDS
        ###############################
        @self.tree.command(
            name="configure_roles",
            description="Configure different roles in your server",
            guild=self.TMP_GUILD,
        )
        @discord.app_commands.choices(
            role_type=[
                discord.app_commands.Choice(name=s.value, value=s)
                for s in enums.RoleConfig
            ]
        )
        async def configure_roles(
            interaction: discord.Interaction,
            role_type: enums.RoleConfig,
            role: discord.Role,
        ):
            allow_moderator = role_type in [enums.RoleConfig.color_rotation_role]
            await utils.call_admin_command(
                ladel_commands.admin.set_role,
                interaction,
                interaction,
                role_type,
                role,
                allow_moderator_role=allow_moderator,
            )

        @self.tree.command(
            name="configure_channels",
            description="Configure different channels in your server",
            guild=self.TMP_GUILD,
        )
        @discord.app_commands.choices(
            channel_type=[
                discord.app_commands.Choice(name=s.value, value=s)
                for s in enums.ChannelConfig
            ]
        )
        async def configure_channels(
            interaction: discord.Interaction,
            channel_type: enums.ChannelConfig,
            channel: discord.TextChannel,
        ):
            allow_moderator = channel_type in [c.value for c in enums.ChannelConfig]
            await utils.call_admin_command(
                ladel_commands.admin.set_channel,
                interaction,
                interaction,
                channel_type,
                channel,
                allow_moderator_role=allow_moderator,
            )

        @self.tree.command(
            name="configure_messages",
            description="Configure different messages in your server. Include [user] to mention the user where applicable",
            guild=self.TMP_GUILD,
        )
        @discord.app_commands.choices(
            message_type=[
                discord.app_commands.Choice(name=s.value, value=s)
                for s in enums.MessageConfig
            ]
        )
        async def configure_messages(
            interaction: discord.Interaction,
            message_type: enums.MessageConfig,
            message: str,
        ):
            allow_moderator = message_type in [m.value for m in enums.MessageConfig]
            await utils.call_admin_command(
                ladel_commands.admin.set_message,
                interaction,
                interaction,
                message_type,
                message,
                allow_moderator_role=allow_moderator,
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

        @self.tree.command(
            name="create_leaderboard",
            description="create and name leaderboard",
            guild=self.TMP_GUILD,
        )
        async def create_leaderboard(
            interaction: discord.Interaction, leaderboard_name: str
        ):
            await utils.call_admin_command(
                ladel_commands.admin.create_leaderboard,
                interaction,
                interaction,
                leaderboard_name,
            )

        @self.tree.command(
            name="add_points",
            description="Add points to a user!",
            guild=self.TMP_GUILD,
        )
        async def add_points(
            interaction: discord.Interaction, member: discord.Member, points: int
        ):
            await utils.call_admin_command(
                ladel_commands.admin.add_points,
                interaction,
                interaction,
                member,
                points,
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
