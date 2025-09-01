import visuals
from entity import Entity
import json
import random



class Monster(Entity):
    def __init__(self, name: str, hp: int, power: int, experience: int, level: int):
        super().__init__(name, hp, power)
        self.experience = experience
        self.level = level

    def show_info(self):
        super().show_info()
        if self.is_alive():
            print(f"| {visuals.emojis.get('monster')} {self.level} LVL")

    @classmethod
    def load_monster_from_json(cls, file_path, player_level)-> "Monster":
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            while True:
                random_index = random.randint(0, len(data)-1)
                monster_level = data[random_index]["level"]
                # wybiera potwory z poziomem maksymalnie o jeden wyżej lub minimalnie o jeden niżej w stosunku do poziomu gracza
                if player_level-1 <= monster_level <= player_level+1:
                    monster_name = data[random_index]["name"]
                    monster_hp = data[random_index]["hp"]
                    monster_power = data[random_index]["power"]
                    monster_experience = data[random_index]["experience"]

                    return Monster(monster_name, monster_hp, monster_power, monster_experience, monster_level)