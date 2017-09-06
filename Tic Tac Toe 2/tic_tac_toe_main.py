from tic_tac_toe_with_classes import *

want_to_play = "y"

while want_to_play != "n":

    want_to_play = raw_input("\nWould you like to play a game of Tic-Tac-Toe? (y/n): ")

    if want_to_play == "y":
        game = Game()
        game.play_game()

    elif want_to_play == "n":
        print "Okay, maybe another time..."
