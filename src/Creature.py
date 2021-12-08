
from Equipment import Armor, Weapon


class Creature:
    """
    Class of a Creature.
    It initializes with strength,vitality and name attributes.
    """
    def __init__(self, name, strength, vitality,level=1,armor_slot = None, weapon_slot = None) -> None:
        self.name = name
        self.level = level
        self.strength = strength
        self.vitality = vitality
        self.health = round(self.vitality*3)
        self.armor_slot = armor_slot
        self.weapon_slot = weapon_slot

        if not self.weapon_slot:
            self.attack_power = round(self.strength*1.5)

        if self.weapon_slot:
            self.attack_power = round(self.strength*1.5) + self.weapon_slot.damage

        if not self.armor_slot:
            self.defense = 0

        if self.armor_slot:
            self.defense = armor_slot.defense

    def info(self) -> dict:
        """
        Returns the info and stats of the creature.
        Returns:
            dict
        """
        info = vars(self)
        return info
    
    def update(self) -> None:
        """Updates the attack_power and restores health
        """
        self.health = round(self.vitality*3)

        if not self.weapon_slot:
            self.attack_power = round(self.strength*1.5)

        if self.weapon_slot:
            self.attack_power = round(self.strength*1.5) + self.weapon_slot.damage

    def attack(self, target) -> None:
        """
        Attacks the Creature in the paremeter.
        """
        attack_damage = self.attack_power

        if(self.is_alive()):
            damage_dealt = attack_damage - target.defense
            
            if damage_dealt < 0:
                damage_dealt = 0

            target.health -= damage_dealt
            return (f"{self.name} Attacked {target.name} and dealt {damage_dealt} damage!")

    def equip(self, equipment) -> None:
        """Equips a weapon or an armor into weapon_slot or armor_slot

        Args:
            equipment (equipment)
        """
        if type(equipment) is Weapon:
            self.weapon_slot = equipment
            self.attack_power = round(self.strength*1.5) + equipment.damage

        if type(equipment) is Armor:
            self.armor_slot = equipment
            self.defense = equipment.defense
        
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
