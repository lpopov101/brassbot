from dataclasses import dataclass

from .location import Location
from .industries import Industry
from .card import Card
from .player import Player
from .brassboard import BrassBoard
from .deck import (
    build_main_deck,
    build_wild_industry_deck,
    build_wild_location_deck,
)
from .market import Market
from .eras import Era


@dataclass
class Action:
    player_id: int
    discard: Card


@dataclass
class BuildAction(Action):
    location: Location
    industry: Industry


@dataclass
class ConnectAction(Action):
    location_1: Location
    location_2: Location


@dataclass
class DevelopAction(Action):
    industry_1: Industry
    industry_2: Industry | None


@dataclass
class ScoutAction(Action):
    extra_discard_1: Card
    extra_discard_2: Card


@dataclass
class SellAction(Action):
    pass


@dataclass
class LoanAction(Action):
    pass


class BrassGame:

    def __init__(self, player_count: int):
        self.player_count = player_count
        self.player_order = [1, 2, 3, 4][:player_count]
        self.turn = 0
        self.board = BrassBoard(player_count)
        self.players = [Player(i) for i in range(min(max(player_count, 1), 4))]
        self.coal_market = Market(cur_price=1, remaining_at_price=1, max_price=8)
        self.iron_market = Market(cur_price=2, remaining_at_price=2, max_price=6)
        self.main_deck = build_main_deck(player_count)
        self.wild_industry_deck = build_wild_industry_deck(player_count)
        self.wild_location_deck = build_wild_location_deck(player_count)
        self.era = Era.CANAL

    def get_current_player_id(self) -> int:
        return self.player_order[self.turn]

    def get_player(self, player_id: int) -> Player:
        return self.players[player_id - 1]

    def take_loan(self, player_id: int):
        player = self.get_player(player_id)
        player.income.take_loan()
        player.pounds += 30

    def get_total_price(self, pounds: int, iron: int, coal: int) -> int:
        return (
            pounds + self.iron_market.get_price(iron) + self.coal_market.get_price(coal)
        )

    def pay(self, player_id: int, pounds: int, iron: int, coal: int):
        player = self.get_player(player_id)
        total_price = self.get_total_price(pounds, iron, coal)
        player.pounds -= total_price
        player.pounds_spent_this_turn += total_price
        self.iron_market.buy(iron)
        self.coal_market.buy(coal)

    def flip_industry(self, industry: Industry):
        industry.flipped = True
        player = self.get_player(industry.player_id)
        player.income.increase(industry.stats.income_increase)

    def end_round(self):
        # Change player order by pounds spent this turn (player who spent least goes first)
        self.player_order.sort(
            key=lambda player_id: self.get_player(player_id).pounds_spent_this_turn
        )

        # Apply incomes
        for player in self.players:
            income = player.income.get_level()
            if income < 0 and player.pounds < -income:
                self.take_loan(player.id)

    def end_game(self):
        winning_player = max(self.players, key=lambda player: player.vp)
        print(
            f"Game over! The winner is {winning_player.name} with {winning_player.vp} VP."
        )
        exit()

    def end_era(self):
        # Count up connector VPs
        for connector_node in self.board.connector_nodes:
            self.get_player(
                connector_node.player_id
            ).vp += self.board.get_connector_node_vp(connector_node)

        # Count up industry VPs and clear level 1 industries
        for location_node in self.board.city_nodes:
            for industry_slot in location_node.industry_slots:
                if industry_slot.cur_industry is not None:
                    industry = industry_slot.cur_industry
                    if industry.flipped:
                        self.get_player(industry.player_id).vp += industry.stats.vp
                    if industry.level == 1:
                        industry_slot.cur_industry = None

        # Reset merchant beer
        for merchant_node in self.board.merchant_nodes:
            for merchant_tile_slot in merchant_node.merchant_tile_slots:
                if merchant_tile_slot.merchant_tile is not None:
                    merchant_tile_slot.beer_avaiable = True

        # Reset decks
        self.main_deck.reset()
        self.wild_industry_deck.reset()
        self.wild_location_deck.reset()

        # Move to next era or end game
        if self.era == Era.CANAL:
            self.era = Era.RAIL
        elif self.era == Era.RAIL:
            self.end_game()
