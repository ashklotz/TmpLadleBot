from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy
import datetime

from . import Base


class Leaderboard(Base):
    __tablename__ = "leaderboard"

    id: Mapped[int] = mapped_column(primary_key=True)
    server_id: Mapped[int]
    name: Mapped[str]
    date_created: Mapped[sqlalchemy.DateTime] = mapped_column(
        default=datetime.datetime.now(datetime.timezone.utc)
    )


class LeaderboardUser(Base):
    __tablename__ = "leaderboard_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    points: Mapped[int]
    date_created: Mapped[sqlalchemy.DateTime] = mapped_column(
        default=datetime.datetime.now(datetime.timezone.utc)
    )
