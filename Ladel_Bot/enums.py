from enum import Enum


class GreetingRarity:
    COMMON = 100
    UNCOMMON = 80
    RARE = 50
    LEGENDARY = 20
    UNIQUE = 5


class NotValidStr(Enum):
    nv_1 = "i'm not valid"
    nv_2 = "i am not valid"
