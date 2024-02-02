"""
This module is responsible for the games logic
"""


class Logic:
    """
    Handles the game logic i.e functionalities
    """

    def __init__(self):
        """Initializes the game logic
        """
        return

    def make_move(self, row, column, player, board):
        """Moves players piece on board if not occupied

        Args:
            row int: Row to be moved to
            column int: Column to be moved to
            player str: Piece to be moved. 'X' or '0'.

        Returns:
            bool: True or False whether the move was successful or not
        """
        if row < 0 or row >= len(board.board):
            print("Invalid row!")
            return False

        if column < 0 or column >= len(board.board):
            print("Invalid column!")
            return False

        if board.board[row][column] == "-":
            board.make_move(row, column, player)
            return True

        print(f"Square ({row}, {column}) is already occupied!")
        return False

    def check_horizontal(self, row, col, player, board):
        """Checks if a player has 5 pieces in a row horizontally

        Args:
            row int: player's row on the board
            column int: player's column on the board
            player str: player, 'X' or '0'

        Returns:
            bool: True if the player has 5 pieces horizontally, False otherwise
        """
        count = 0

        for i in range(max(0, col-4), min(len(board.board[0]), col+5)):
            if board.board[row][i] == player:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0

        return False

    def check_vertical(self, row, col, player, board):
        """Checks if a player has 5 pieces in a row vertically

        Args:
            row int: player's row on the board
            column int: player's column on the board
            player str: player, 'X' or '0'

        Returns:
            bool: True if the player has 5 pieces vertically, False otherwise
        """
        count = 0

        for i in range(max(0, row-4), min(len(board.board), row+5)):
            if board.board[i][col] == player:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
        return False

    def check_diagonals(self, row, col, player, board):
        """Checks if a player has 5 pieces in a row diagonally

        Args:
            row (int): Player's row on the board
            col (int): Player's column on the board
            player (str): Player, 'X' or '0'

        Returns:
            bool: True if player has 5 pieces diagonally, False otherwise
        """

        # Checks diagonal from left to right (\)
        count = 0

        for i in range(-4, 5):

            if 0 <= row+i < len(board.board) and 0 <= col+i < len(board.board[0]):
                if board.board[row+i][col+i] == player:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0

        # Checks diagonal from right to left (/)
        count = 0

        for j in range(-4, 5):
            if 0 <= row+j < len(board.board) and 0 <= col-j < len(board.board[0]):
                if board.board[row+j][col-j] == player:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0

        return False

    def check_win(self, row, column, player, board):
        """Checks if a player has 5 pieces in a row after moving

        Args:
            row (int): Player's row on the board after move
            column (int): Player's column on the board after move
            player (str): Player who made the move

        Returns:
            bool: True if 5 pieces are found in a row, False otherwise
        """
        if self.check_horizontal(row, column, player, board) or \
                self.check_vertical(row, column, player, board) or \
                self.check_diagonals(row, column, player, board):
            return True

        return False
