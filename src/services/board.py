"""
This module implements the gameboard
"""


class Board:
    """Defines the gameboard
    """

    def __init__(self, board_size=20):
        """Setup 20*20 (default) board"""

        self.board = [['-' for _ in range(board_size)]
                      for _ in range(board_size)]

    def make_move(self, row, column, player):
        """Moves the player on the board if given square is not occupied"""

        if self.board[row][column] == '-':
            self.board[row][column] = player
            return True

        return False

    def print_board(self):
        """Prints the current state of the board"""

        for row in self.board:
            print(" ".join(row))
        print()
