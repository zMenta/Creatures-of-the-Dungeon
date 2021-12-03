
class Creature:
    """
    Class of a Creature.

    It initializes with strength and vitality attributes.
    """
    def __init__(self, strength, vitality) -> None:
        self.strength = strength
        self.vitality = vitality

        self.health = vitality*3
        self.attack = round(strength*1.5)


    def info(self) -> dict:
        info = {
            "strength": self.strength,
            "vitality": self.vitality,
            "health": self.health,
            "attack": self.attack
        }

        return info

