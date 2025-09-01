class Item:
    def __init__(self, name: str, amount: int, limit: int):
        self.name = name
        self.amount = amount
        self.limit = limit

    def is_in_bag(self) -> bool:
        return self.amount > 0