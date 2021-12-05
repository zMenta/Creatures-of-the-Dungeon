
from Creature import Creature
from battle import battle


def main():
    player = Creature(8,15, "player")
    enemy = Creature(20,5,"enemy")

    informação_do_jogador = player.info()

    print(informação_do_jogador)
    battle(player, enemy)

if __name__ == "__main__":
    main()
