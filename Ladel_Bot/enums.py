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


class RoleConfig(StrEnum):
    color_rotation_role = auto()
    moderator_role = auto()
    unverified_role = auto()
    verified_role = auto()


class ChannelConfig(StrEnum):
    log_channel = auto()
    welcome_channel = auto()


class MessageConfig(StrEnum):
    welcome_message = auto()
    verified_message = auto()
