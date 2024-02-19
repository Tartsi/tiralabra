"""
Responsible for interactions with the user
"""

from copy import deepcopy


class UI:
    """Defines a simple user interface for the game
    """

    def __init__(self, board, logic, ai):
        self.board = board
        self.logic = logic
        self.ai = ai
        self.all_moves_made = set()

    def display_board_numbers(self, board):
        """Generates row and column numbers for the board

        Args:
            board (board): Board-object to add row and column numbers to
        """

        # ChatGPT - Entire purpose of this function is better playability for users

        column_headers = '   ' + \
            ' '.join(str(i).rjust(2)
                     for i in range(1, len(board.board[0]) + 1))
        print(column_headers)

        for i, row in enumerate(board.board, start=1):
            row_display = f"{str(i).rjust(2)} " + \
                ' '.join(str(cell).rjust(2) for cell in row)
            print(row_display)

    def start_game(self):
        """Starts the game
        """

        print("\n- Starting the game! AI (X) moves first!\n")
        print("- First to reach 5 pieces in a row on the board wins the game!\n")
        print("- Give your squares in order as a number after 'Choice' (row and column).\n")
        print("- The game is 1-indexed, first row is 1 and last row 20.\n")
        users_turn = False

        while True:

            if users_turn:

                print("\nPress anything to enter square, 0 to exit game.")

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
                            f"Moved to square ({row_input+1} and {col_input+1})\n")
                        self.all_moves_made.add((row_input, col_input))
                        self.display_board_numbers(self.board)
                        users_turn = False

                    if self.logic.check_win(row_input, col_input, '0', self.board):
                        print("\n0 won!")
                        print("Game over! Thanks for playing.")
                        return
                except Exception as e:
                    print('Invalid input, try again!', e, "\n")
            else:

                # AI always starts from the middle of the board
                if not self.all_moves_made:
                    start_point = (len(self.board.board) // 2)-1
                    self.board.make_move(start_point, start_point, 'X')
                    self.all_moves_made.add((start_point, start_point))
                    print(
                        f"\nAI moved to square ({start_point+1}, {start_point+1})\n")
                    self.display_board_numbers(self.board)
                    users_turn = True
                    continue

                cloned_board = deepcopy(self.board)

                row, column = self.ai.minimax(
                    2, True, cloned_board, float("-inf"), float("inf"), self.all_moves_made)[1]

                self.logic.make_move(row, column, "X", self.board)

                print(f"\nAI moved to square ({row+1}, {column+1})\n")

                self.all_moves_made.add((row, column))

                if self.logic.check_win(row, column, 'X', self.board):
                    self.display_board_numbers(self.board)
                    print("\nX won!")
                    print("Game over! Thanks for playing.")
                    return

                self.display_board_numbers(self.board)
                users_turn = True
