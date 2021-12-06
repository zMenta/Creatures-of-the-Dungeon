
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

        if(enemy.is_dead()):
            print(f"{player.name} defeated {enemy.name}")
            return True

