from .industries import Industries
from .income import Income


class Player:
    def __init__(self, name):
        self.name = name
        self.pounds = 17
        self.pounds_spent_this_turn = 0
        self.income = Income()
        self.vp = 0
        self.link_tiles = 14
        self.industries = Industries()
        self.hand = []
