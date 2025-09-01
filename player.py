from entity import Entity
from monster import Monster

max_level = 15 #maksymalny poziom do zdobycia


class Player(Entity):

    def __init__(self, name: str, hp: int, power: int):
        super().__init__(name, hp, power)
        self.level = 1
        self.level_cap = 100  # granica poziomu, >= oznacza level up
        self.experience = 0


    def show_info(self):
        super().show_info()
        if self.is_alive() :
            if self.level == max_level :
                print(f"| ✨ MAX EXP | 🧝 {self.level} LVL")
            else:
                print(f"| ✨ {self.experience}/{self.level_cap} EXP | 🧝 {self.level} LVL")


    def add_experience(self, amount: int):
        if not self.is_max_level():
            self.experience += amount
            print(f"{self.name} zdobywa {amount} EXP")
            while self.can_level_up() and not self.is_max_level():
                self.experience = self.experience - self.level_cap
                self.level_cap += 20
                self.level += 1
                print(f"{self.name} zdobywa nowy poziom! Teraz ma {self.level} LVL")


    def can_level_up(self):
        return self.experience >= self.level_cap

    def is_max_level(self):
        return self.level == max_level


    def deal_damage(self, target: "Monster"):
        super().deal_damage(target)
        if not target.is_alive():
            self.add_experience(target.experience)


