
from Creature import Creature
from battle import battle

def main():
    player = Creature(8,15, "player")
    enemy = Creature(20,5,"enemy")

    while(player.is_alive() and enemy.is_alive()):
        battle(player, enemy)

if __name__ == "__main__":
    main()
