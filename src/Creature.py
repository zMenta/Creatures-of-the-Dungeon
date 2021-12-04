
class Creature:
    """
    Class of a Creature.
    It initializes with strength,vitality and name attributes.
    """
    def __init__(self, strength, vitality, name) -> None:
        self.name = name
        self.strength = strength
        self.vitality = vitality

        self.health = round(vitality*3)
        self.attack_damage = round(strength*1.5)


    def info(self) -> dict:
        """
        Returns the info and stats of the creature.
        Returns:
            dict
        """
        info = {
            "name": self.name,
            "strength": self.strength,
            "vitality": self.vitality,
            "health": self.health,
            "attack_damage": self.attack_damage
        }
        
        return info


    def attack(self, target) -> None:
        """
        Attacks the Creature in the paremeter.
        """
        target.health -= self.attack_damage

        print(f"{self.name} Attacked {target.name} and dealt {self.attack_damage} damage!")
        
        

