from dataclasses import dataclass


@dataclass
class SellStats:
    quantity_sold: int
    profit: int


class Market:
    def __init__(self, cur_price: int, remaining_at_price: int, max_price: int):
        self.cur_price
        self.remaining_at_price = remaining_at_price
        self.max_price = max_price

    def buy(self, quantity: int) -> int:
        final_price = 0
        for _ in range(quantity):
            if self.remaining_at_price == 0:
                self.cur_price += 1
                self.remaining_at_price = 2
            if self.cur_price < self.max_price:
                self.remaining_at_price -= 1
            final_price += self.cur_price
        return final_price

    def sell(self, quantity: int) -> SellStats:
        profit = 0
        quantity_sold = 0
        for _ in range(quantity):
            if self.remaining_at_price == 2:
                if self.cur_price <= 1:
                    break
                self.cur_price -= 1
                self.remaining_at_price = 0
            self.remaining_at_price += 1
            profit += self.cur_price
            quantity_sold += 1

        return SellStats(quantity_sold=quantity_sold, profit=profit)

    def get_price(self, quantity: int) -> int:
        market_copy = self.copy()
        return market_copy.buy(quantity)
