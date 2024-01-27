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

    # def undo_move(self, row, column, player):
    #     """Undos the previously made move on the board
    #     Necessary for AI's minimax-algorithm"""
    #     pass

    def get_possible_moves(self):
        """Returns a set of possible moves"""
        # Move Pruning Optimization will be applied here

        # Use sets for faster lookups O(1) for later usage
        legal = set()

        for row in range(len(self.board)):

            for column in range(len(self.board)):

                if self.board[row][column] == '-':

                    legal.add((row, column))

        return legal

    def print_board(self):
        """Prints the current state of the board"""

        for row in self.board:
            print(" ".join(row))
        print()
