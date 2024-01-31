# """
# This module is the 'brain' for the AI
# """

# # Used to generate a copy of the board for minimax-simulation
# # from copy import deepcopy

# from services.board import Board
# from services.logic import Logic


# class AI():
#     """
#     Encompasses the algorithms the AI will use for its decisions
#     """

#     def __init__(self):
#         """Initialize the AI
#         """
#         self.board = Board()
#         self.logic = Logic(self.board)
#         self.made_moves = 0

#     # def choose_best_move(self):
#     #     # this is what is called in the UI
#     #     pass

#     # def evaluate_board(self):
#     #     # evaluates each possible move
#     #     pass

# def minimax(self, depth, maximizing):
#     """Minimax-algorithm used for decision making

#     Args:
#         depth (int): How 'deep' the algorithm checks for potential moves
#         maximizing (bool): True or False whether the algorithm tries to
#         maximize potential outcome of the moves evaluation, or minimize it
#     """
#     # first without alpha-beta pruning

#     if depth == 0 or self.logic.check_win():  # Check win? Needs arguments
#         return  # evaluation

#     cloned_board = deepcopy(self.board)

#     if maximizing:
#         max_evaluation = float("-inf")
#         for move in self.board.get_possible_moves():
#             # Hard code AI to X for now
#             cloned_board.make_move(move[0], move[1], "X")
#             # This is where evaluation happens!
#             cloned_board.undo_move()
#             max_evaluation = max(max_evaluation, made_evaluation)
#     else:
#         min_evaluation = float("inf")
#         pass
