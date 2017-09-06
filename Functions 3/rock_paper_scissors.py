# Break up the function:
#  def play_rock_paper_scissors(n_rounds):
#      '''
#      Input:  Int - number of rounds to play rock paper scissors for
#      '''
#      for _ in range(n_rounds):
#          player_1 = raw_input('Player 1 play (r/p/s): ')
#          player_2 = raw_input('Player 2 play (r/p/s): ')
#          if player_1 == player_2:
#              print("It's a tie!")
#          elif player_1 == 'r' and player_2 == 's':
#              print('Player 1 wins!')
#          elif player_1 == 'r' and player_2 == 'p':
#              print('Player 2 wins!')
#          elif player_1 == 'p' and player_2 == 'r':
#              print('Player 1 wins!')
#          elif player_1 == 'p' and player_2 == 's':
#              print('Player 2 wins!')
#          elif player_1 == 's' and player_2 == 'r':
#              print('Player 2 wins!')
#          elif player_1 == 's' and player_2 == 'p':
#              print('Player 1 wins!')
#          else:
#              print("Someone didn't play right!")

def player_1_wins(player_1, player_2):

    if (player_1 == 'r' and player_2 == 's') or (player_1 == 'p' and player_2 == 'r') or (player_1 == 's' and player_2 == 'p'):
        return True
    return False

def play_rock_paper_scissors(n_rounds):
    #  '''
    #  Input:  Int - number of rounds to play rock paper scissors for
    #  '''
    for _ in range(n_rounds):
        player_1 = raw_input('Player 1 play (r/p/s): ')
        player_2 = raw_input('Player 2 play (r/p/s): ')
        if player_1 not in "rps" or player_2 not in "rps":
            print "Someone didn't play right"
        elif player_1 == player_2:
            print("It's a tie!")
        elif player_1_wins(player_1, player_2) is True:
            print('Player 1 wins!')
        else:
            print ("Player 2 wins!")


rounds = int(raw_input("How many rounds do you want to play?: "))
play_rock_paper_scissors(rounds)
