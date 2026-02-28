from .industries import IndustryType


class MerchantTile:
    def __init__(self, industry_types: list[IndustryType]):
        self.industry_types = industry_types
