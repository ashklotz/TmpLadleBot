import discord
import datetime
from sqlalchemy.orm import Session
import environment
from models import Reminder


async def set_reminder(interaction: discord.Interaction, hours: float, message: str):
    if "@everyone" in message:
        await interaction.response.send_message(
            f"Sorry, you can't use @everyone", ephemeral=True
        )
        return
    with Session(environment.DB_ENGINE) as session:
        reminder = Reminder(
            user_id=interaction.user.id,
            channel_id=interaction.channel_id,
            remind_date=datetime.datetime.now() + datetime.timedelta(hours=hours),
            message=message,
        )
        session.add(reminder)
        session.commit()
    await interaction.response.send_message(
        f"I'll remind you in {hours} hours to {message}", ephemeral=True
    )
