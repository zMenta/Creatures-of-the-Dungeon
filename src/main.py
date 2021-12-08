from random import randint

from Creature import Creature
from Equipment import Armor, Weapon
from game_systems import battle
from game_systems import loot_drop
from data import options


def main():
    creatures_defeated = 0
    player = Creature("player",8,15)
    enemy = Creature(f"Enemy {creatures_defeated}",randint(0,6),randint(5,10))

    while player.is_alive():
        print(options)
        choice = int(input("Type the option: "))
        print(options.get(choice, "Invalid Input"))

        if choice == 1:
            print(player.info())

        if choice == 2:
            print(enemy.info())

        if choice == 3:
            if(battle(player,enemy)):
                creatures_defeated += 1
                enemy = Creature(f"Enemy {creatures_defeated}",randint(3,5+creatures_defeated),randint(3,7+creatures_defeated))
                loot = loot_drop(0.25,creatures_defeated)

                if loot:
                    print(f"You got loot! {(vars(loot))}")
                    print(f"Your gear: Armor {vars(player.armor_slot) if player.armor_slot else None} | Weapon {vars(player.weapon_slot) if player.weapon_slot else None}")
                    choice = input("You want to equip this item? 1-to equip ")
                    if choice == str(1):
                        player.equip(loot)
                

        print("-="*40)


    print(f"You defeated {creatures_defeated} creatures")



if __name__ == "__main__":
    main()
