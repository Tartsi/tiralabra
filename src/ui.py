"""
Responsible for interactions with the user
"""

from copy import deepcopy
from services.ai import AI
from services.board import Board
from services.logic import Logic


class UI:
    """Defines a simple user interface for the game
    """

    def __init__(self):
        self.board = Board()
        self.logic = Logic()
        self.ai = AI()

    def start(self):
        """Starts the game
        """

        print("Starting the game! X moves first!")
        print("Give your squares as a row and column.\n")
        users_turn = False

        while True:

            if users_turn:

                print("Press anything to enter square, 0 to exit game.")

                try:

                    decision = input("Choice: ")

                    if decision == '0':
                        return

                    print()
                    row_input = int(
                        input("Enter your row number please: "))
                    col_input = int(
                        input("Enter your column number please: "))

                    if self.logic.make_move(row_input, col_input, '0', self.board):
                        print(
                            f"Succesfully moved to square ({row_input} and {col_input})")
                        self.board.print_board()
                        users_turn = False

                    if self.logic.check_win(row_input, col_input, '0', self.board):
                        print("0 won!")
                        print("Game over! Thanks for playing.")
                        return
                except Exception:
                    print('Invalid input, try again!')
            else:

                cloned_board = deepcopy(self.board)

                row, column = self.ai.minimax(
                    2, True, cloned_board, float("-inf"), float("inf"))[1]

                self.logic.make_move(row, column, "X", self.board)

                print(f"AI moved to square ({row}, {column})")

                if self.logic.check_win(row, column, 'X', self.board):
                    print("X won!")
                    print("Game over! Thanks for playing.")
                    return

                self.board.print_board()
                users_turn = True
