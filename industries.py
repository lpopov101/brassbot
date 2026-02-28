from dataclasses import dataclass
from enum import Enum

from .eras import Era


class IndustryType(Enum):
    COAL = 1
    IRON = 2
    BEER = 3
    COTTON = 4
    MANUFACTURED_GOODS = 5
    POTTERY = 6


@dataclass
class IndustryStats:
    money_cost: int
    coal_cost: int
    iron_cost: int
    income: int
    vp: int
    connection_vp: int
    beer_cost: int
    commodity_count: int
    no_develop: bool
    double_commodity_rail_era: bool
    era_only: Era | None


INDUSTRY_STATS = {
    (IndustryType.COAL, 1): IndustryStats(
        money_cost=5,
        coal_cost=0,
        iron_cost=0,
        income=4,
        vp=1,
        connection_vp=2,
        beer_cost=0,
        commodity_count=2,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=Era.CANAL,
    ),
    (IndustryType.COAL, 2): IndustryStats(
        money_cost=7,
        coal_cost=0,
        iron_cost=0,
        income=7,
        vp=2,
        connection_vp=1,
        beer_cost=0,
        commodity_count=3,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.COAL, 3): IndustryStats(
        money_cost=8,
        coal_cost=0,
        iron_cost=1,
        income=6,
        vp=3,
        connection_vp=1,
        beer_cost=0,
        commodity_count=4,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.COAL, 4): IndustryStats(
        money_cost=10,
        coal_cost=0,
        iron_cost=1,
        income=5,
        vp=4,
        connection_vp=1,
        beer_cost=0,
        commodity_count=5,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.IRON, 1): IndustryStats(
        money_cost=5,
        coal_cost=1,
        iron_cost=0,
        income=3,
        vp=3,
        connection_vp=1,
        beer_cost=0,
        commodity_count=4,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=Era.CANAL,
    ),
    (IndustryType.IRON, 2): IndustryStats(
        money_cost=7,
        coal_cost=1,
        iron_cost=0,
        vp=5,
        income=3,
        connection_vp=1,
        beer_cost=0,
        commodity_count=4,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.IRON, 3): IndustryStats(
        money_cost=9,
        coal_cost=1,
        iron_cost=0,
        vp=7,
        income=2,
        connection_vp=1,
        beer_cost=0,
        commodity_count=5,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.IRON, 4): IndustryStats(
        money_cost=12,
        coal_cost=1,
        iron_cost=0,
        vp=9,
        income=1,
        connection_vp=1,
        beer_cost=0,
        commodity_count=6,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.BEER, 1): IndustryStats(
        money_cost=5,
        coal_cost=0,
        iron_cost=1,
        vp=4,
        income=4,
        connection_vp=2,
        beer_cost=0,
        commodity_count=1,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=Era.CANAL,
    ),
    (IndustryType.BEER, 2): IndustryStats(
        money_cost=7,
        coal_cost=0,
        iron_cost=1,
        vp=5,
        income=5,
        connection_vp=2,
        beer_cost=0,
        commodity_count=1,
        no_develop=False,
        double_commodity_rail_era=True,
        era_only=None,
    ),
    (IndustryType.BEER, 3): IndustryStats(
        money_cost=9,
        coal_cost=0,
        iron_cost=1,
        vp=7,
        income=5,
        connection_vp=2,
        beer_cost=0,
        commodity_count=1,
        no_develop=False,
        double_commodity_rail_era=True,
        era_only=None,
    ),
    (IndustryType.BEER, 4): IndustryStats(
        money_cost=9,
        coal_cost=0,
        iron_cost=1,
        vp=10,
        income=5,
        connection_vp=2,
        beer_cost=0,
        commodity_count=1,
        no_develop=False,
        double_commodity_rail_era=True,
        era_only=Era.RAIL,
    ),
    (IndustryType.COTTON, 1): IndustryStats(
        money_cost=12,
        coal_cost=0,
        iron_cost=0,
        vp=5,
        income=5,
        connection_vp=1,
        beer_cost=1,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=Era.CANAL,
    ),
    (IndustryType.COTTON, 2): IndustryStats(
        money_cost=14,
        coal_cost=1,
        iron_cost=0,
        vp=5,
        income=4,
        connection_vp=2,
        beer_cost=1,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.COTTON, 3): IndustryStats(
        money_cost=16,
        coal_cost=1,
        iron_cost=1,
        vp=9,
        income=3,
        connection_vp=1,
        beer_cost=1,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.COTTON, 4): IndustryStats(
        money_cost=18,
        coal_cost=1,
        iron_cost=1,
        vp=12,
        income=2,
        connection_vp=1,
        beer_cost=1,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.MANUFACTURED_GOODS, 1): IndustryStats(
        money_cost=8,
        coal_cost=1,
        iron_cost=0,
        vp=3,
        income=5,
        connection_vp=2,
        beer_cost=1,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=Era.CANAL,
    ),
    (IndustryType.MANUFACTURED_GOODS, 2): IndustryStats(
        money_cost=10,
        coal_cost=0,
        iron_cost=1,
        vp=5,
        income=1,
        connection_vp=1,
        beer_cost=1,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.MANUFACTURED_GOODS, 3): IndustryStats(
        money_cost=12,
        coal_cost=2,
        iron_cost=0,
        vp=4,
        income=4,
        connection_vp=0,
        beer_cost=0,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.MANUFACTURED_GOODS, 4): IndustryStats(
        money_cost=8,
        coal_cost=0,
        iron_cost=1,
        vp=3,
        income=6,
        connection_vp=1,
        beer_cost=1,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.MANUFACTURED_GOODS, 5): IndustryStats(
        money_cost=16,
        coal_cost=1,
        iron_cost=0,
        vp=8,
        income=2,
        connection_vp=2,
        beer_cost=2,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.MANUFACTURED_GOODS, 6): IndustryStats(
        money_cost=20,
        coal_cost=0,
        iron_cost=0,
        vp=7,
        income=6,
        connection_vp=1,
        beer_cost=1,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.MANUFACTURED_GOODS, 7): IndustryStats(
        money_cost=16,
        coal_cost=1,
        iron_cost=1,
        vp=9,
        income=4,
        connection_vp=0,
        beer_cost=0,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.MANUFACTURED_GOODS, 8): IndustryStats(
        money_cost=20,
        coal_cost=0,
        iron_cost=2,
        vp=11,
        income=1,
        connection_vp=1,
        beer_cost=1,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.POTTERY, 1): IndustryStats(
        money_cost=17,
        coal_cost=0,
        iron_cost=1,
        vp=10,
        income=5,
        connection_vp=1,
        beer_cost=1,
        commodity_count=0,
        no_develop=True,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.POTTERY, 2): IndustryStats(
        money_cost=0,
        coal_cost=1,
        iron_cost=0,
        vp=1,
        income=1,
        connection_vp=1,
        beer_cost=1,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.POTTERY, 3): IndustryStats(
        money_cost=22,
        coal_cost=2,
        iron_cost=0,
        vp=11,
        income=5,
        connection_vp=1,
        beer_cost=2,
        commodity_count=0,
        no_develop=True,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.POTTERY, 4): IndustryStats(
        money_cost=0,
        coal_cost=1,
        iron_cost=0,
        vp=1,
        income=1,
        connection_vp=1,
        beer_cost=1,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=None,
    ),
    (IndustryType.POTTERY, 5): IndustryStats(
        money_cost=24,
        coal_cost=2,
        iron_cost=0,
        vp=20,
        income=5,
        connection_vp=1,
        beer_cost=2,
        commodity_count=0,
        no_develop=False,
        double_commodity_rail_era=False,
        era_only=Era.RAIL,
    ),
}

