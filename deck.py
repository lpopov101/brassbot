import random

from .card import Card, CardType
from .merchant_tile import MerchantTile
from .location import Location
from .industries import IndustryType


class Deck[T]:
    def __init__(self, items: list[T]):
        self.items = items
        self.discard = []
        self.shuffle()

    def draw(self) -> T:
        result = self.items.pop()
        self.discard.append(result)
        return result

    def shuffle(self):
        random.shuffle(self.items)

    def reset(self):
        self.items.extend(self.discard)
        self.discard.clear()
        self.shuffle()

    def remaining(self) -> int:
        return len(self.items)


def build_merchant_tile_deck(player_count: int) -> Deck[MerchantTile]:
    merchant_tiles = [
        MerchantTile([]),
        MerchantTile([]),
        MerchantTile([IndustryType.MANUFACTURED_GOODS]),
        MerchantTile([IndustryType.COTTON]),
        MerchantTile(
            [
                IndustryType.MANUFACTURED_GOODS,
                IndustryType.COTTON,
                IndustryType.POTTERY,
            ]
        ),
    ]
    if player_count >= 3:
        merchant_tiles.extend(
            [
                MerchantTile([IndustryType.POTTERY]),
                MerchantTile([]),
            ]
        )
    if player_count >= 4:
        merchant_tiles.extend(
            [
                MerchantTile([IndustryType.MANUFACTURED_GOODS]),
                MerchantTile([IndustryType.COTTON]),
            ]
        )
    return Deck(merchant_tiles)


def build_main_deck(player_count: int) -> Deck[Card]:
    cards = []

    def add_location_cards(location_counts: list[(Location, int)]):
        for location, count in location_counts:
            for _ in range(count):
                cards.append(Card(CardType.LOCATION, location=location))

    def add_industry_cards(industry_counts: list[(list[IndustryType], int)]):
        for industry_type_list, count in industry_counts:
            for _ in range(count):
                cards.append(Card(CardType.INDUSTRY, industries=industry_type_list))

    add_location_cards(
        [
            (Location.STAFFORD, 2),
            (Location.BURTON_ON_TRENT, 2),
            (Location.CANNOCK, 2),
            (Location.TAMWORTH, 1),
            (Location.WALSALL, 1),
            (Location.COALBROOKDALE, 3),
            (Location.DUDLEY, 2),
            (Location.KIDDERMINSTER, 2),
            (Location.WOLVERHAMPTON, 2),
            (Location.WORCESTER, 2),
            (Location.BIRMINGHAM, 3),
            (Location.COVENTRY, 3),
            (Location.NUNEATON, 1),
            (Location.REDDITCH, 1),
        ]
    )
    add_industry_cards(
        [
            ([IndustryType.IRON], 4),
            ([IndustryType.COAL], 2),
            ([IndustryType.POTTERY], 2),
            ([IndustryType.BEER], 5),
        ]
    )

    if player_count >= 3:
        add_location_cards(
            [
                (Location.LEEK, 2),
                (Location.STOKE_ON_TRENT, 3),
                (Location.STONE, 2),
                (Location.UTTOXETER, 1),
            ]
        )
        add_industry_cards(
            [
                ([IndustryType.MANUFACTURED_GOODS, IndustryType.COTTON], 6),
            ]
        )

    if player_count >= 4:
        add_location_cards(
            [
                (Location.BELPER, 2),
                (Location.DERBY, 2),
                (Location.UTTOXETER, 1),
            ]
        )
        add_industry_cards(
            [
                ([IndustryType.COAL], 1),
                ([IndustryType.MANUFACTURED_GOODS, IndustryType.COTTON], 2),
                ([IndustryType.POTTERY], 1),
            ]
        )

    return Deck(cards)


def build_wild_location_deck(player_count: int) -> Deck[Card]:
    cards = [Card(CardType.LOCATION, wild=True)] * player_count
    return Deck(cards)


def build_wild_industry_deck(player_count: int) -> Deck[Card]:
    cards = [Card(CardType.INDUSTRY, wild=True)] * player_count
    return Deck(cards)
