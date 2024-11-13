from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy
import datetime

from . import Base


class Leaderboard(Base):
    __tablename__ = "leaderboard"

    id: Mapped[int] = mapped_column(primary_key=True)
    guild_id: Mapped[int] = mapped_column(sqlalchemy.BigInteger)
    name: Mapped[str]
    positive_point_message: Mapped[str]
    negative_point_message: Mapped[str]
    date_created: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now(datetime.timezone.utc)
    )


class LeaderboardUser(Base):
    __tablename__ = "leaderboard_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    leaderboard_id: Mapped[int]
    user_id: Mapped[int] = mapped_column(sqlalchemy.BigInteger)
    points: Mapped[int] = mapped_column(sqlalchemy.BigInteger)
    date_created: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now(datetime.timezone.utc)
    )
