import json
import visuals
from entity import Entity
from item import Item
from monster import Monster

max_level = 15 #maksymalny poziom do zdobycia
heal_potion_index = 0 #indeks mikstury leczenia w plecaku
levels_file_path = "assets/levels.json" # ścieżka do informacji o bazowych statystykach każdego poziomu gracza

class Player(Entity):

    def __init__(self, name: str, hp: int, power: int):
        super().__init__(name, hp, power)
        self.level = 1
        self.level_cap = 0  # granica poziomu, >= oznacza level up, na początek ustawiona na defaultową wartość
        self.experience = 0
        self.bag = [Item("Mikstura Zdrowia", 3,3)]
        self.set_lvl_statistic()
        self.revive()

    def show_info(self):
        super().show_info()
        if self.is_alive() :
            if self.level == max_level :
                print(f"| {visuals.emojis.get('stars')} MAX EXP | {visuals.emojis.get('hero')} {self.level} LVL")
            else:
                print(f"| {visuals.emojis.get('stars')} {self.experience}/{self.level_cap} EXP | {visuals.emojis.get('hero')} {self.level} LVL")


    def add_experience(self, amount: int):
        if not self.is_max_level():
            self.experience += amount
            print(f"{self.name} zdobywa {amount} EXP")
            while self.can_level_up() and not self.is_max_level():
                self.experience = self.experience - self.level_cap
                self.level += 1
                self.set_lvl_statistic()
                print(f"{self.name} zdobywa nowy poziom! Teraz ma {self.level} LVL")


    def can_level_up(self):
        return self.experience >= self.level_cap

    def is_max_level(self):
        return self.level == max_level

    def set_lvl_statistic(self):
        with open(levels_file_path, "r", encoding="utf-8") as f:
            levels = json.load(f)
            self.max_hp = levels[self.level-1]["max_hp"]
            self.power = levels[self.level-1]["power"]
            self.level_cap = levels[self.level-1]["level_cap"]

    def deal_damage(self, target: "Monster"):
        super().deal_damage(target)
        if not target.is_alive():
            self.add_experience(target.experience)


