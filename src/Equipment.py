class Equipment:
    def __init__(self, name) -> None:
        self.name = name

class Weapon(Equipment):
    def __init__(self, name, damage) -> None:
        super().__init__(name)
        self.damage = damage

class Armor(Equipment):
    def __init__(self, name, defense) -> None:
        super().__init__(name)
        self.defense = defense
