import datetime

from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class Reminder(Base):
    __tablename__ = "reminder"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    remind_date: Mapped[datetime.datetime]
    message: Mapped[str]
    complete: Mapped[bool] = False
