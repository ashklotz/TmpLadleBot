import discord
import datetime
from sqlalchemy.orm import Session
import environment
from models import Reminder


async def set_reminder(interaction: discord.Interaction, hours: int, message: str):
    with Session(environment.DB_ENGINE) as session:
        reminder = Reminder(
            user_id=interaction.user.id,
            channel_id=interaction.channel_id,
            guild_id=interaction.guild_id,
            remind_date=datetime.datetime.now() + datetime.timedelta(hours=hours),
            message=message,
        )
        session.add(reminder)
        session.commit()
    await interaction.response.send_message(
        f"I'll remind you in {hours} hours to {message}", ephemeral=True
    )
