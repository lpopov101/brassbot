from enum import Enum

from .industries import IndustryType
from .location import Location


class CardType(Enum):
    INDUSTRY = 1
    LOCATION = 2


class Card:
    def __init__(
        self,
        card_type: CardType,
        location: Location = None,
        industries: list[IndustryType] = None,
        wild=False,
    ):
        self.card_type = card_type
        self.location = location
        self.industries = industries
        self.wild = wild
