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
        # Necessary for MiniMax-algorithm
        self.moves_made = []

    def make_move(self, row, column, player):
        """Moves the player on the board if given square is not occupied"""

        if self.board[row][column] == '-':
            current_state = self.board[row][column]
            self.moves_made.append((row, column, current_state))
            self.board[row][column] = player
            return True

        return False

    def undo_move(self):
        """Undos the previously made move on the board
        Necessary for AI's minimax-algorithm"""

        if self.moves_made:
            row, column, previous_state = self.moves_made.pop()
            self.board[row][column] = previous_state
            return True

        return False