INDUSTRY_TILE_COUNTS = {
    (IndustryType.COAL, 1): 1,
    (IndustryType.COAL, 2): 2,
    (IndustryType.COAL, 3): 2,
    (IndustryType.COAL, 4): 2,
    (IndustryType.IRON, 1): 1,
    (IndustryType.IRON, 2): 1,
    (IndustryType.IRON, 3): 1,
    (IndustryType.IRON, 4): 1,
    (IndustryType.BEER, 1): 2,
    (IndustryType.BEER, 2): 2,
    (IndustryType.BEER, 3): 2,
    (IndustryType.BEER, 4): 1,
    (IndustryType.COTTON, 1): 3,
    (IndustryType.COTTON, 2): 2,
    (IndustryType.COTTON, 3): 3,
    (IndustryType.COTTON, 4): 3,
    (IndustryType.MANUFACTURED_GOODS, 1): 1,
    (IndustryType.MANUFACTURED_GOODS, 2): 2,
    (IndustryType.MANUFACTURED_GOODS, 3): 1,
    (IndustryType.MANUFACTURED_GOODS, 4): 1,
    (IndustryType.MANUFACTURED_GOODS, 5): 2,
    (IndustryType.MANUFACTURED_GOODS, 6): 1,
    (IndustryType.MANUFACTURED_GOODS, 7): 1,
    (IndustryType.MANUFACTURED_GOODS, 8): 2,
    (IndustryType.POTTERY, 1): 1,
    (IndustryType.POTTERY, 2): 1,
    (IndustryType.POTTERY, 3): 1,
    (IndustryType.POTTERY, 4): 1,
    (IndustryType.POTTERY, 5): 1,
}


class Industry:
    def __init__(self, industry_type: IndustryType, level: int, player_id: int):
        self.industry_type = industry_type
        self.level = level
        self.player_id = player_id
        self.stats = INDUSTRY_STATS[industry_type, level]
        self.flipped = False


class Industries:
    def __init__(self, player_id: int):
        self.player_id = player_id
        self.industry_levels = {
            IndustryType.COAL: 1,
            IndustryType.IRON: 1,
            IndustryType.BEER: 1,
            IndustryType.COTTON: 1,
            IndustryType.MANUFACTURED_GOODS: 1,
            IndustryType.POTTERY: 1,
        }
        self.industry_tile_counts = INDUSTRY_TILE_COUNTS.copy()

    def get_next_industry(self, industry_type: IndustryType) -> Industry | None:
        level = self.industry_levels[industry_type]
        if (industry_type, level) not in self.industry_tile_counts:
            return None
        return Industry(
            industry_type=industry_type, level=level, player_id=self.player_id
        )

    def develop_industry(self, industry_type: IndustryType):
        current_level = self.industry_levels[industry_type]
        if (industry_type, current_level) not in self.industry_tile_counts:
            return
        current_count = self.industry_tile_counts[industry_type, current_level]
        new_count = current_count - 1
        if new_count <= 0:
            self.industry_levels[industry_type] += 1
        else:
            self.industry_tile_counts[industry_type, current_level] = new_count
