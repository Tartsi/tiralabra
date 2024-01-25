"""
This module is responsible for the games logic
"""


class Logic:
    """
    Handles the game logic i.e functionalities
    """

    def __init__(self, board):
        """Initializes the game logic

        Args:
            board (Board): Board to be used for the game
        """
        self.board = board
        # X represents Black, which starts first in Gomoku
        self.current_turn = 'X'
        self.game_over = False

    def make_move(self, row, column, player):
        """Moves players piece on board if not occupied

        Args:
            row int: Row to be moved to
            column int: Column to be moved to
            player str: Piece to be moved. 'X' or '0'.

        Returns:
            bool: True or False whether the move was successful or not
        """
        if row < 0 or row >= len(self.board.board):
            print("Invalid row!")
            return False

        if column < 0 or column >= len(self.board.board):
            print("Invalid column!")
            return False

        if self.board.board[row][column] == "-":
            self.board.make_move(row, column, player)
            return True

        print(f"Square ({row}, {column}) is already occupied!")
        return False

    def check_draw(self):
        """Check if the game board is full

        Returns:
            bool: True if the game board is full, False otherwise
        """

        for row in self.board.board:
            if "-" in row:
                return False

        return True
