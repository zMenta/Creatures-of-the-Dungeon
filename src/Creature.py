
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
        if(self.is_alive()):
            target.health -= self.attack_damage
            print(f"{self.name} Attacked {target.name} and dealt {self.attack_damage} damage!")
        
        
    def is_dead(self) -> bool:
        """
        Returns true if creature has it's health <= 0, else returns false
        """

        if(self.health <= 0):
            return True

        if(not self.health <= 0):
            return False

    def is_alive(self) -> bool:
        """
        Returns true if creature has it's health > 0, else returns false
        """

        return not self.is_dead()
