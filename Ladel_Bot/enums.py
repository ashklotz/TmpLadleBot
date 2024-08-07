from enum import Enum, auto, StrEnum


class GreetingRarity:
    COMMON = 100
    UNCOMMON = 80
    RARE = 50
    LEGENDARY = 20
    UNIQUE = 5


class NotValidStr(StrEnum):
    nv_1 = "i'm not valid"
    nv_2 = "i am not valid"


class GuildConfig(StrEnum):
    # CHANNELS
    log_channel = auto()

    # ROLES
    color_rotation_role = auto()
    moderator_role = auto()
    unverified_role = auto()
    verified_role = auto()
    welcome_channel = auto()
