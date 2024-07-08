from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class GuildConfig(Base):
    __tablename__ = "guild_config"

    id: Mapped[int] = mapped_column(primary_key=True)
    guild_id: Mapped[int]
    log_channel_id: Mapped[int]
