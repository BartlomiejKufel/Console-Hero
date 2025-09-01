import visuals


class Entity:
    def __init__(self, name: str, hp: int, power: int):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power


    def show_info(self):
        if self.is_alive():
            print(f"{self.name}: {visuals.emojis.get('heart')} {self.hp}/{self.max_hp} HP | {visuals.emojis.get('sword')} {self.power} A ", end=" ")
        else:
            print(f"{self.name} nie żyje {visuals.emojis.get('skull')}!")

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, damage: int):
        self.hp -= damage
        print(f"{self.name} otrzymuje {damage} obrażeń")

    def deal_damage(self, target: "Entity"):
        print(f"{self.name} atakuje {target.name} zadając {self.power} obrażeń")
        target.take_damage(self.power)
        if not target.is_alive():
            print(f"{self.name} pokonuje {target.name}!")

    def heal_damage(self, amount: int):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print(f"{self.name} leczy się o {amount}. Teraz ma {self.hp} HP")

    def revive (self):
        self.hp = self.max_hp