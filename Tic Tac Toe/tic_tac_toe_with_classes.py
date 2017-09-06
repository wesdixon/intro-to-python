class Player():

    def __init__(self, name, icon):

        self.name = name
        self.icon = icon


class Board():

    def __init__(self, player1, player2):

        self.top_row = [(0, 0), (1,0), (2,0)]
        self.middle_row = [(0, 1), (1,1), (2,1)]
        self.bottom_row = [(0, 2), (1,2), (2,2)]
        self.all_rows = [self.top_row, self.middle_row, self.bottom_row]

        self.player1 = player1
        self.player2 = player2

        self.player1_turn = True


    def print_board(self):
        print ""
        print self.all_rows[0]
        print self.all_rows[1]
        print self.all_rows[2]


    def update_board(self, play_made):

        #Check whose turn it is to assign the mark
        if self.player1_turn:
            mark = "  {} ".format(self.player1.icon)
        else:
            mark = "  {} ".format(self.player2.icon)

        if play_made[1] == 0:
            #Change the top row
            self.all_rows[0] = [mark if index == play_made else index for index in self.all_rows[0]]
        elif play_made[1] == 1:
            #Change the middle row
            self.all_rows[1] = [mark if index == play_made else index for index in self.all_rows[1]]
        elif play_made[1] == 2:
            #Change the bottom row
            self.all_rows[2] = [mark if index == play_made else index for index in self.all_rows[2]]

        #Switch the player's turn
        self.player1_turn = not self.player1_turn


    #This function checks all 8 possible ways to win the game to see if it is over and someone has won
    def is_game_over(self):
        #Check the board to see if game is over
        mark_lst = ["  {} ".format(self.player1.icon), "  {} ".format(self.player2.icon) ]

        #Check the top, middle, and bottom rows
        for index in mark_lst:
            if self.all_rows[0].count(index) == 3 or self.all_rows[1].count(index) == 3 or self.all_rows[2].count(index) == 3:
                return True

        #Check the left, middle, and right columns
        left_column = [self.all_rows[0][0], self.all_rows[1][0], self.all_rows[2][0]]
        middle_column = [self.all_rows[0][1], self.all_rows[1][1], self.all_rows[2][1]]
        right_column = [self.all_rows[0][2], self.all_rows[1][2], self.all_rows[2][2]]

        for index in mark_lst:
            if left_column.count(index) == 3 or middle_column.count(index) == 3 or left_column.count(index) == 3:
                return True

        #Check the first, and second diagonals
        first_diagonal = [self.all_rows[0][0], self.all_rows[1][1], self.all_rows[2][2]]
        second_diagonal = [self.all_rows[0][2], self.all_rows[1][1], self.all_rows[2][0]]

        for index in mark_lst:
            if first_diagonal.count(index) == 3 or second_diagonal.count(index) == 3:
                return True

        return False



class Game():

    def __init__(self):

        self.turn_num = 1
        self.game_over = False


    def set_up_game(self):

        print ("\nLet's set up the game:")

        #Set up Player 1's name and icon, and make sure name isn't blank and icon is only one character
        player1_name = ""
        while player1_name == "":
            player1_name = raw_input("Please enter Player 1's name:  ")

        player1_icon = "XX"
        while len(player1_icon) != 1:
            player1_icon = raw_input("Please enter a single character icon to play as: ")

        #Assign data into player1 attribute of Game class
        self.player1 = Player(player1_name, player1_icon)

        #Set up Player 2's name and icon, and make sure name isn't blank and icon is only one character
        player2_name = ""
        while player2_name == "":
            player2_name = raw_input("Please enter Player 2's name:  ")

        player2_icon = "XX"
        while len(player2_icon) != 1:
            player2_icon = raw_input("Please enter a single character icon to play as: ")

        #Assign data into player 1 attribute of Game class
        self.player2 = Player(player2_name, player2_icon)

        #Instantiate a new Board object and pass player1 and player2 objects into it
        self.board = Board(self.player1, self.player2)


    def make_a_play(self):

        if self.board.player1_turn:
            player_name = self.player1.name
        else:
            player_name = self.player2.name

        input_play = raw_input("Now {} gets to play.  Enter coordinates of where you want to go (two numbers, separated by comma): ".format(player_name))
        input_play = input_play.replace(" ", "")
        play_made = tuple(int(num) for num in input_play.split(","))

        self.board.update_board(play_made)


    def end_of_game(self):

        self.board.print_board()
        self.game_over = self.board.is_game_over()

        #Determine whose turn it was when game ended
        if self.turn_num % 2 == 0:
            player_name = self.player1.name
        else:
            player_name = self.player2.name

        #Check if it is a tie, otherwise show who won
        if self.turn_num == 10 and self.game_over is False:
            print "Dang!  It's a tie!!"
        else:
            print "Game over!!  {} wins this time!!".format(player_name)


    def play_game(self):

        self.set_up_game()

        while self.turn_num < 10 and self.game_over is False:

            self.board.print_board()

            self.make_a_play()

            self.game_over = self.board.is_game_over()
            self.turn_num += 1

        self.end_of_game()


#Added to different file
#Main test block

# want_to_play = "y"
#
# while want_to_play != "n":
#
#     want_to_play = raw_input("\nWould you like to play a game of Tic-Tac-Toe? (y/n): ")
#
#     if want_to_play == "y":
#         game = Game()
#         game.play_game()
#
#     elif want_to_play == "n":
#         print "Okay, maybe another time..."
