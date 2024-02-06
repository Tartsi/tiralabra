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

    def get_possible_moves(self, board, all_moves_made):
        """Returns a set of possible moves

        Args:
            board (board): Board to get possible moves from
            all_moves_made (set()): Set/List to hold possible move set

        Returns:
            set(): Set of possible moves
        """

        if not all_moves_made:
            start_point = (len(board.board) // 2)-1
            return [(start_point, start_point)]

        # Use sets for faster lookups O(1) for later usage
        possible_moves = set()

        for move in all_moves_made:
            row, column = move

            for i in range(max(0, row - 2), min(len(board.board), row + 3)):

                for j in range(max(0, column - 2), min(len(board.board), column + 3)):

                    if board.board[i][j] == "-":
                        possible_moves.add((i, j))

        return possible_moves

    def minimax(self, depth, maximizing, board, alpha, beta, all_moves_made):
        """Minimax-algorithm used for decision making

        Args:
            depth (int): How 'deep' the algorithm checks for potential moves
            maximizing (bool): True or False whether the algorithm tries to
            maximize potential outcome of the moves evaluation, or minimize it
            board (Board): Clone of the game board the AI uses during simulations
            alpha (int): The alpha cut-off for the alpha-beta pruning optimization
            beta (int): The beta cut-off for the alpha-beta pruning optimization
        """

        if depth == 0:
            # Return evaluation score and no move
            return self.evaluate_board(board), None

        best_move = None

        # Hard code AI to X for now
        if maximizing:

            max_evaluation = float("-inf")

            for move in self.get_possible_moves(board, all_moves_made):

                board.make_move(move[0], move[1], "X")

                if self.logic.check_win(move[0], move[1], "X", board):
                    made_evaluation = 100
                else:
                    made_evaluation, _ = self.minimax(
                        depth-1, False, board, alpha, beta, all_moves_made)

                board.undo_move()

                if made_evaluation > max_evaluation:
                    max_evaluation = made_evaluation
                    best_move = move

                alpha = max(alpha, made_evaluation)

                if beta <= alpha:
                    break

            return max_evaluation, best_move
        else:

            min_evaluation = float("inf")

            for move in self.get_possible_moves(board, all_moves_made):

                board.make_move(move[0], move[1], "0")

                if self.logic.check_win(move[0], move[1], "0", board):
                    made_evaluation = -100
                else:
                    made_evaluation, _ = self.minimax(
                        depth-1, False, board, alpha, beta, all_moves_made)

                board.undo_move()

                if made_evaluation < min_evaluation:
                    min_evaluation = made_evaluation
                    best_move = move

                beta = min(beta, made_evaluation)

                if beta <= alpha:
                    break

            return min_evaluation, best_move
