from random import randint

from Creature import Creature
from battle import battle


def main():
    creatures_defeated = 0
    player = Creature(8,15, "player")
    enemy = Creature(randint(0,6),randint(5,10), f"Enemy {creatures_defeated}")

    
    # informação_do_jogador = player.info()

    # print(informação_do_jogador)
    # battle(player, enemy)

    options = {
        1: "Check player info",
        2: "Check Enemy info",
        3: "Battle enemy"
    }

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
                enemy = Creature(randint(3,5+creatures_defeated),randint(3,7+creatures_defeated), f"Enemy {creatures_defeated}")

        print("-="*40)


    print(f"You defeated {creatures_defeated} creatures")



if __name__ == "__main__":
    main()
