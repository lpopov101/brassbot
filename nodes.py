from dataclasses import dataclass, field
from enum import Enum

from .eras import Era
from .industries import Industry, IndustryType
from .location import Location
from .merchant_tile import MerchantTile


@dataclass
class CityNodeIndustrySlot:
    supported_industry_types: list[IndustryType]
    cur_industry: Industry = None


@dataclass
class MerchantNodeTileSlot:
    merchant_tile: MerchantTile
    beer_avaiable: bool


@dataclass
class LocationNode:
    location: Location


@dataclass
class CityNode(LocationNode):
    industry_slots: list[CityNodeIndustrySlot] = field(compare=False)


class MerchantNodeBonusType(Enum):
    FIVE_POUNDS = 1
    THREE_VP = 2
    FOUR_VP = 3
    TWO_INCOME = 4
    DEVELOP = 5


@dataclass
class MerchantNode(LocationNode):
    merchant_tile_slots: list[MerchantNodeTileSlot] = field(compare=False)
    bonus_type: MerchantNodeBonusType = field(compare=False)


@dataclass
class ConnectorNode:
    connected_locations: set[Location]
    eras: set[Era] = field(compare=False)
    player_id: int = field(compare=False, default=None)
