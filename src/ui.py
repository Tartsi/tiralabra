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
        self.all_moves_made = set()

    def start_game(self):
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
                        input("Row: "))-1
                    col_input = int(
                        input("Column: "))-1

                    if self.logic.make_move(row_input, col_input, '0', self.board):
                        print(
                            f"Moved to square ({row_input+1} and {col_input+1})")
                        self.all_moves_made.add((row_input, col_input))
                        self.board.print_board()
                        users_turn = False

                    if self.logic.check_win(row_input, col_input, '0', self.board):
                        print("0 won!")
                        print("Game over! Thanks for playing.")
                        return
                except Exception:
                    print('Invalid input, try again!')
            else:

                # AI always starts from the middle of the board
                if not self.all_moves_made:
                    start_point = (len(self.board.board) // 2)-1
                    self.board.make_move(start_point, start_point, 'X')
                    self.all_moves_made.add((start_point, start_point))
                    print(
                        f"AI moved to square ({start_point+1}, {start_point+1})")
                    self.board.print_board()
                    users_turn = True
                    continue

                cloned_board = deepcopy(self.board)

                row, column = self.ai.minimax(
                    2, True, cloned_board, float("-inf"), float("inf"), self.all_moves_made)[1]

                self.logic.make_move(row, column, "X", self.board)

                print(f"AI moved to square ({row+1}, {column+1})")

                self.all_moves_made.add((row, column))

                if self.logic.check_win(row, column, 'X', self.board):
                    self.board.print_board()
                    print("X won!")
                    print("Game over! Thanks for playing.")
                    return

                self.board.print_board()
                users_turn = True
