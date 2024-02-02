"""
This module is the 'brain' for the AI
"""

from services.board import Board
from services.logic import Logic


class AI():
    """
    Encompasses the algorithms the AI will use for its decisions
    """

    def __init__(self):
        """Initialize the AI
        """
        self.board = Board()
        self.logic = Logic()
        self.made_moves = 0

    def evaluate_board(self, board):
        """
        Evaluates the current board state from AI's perspective
        """

        score = 0

        for row in range(len(board.board)):

            for column in range(len(board.board)):

                if self.board.board[row][column] == "X":  # 'X' Hard coded for AI
                    score += self.evaluate_position(row, column, "X")
                elif self.board.board[row][column] == "0":
                    score -= self.evaluate_position(row, column, "0")

        return score

    def evaluate_position(self, row, column, player):
        """Evaluates a singular position from AI's perspective

        Args:
            row (int): Row of the square to be evaluated on game board
            column (int): Column of the square to be evaluated on game board
            player (str): Player to be evaluated on game board
        """

        # Very simple implementation for now, can be improved

        score = 0

        # Encompasses vertical, horizontal and diagonal positions
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for delta_row, delta_column in directions:
            score += self.count_consecutive(row,
                                            column, player, delta_row, delta_column)

        return score

    def count_consecutive(self, row, column, player, delta_row, delta_column):
        """Counts the number of consecutive pieces from a given position
           Helper function for evaluating a move's value

        Args:
            row (int): Row to start the count from
            column (int): Column to start the count from
            player (str): Player whose move is being evaluated
            delta_row (int): Row direction
            delta_column (int): Column direction
        """

        count = 0

        for _ in range(4):
            row += delta_row
            column += delta_column

            if (0 <= row < len(self.board.board) and
                0 <= column < len(self.board.board) and
                    self.board.board[row][column] == player):
                count += 1
            else:
                break

        return count

    def get_possible_moves(self, board):
        """Returns a set of possible moves"""
        # Move Pruning Optimization will be applied here

        # Use sets for faster lookups O(1) for later usage
        possible_moves = set()

        for row in range(len(board.board)):

            for column in range(len(board.board)):

                if board.board[row][column] == '-':

                    possible_moves.add((row, column))

        return possible_moves

    # def minimax(self, depth, maximizing, board):
    #     """Minimax-algorithm used for decision making

    #     Args:
    #         depth (int): How 'deep' the algorithm checks for potential moves
    #         maximizing (bool): True or False whether the algorithm tries to
    #         maximize potential outcome of the moves evaluation, or minimize it
    #         board (Board): Clone of the game board the AI uses during simulations
    #     """
    #     # first without alpha-beta pruning

    #     if depth == 0:
    #         return self.evaluate_board(board)

    #     best_move = None

    #     # Hard code AI to X for now
    #     if maximizing:

    #         max_evaluation = float("-inf")

    #         for move in self.get_possible_moves(board):

    #             board.make_move(move[0], move[1], "X")

    #             if self.logic.check_win(move[0], move[1], "X", board):
    #                 made_evaluation = 100
    #             else:
    #                 made_evaluation = self.minimax(depth-1, False, board)

    #             board.undo_move()

    #             if made_evaluation > max_evaluation:
    #                 max_evaluation = made_evaluation
    #                 best_move = move
    #     else:

    #         min_evaluation = float("inf")

    #         for move in self.get_possible_moves(board):

    #             board.make_move(move[0], move[1], "0")

    #             if self.logic.check_win(move[0], move[1], "0", board):
    #                 made_evaluation = -100
    #             else:
    #                 made_evaluation = self.minimax(depth-1, False, board)

    #             board.undo_move()

    #             if made_evaluation < min_evaluation:
    #                 min_evaluation = made_evaluation
    #                 best_move = move

    #     return best_move
