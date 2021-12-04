
class Creature:
    """
    Class of a Creature.
    It initializes with strength and vitality attributes.
    """
    def __init__(self, strength, vitality) -> None:
        self.strength = strength
        self.vitality = vitality

        self.health = round(vitality*3)
        self.attack = round(strength*1.5)

        self.equipment = None


    def info(self) -> dict:
        """
        Returns the info and stats of the creature.
        Returns:
            dict
        """
        info = {
            "strength": self.strength,
            "vitality": self.vitality,
            "health": self.health,
            "attack": self.attack,
            "equipment": self.equipment
        }
        
        return info

