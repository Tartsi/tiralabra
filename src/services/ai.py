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

    def evaluate_board(self, board):
        """Evaluates the current board state and returns a value of it

        Args:
            board (board): Current board state

        Returns:
            int: Value of the current board state
        """
        score = 0

        for row in range(len(board.board)):

            for column in range(len(board.board)):

                if board.board[row][column] != "-":
                    player = board.board[row][column]
                    score_multiplier = 1 if player == "X" else -1
                    score += score_multiplier * \
                        self.evaluate_position(board, row, column, player)

        return score

    def evaluate_position(self, board, row, column, player):
        """Evaluates a position on the current board state and returns a value

        Args:
            board (board): Current board state
            row (int): Row number for the position
            column (int): Column number for the position
            player (str): Player whose position is to be evaluated

        Returns:
            int: Value for the position
        """

        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        pos_score = 0

        for delta_row, delta_column in directions:

            line_score, open_ends = self.evaluate_line(
                board, row, column, player, delta_row, delta_column)

            if line_score == 3 and open_ends == 0:
                pos_score += 0
            elif line_score == 3:
                pos_score += 50 if open_ends > 0 else 30
            elif line_score == 2:
                pos_score += 10 if open_ends == 2 else 5
            elif line_score == 1:
                pos_score += 3 if open_ends == 2 else 1
            else:
                pos_score += line_score * (1 + open_ends)

        return pos_score

    def evaluate_line(self, board, row, column, player, delta_row, delta_column):
        """Finds and returns potential line scores (consecutive pieces) and number of open ends

        Args:
            board (board): Current board state
            row (int): Row number of the position from which to evaluate
            column (int): Column number of the position from which to evaluate
            player (str): Player who is under evaluation
            delta_row (int): Determines the direction of the row to be evaluated
            delta_column (int): Determines the direction of the column to be evaluated

        Returns:
            int, int: Score of the position based on consecutive pieces and number of open ends
        """

        line_length = 0
        open_ends = 0

        for step in range(1, 5):
            # Check up to 4 steps in a given direction
            next_row = row + step * delta_row
            next_column = column + step * delta_column

            if 0 <= next_row < len(board.board) and 0 <= next_column < len(board.board[0]):
                if board.board[next_row][next_column] == player:
                    line_length += 1
                elif board.board[next_row][next_column] == '-':  # Empty == open end
                    open_ends += 1
                    break
                else:
                    break
            else:
                break

        return line_length, open_ends

    def update_possible_moves_for_simulation(self, latest_move, cloned_possible_moves, board):
        """Updates a cloned list of possible moves based on the latest simulated move in minimax

        Args:
            latest_move (tuple(int, int)): Row and column of the latest move made in the simulation
            cloned_possible_moves (list[tuple(int, int)]): Cloned list of possible moves
            board (Board): Current state of the board in the simulation
        """

        rows = range(
            max(0, latest_move[0] - 2), min(len(board.board), latest_move[0] + 3))
        cols = range(
            max(0, latest_move[1] - 2), min(len(board.board[0]), latest_move[1] + 3))

        for row in rows:

            for col in cols:

                if board.board[row][col] == "X" or board.board[row][col] == "0":
                    continue

                if board.board[row][col] == "-":

                    current_move = (row, col)

                    close = abs(
                        row - latest_move[0]) <= 1 and abs(col - latest_move[1]) <= 1

                    if current_move not in cloned_possible_moves:

                        if close:
                            cloned_possible_moves.append(current_move)
                        else:
                            cloned_possible_moves.insert(0, current_move)

        if latest_move in cloned_possible_moves:
            cloned_possible_moves.remove(latest_move)

    def minimax(self, depth, maximizing, board, alpha, beta, possible_moves):
        """Minimax-algorithm used for decision making

        Args:
            depth (int): How 'deep' the algorithm checks for potential moves
            maximizing (bool): True or False whether the algorithm tries to
            maximize potential outcome of the moves evaluation, or minimize it
            board (Board): Clone of the game board the AI uses during simulations
            alpha (int): The alpha cut-off for the alpha-beta pruning optimization
            beta (int): The beta cut-off for the alpha-beta pruning optimization
            possible_moves (list[tuple(int, int)]): List of all moves that can be made on the board

        Returns:
            int, tuple(int, int): 
            A evaluation score of the current board state
            and best possible move for each situation
        """

        if depth == 0:
            # Return evaluation score and no move
            return self.evaluate_board(board), None

        best_move = None

        # Hard code AI to X
        if maximizing:

            max_evaluation = float("-inf")

            # Reversed selection for optimized Alpha-Beta pruning
            for i in range(len(possible_moves) - 1, -1, -1):

                move = possible_moves[i]

                cloned_possible_moves = possible_moves.copy()

                board.make_move(move[0], move[1], "X")

                self.update_possible_moves_for_simulation(
                    move, cloned_possible_moves, board)

                if self.logic.check_win(move[0], move[1], "X", board):
                    # Immadetially return if winning move is found
                    board.undo_move()
                    return 100000, move

                made_evaluation, _ = self.minimax(
                    depth-1, False, board, alpha, beta, cloned_possible_moves)

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

            for i in range(len(possible_moves) - 1, -1, -1):

                move = possible_moves[i]

                cloned_possible_moves = possible_moves.copy()

                board.make_move(move[0], move[1], "0")

                if self.logic.check_win(move[0], move[1], "0", board):
                    # Inevitable loss
                    board.undo_move()
                    return -100000, best_move

                made_evaluation, _ = self.minimax(
                    depth-1, True, board, alpha, beta, cloned_possible_moves)

                board.undo_move()

                if made_evaluation < min_evaluation:
                    min_evaluation = made_evaluation
                    best_move = move

                beta = min(beta, made_evaluation)

                if beta <= alpha:
                    break

            return min_evaluation, best_move
