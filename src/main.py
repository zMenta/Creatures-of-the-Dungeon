
from Creature import Creature

def main():
    guy = Creature(8,15, "player")
    enemy = Creature(4,5,"enemy")

    print(guy.info())
    print(enemy.info())

    guy.attack(enemy)
    print(enemy.info())
    print(enemy.is_dead())
    guy.attack(enemy)
    print(enemy.info())
    print(enemy.is_dead())
    guy.attack(enemy)
    print(enemy.info())
    print(enemy.is_dead())

if __name__ == "__main__":
    main()
