# 16. Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.

# Because I am not familiar with Super Mario, I am trying to model a
# player of game 8-puzzle.
# It is played on a 3-by-3 grid with 8 square blocks labeled 1 through 8
# and a blank square. Your goal is to rearrange the blocks so that they are
# in order. You are permitted to slide blocks horizontally or vertically
# into the blank square. The following shows a sequence of legal moves
# from an initial board position (left) to the goal position (right).

class EightPuzzle:
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def __init__(self, board_config):
        self.board_config = board_config

    def show_current_board(self):
        print(self.board_config)

    def move_right(self):
        blank_position = self.board_config.index(0)
        if blank_position != 2 and blank_position != 5 and blank_position != 8:
            self.board_config[blank_position] = self.board_config[blank_position+1]
            self.board_config[blank_position+1] = 0
        else:
            print("Not possible to move right.")

    def move_left(self):
        blank_position = self.board_config.index(0)
        if blank_position != 0 and blank_position != 3 and blank_position != 6:
            self.board_config[blank_position] = self.board_config[blank_position-1]
            self.board_config[blank_position-1] = 0
        else:
            print("Not possible to move left.")

    def move_up(self):
        blank_position = self.board_config.index(0)
        if blank_position != 0 and blank_position != 1 and blank_position != 2:
            self.board_config[blank_position] = self.board_config[blank_position-3]
            self.board_config[blank_position-3] = 0
        else:
            print("Not possible to move up.")

    def move_down(self):
        blank_position = self.board_config.index(0)
        if blank_position != 6 and blank_position != 7 and blank_position != 8:
            self.board_config[blank_position] = self.board_config[blank_position+3]
            self.board_config[blank_position+3] = 0
        else:
            print("Not possible to move down.")

    def goal_test(self):
        if self.board_config == EightPuzzle.goal:
            print("Congratulations! You have reached the goal.")
        else:
            print("Goal not reached yet.")

# Here 0 acts as a blank cell
initial = [7, 1, 3, 4, 2, 5, 0, 8, 6]
game1 = EightPuzzle(initial)
game1.show_current_board()
game1.move_right()
game1.show_current_board()
game1.move_left()
game1.show_current_board()
game1.move_up()
game1.show_current_board()
game1.move_down()
game1.show_current_board()
game1.goal_test()
