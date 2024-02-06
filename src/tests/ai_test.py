import unittest
from services.ai import AI


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.ai = AI()

    def test_consecutive_count_empty_board(self):
        self.assertEqual(self.ai.count_consecutive(0, 0, "X", 1, 1), 0)

    def test_consecutive_count_single_filled_board(self):
        self.ai.board.make_move(1, 1, "X")
        self.assertEqual(self.ai.count_consecutive(0, 0, "X", 1, 1), 1)

    def test_consecutive_count_multi_filled_board(self):
        self.ai.board.make_move(1, 1, "X")
        self.ai.board.make_move(2, 2, "X")
        self.ai.board.make_move(3, 3, "X")
        self.ai.board.make_move(4, 4, "X")
        self.assertEqual(self.ai.count_consecutive(0, 0, "X", 1, 1), 4)

    def test_evaluate_empty_board(self):
        self.assertEqual(self.ai.evaluate_board(self.ai.board), 0)

    def test_evaluate_X_filled_board(self):
        self.ai.board.make_move(1, 1, "X")
        self.ai.board.make_move(2, 2, "X")
        self.assertEqual(self.ai.evaluate_board(self.ai.board), 1)

    def test_evaluate_0_filled_board(self):
        self.ai.board.make_move(1, 1, "0")
        self.ai.board.make_move(2, 2, "0")
        self.assertEqual(self.ai.evaluate_board(self.ai.board), -1)

    def test_get_possible_moves_empty_board(self):
        board = self.ai.board
        expected_possible_moves = 1
        self.assertEqual(len(self.ai.get_possible_moves(board, [])),
                         expected_possible_moves)

    def test_get_possible_moves_non_empty_board(self):
        board = self.ai.board
        board.make_move(1, 1, "0")
        expected_possible_moves = 8
        self.assertEqual(len(self.ai.get_possible_moves(board, [(1, 1)])),
                         expected_possible_moves)
