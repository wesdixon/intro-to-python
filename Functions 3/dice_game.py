# 1. Write a function that rolls two sets of dice to model players playing a game with dice.
# It will accept two arguments, the number of dice to roll for the first player, and
# the number of dice to roll for the second player. Then, the function will do the following:
#
#  * Model rolling the appropriate number of dice for each player.
#  * Sum the total values of the corresponding dice rolls.
#  * Print which player rolled the higher total.
#  * Return the total sum of each players rolls in a tuple.
#
#  Here's how we would call it:
#
#  ```python
#  In [1]: player_rolls = model_dice_rolls(3, 2)
#  Player 1 wins!
#  In [2]: player_rolls
#  Out[2]: (13, 7)

import random

def model_dice_rolls(player1_dice, player2_dice):

    player1_total = sum([random.randint(1,6) for num in range(1,player1_dice)])
    player2_total = sum([random.randint(1,6) for num in range(1,player2_dice)])

    if player1_total == player2_total:
        print "It's at tie!"
    elif player1_total > player2_total:
        print "Player 1 wins!"
    else:
        print "Player 2 wins!"

    return tuple([player1_total, player2_total])

player1 = int(raw_input("Enter the number of dice to roll for the first player: "))
player2 = int(raw_input("Enter the number of dice to roll for the second player: "))

print model_dice_rolls(player1, player2)
