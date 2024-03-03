import unittest
from services.ai import AI
from services.logic import Logic
from services.board import Board
from ui import UI


class TestUI(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.logic = Logic()
        self.ai = AI()
        self.ui = UI(self.board, self.logic, self.ai)

    def testPossibleMoves(self):

        expected_moves = [
            (12, 12), (12, 11), (12, 10), (12, 9), (12, 8),
            (11, 12), (11, 8), (10, 12), (10, 8), (9, 12),
            (9, 8), (8, 12), (8, 11), (8, 10), (8, 9),
            (8, 8), (9, 9), (9, 10), (9, 11), (10, 9),
            (10, 11), (11, 9), (11, 10), (11, 11)
        ]

        self.ui.update_possible_moves((10, 10))
        self.assertEqual(self.ui.possible_moves, expected_moves)
