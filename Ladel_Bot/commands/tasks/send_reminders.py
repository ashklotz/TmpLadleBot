from discord.ext.commands import Bot
import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

import environment
from models import Reminder


async def send_reminders(bot: Bot):
    with Session(environment.DB_ENGINE) as session:
        statement = (
            select(Reminder)
            .where(Reminder.complete == False)
            .where(Reminder.remind_date <= datetime.datetime.now())
        )
        reminders = session.scalars(statement)
        for reminder in reminders:
            reminder: Reminder
            channel = bot.get_channel(int(reminder.channel_id))
            if not channel:
                channel = await bot.fetch_channel(int(reminder.channel_id))
            user = bot.get_user(int(reminder.user_id))
            if not user:
                user = await bot.fetch_user(int(reminder.user_id))
            await channel.send(f"{user.mention} don't forget!\n{reminder.message}")
            reminder.complete = True
            print(f"sent {user.display_name} reminder: {reminder.message}")

        session.commit()
