from random import choice
from random import random
from random import randint

from Equipment import Armor, Weapon

def battle(player, enemy):
    """
    Makes a battle until one creatures defeats another. The first Creature in the parameter attacks first.

    Returns true if player won. Else returns false

    Args:
        player (Creature)
        enemy (Creature)
    """
    while(player.is_alive() and enemy.is_alive()):
        print(player.attack(enemy))
        print(enemy.attack(player))
        
        if(player.is_dead()):
            print(f"{enemy.name} defeated {player.name}")
            return False

        if(enemy.is_dead()):
            print(f"{player.name} defeated {enemy.name}")
            return True

def loot_drop(probability,modifier=0):
    """
    Probability of receiving an Equipment. Returns the equipment generated.

    Args:
        probability (float): [The probability of receiving the loot_drop. Values between 0 and 1. Ex 0.50 equals to 50% probability of dropping loot.]
        modifier (int, optional): [The amount of modified higher stats equipment]. Defaults to 0.

    Returns:
        [Equipment]: Either a weapon or armor
    """
    chance = random()
    if chance <= probability:
        weapon = Weapon("Weapon",randint(2+modifier,5+modifier))
        armor = Armor("Armor",randint(1+modifier,4+modifier))
        items = [weapon,armor]
        return choice(items)

    if not chance <= probability:
        return False

def level_up(Creature, attribute ):
    pass