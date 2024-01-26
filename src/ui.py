"""
Responsible for interactions with the user
"""

from random import choice
from services.board import Board
from services.logic import Logic


class UI:
    """Defines a simple user interface for the game
    """

    def __init__(self):
        self.board = Board()
        self.logic = Logic(self.board)

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

                    if self.logic.make_move(row_input, col_input, '0'):
                        print(
                            f"Succesfully moved to square ({row_input} and {col_input})")
                        self.board.print_board()
                        users_turn = False

                    if self.logic.check_win(row_input, col_input, '0'):
                        print("Game over! Thanks for playing.")
                        return
                except ValueError:
                    print('Please enter integers only!')
            else:
                # Testing purpose AI-here
                # This will be replaced later with a more complex AI

                empty_cells = [(i, j) for i in range(len(self.board.board)) for j in range(
                    len(self.board.board[0])) if self.board.board[i][j] == '-']
                if not empty_cells:
                    return

                row, column = choice(empty_cells)
                self.logic.make_move(row, column, 'X')
                print(f"AI moved to square ({row}, {column})")

                if self.logic.check_win(row, column, 'X'):
                    print("Game over! Thanks for playing.")
                    return

                self.board.print_board()
                users_turn = True
