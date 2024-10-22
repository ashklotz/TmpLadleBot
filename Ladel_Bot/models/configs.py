from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy

from . import Base


class RoleConfig(Base):
    __tablename__ = "role_config"

    id: Mapped[int] = mapped_column(primary_key=True)
    guild_id: Mapped[int] = mapped_column(sqlalchemy.BigInteger)
    config_type: Mapped[str]  # enums.RoleConfig
    role_id: Mapped[int] = mapped_column(sqlalchemy.BigInteger)


class ChannelConfig(Base):
    __tablename__ = "channel_config"

    id: Mapped[int] = mapped_column(primary_key=True)
    guild_id: Mapped[int] = mapped_column(sqlalchemy.BigInteger)
    config_type: Mapped[str]  # enums.ChannelConfig
    channel_id: Mapped[int] = mapped_column(sqlalchemy.BigInteger)


class MessageConfig(Base):
    __tablename__ = "message_config"

    id: Mapped[int] = mapped_column(primary_key=True)
    guild_id: Mapped[int] = mapped_column(sqlalchemy.BigInteger)
    config_type: Mapped[str]  # enums.MessageConfig
    message: Mapped[str] = mapped_column(sqlalchemy.String)
