import unittest
from services.ai import AI
from services.board import Board
from services.logic import Logic
from ui import UI


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.logic = Logic()
        self.ai = AI()
        self.ui = UI(self.board, self.logic, self.ai)

    def test_update_possible_moves_for_simulation(self):

        self.board.make_move(10, 10, "X")
        clone = []
        self.ai.update_possible_moves_for_simulation(
            (10, 10), clone, self.board)

        expected_moves = [(8, 8), (8, 9), (8, 10), (8, 11), (8, 12),
                          (9, 8), (9, 9), (9, 10), (9, 11), (9, 12),
                          (10, 8), (10, 9), (10, 11), (10, 12),
                          (11, 8), (11, 9), (11, 10), (11, 11), (11, 12),
                          (12, 8), (12, 9), (12, 10), (12, 11), (12, 12)]

        self.assertEqual(expected_moves, clone)

    def test_minimax_take_winning_move(self):

        self.board.make_move(9, 9, "X")
        self.ui.update_possible_moves((9, 9))
        self.board.make_move(10, 10, "X")
        self.ui.update_possible_moves((10, 10))
        self.board.make_move(11, 11, "X")
        self.ui.update_possible_moves((11, 11))
        self.board.make_move(12, 12, "X")
        self.ui.update_possible_moves((12, 12))

        result_move = self.ai.minimax(
            2, True, self.board,
            float("-inf"), float("inf"), self.ui.possible_moves
        )

        self.assertEqual(result_move, (float("inf"), (13, 13)))

    def test_minimax_build_2_line(self):
        self.board.make_move(10, 10, "X")
        self.ui.update_possible_moves((10, 10))
        self.board.make_move(9, 10, "0")
        self.ui.update_possible_moves((9, 10))

        result_move = self.ai.minimax(
            2, True, self.board,
            float("-inf"), float("inf"), self.ui.possible_moves
        )

        self.assertEqual(result_move, (0, (11, 11)))

    def test_minimax_build_3_line(self):
        self.board.make_move(10, 10, "X")
        self.ui.update_possible_moves((10, 10))
        self.board.make_move(9, 10, "0")
        self.ui.update_possible_moves((9, 10))
        self.board.make_move(10, 11, "X")
        self.ui.update_possible_moves((10, 11))
        self.board.make_move(8, 10, "0")
        self.ui.update_possible_moves((8, 10))

        result_move = self.ai.minimax(
            2, True, self.board,
            float("-inf"), float("inf"), self.ui.possible_moves
        )

        self.assertEqual(result_move, (0, (10, 12)))

    def test_minimax_build_4_line(self):
        self.board.make_move(10, 10, "X")
        self.ui.update_possible_moves((10, 10))
        self.board.make_move(9, 10, "0")
        self.ui.update_possible_moves((9, 10))
        self.board.make_move(10, 11, "X")
        self.ui.update_possible_moves((10, 11))
        self.board.make_move(8, 10, "0")
        self.ui.update_possible_moves((8, 10))
        self.board.make_move(10, 12, "X")
        self.ui.update_possible_moves((10, 12))
        self.board.make_move(7, 10, "0")
        self.ui.update_possible_moves((7, 10))

        result_move = self.ai.minimax(
            2, True, self.board,
            float("-inf"), float("inf"), self.ui.possible_moves
        )

        self.assertEqual(result_move, (20, (10, 13)))

    def test_minimax_return_none_on_guaranteed_loss(self):
        self.board.make_move(13, 10, "X")
        self.ui.update_possible_moves((13, 10))
        self.board.make_move(9, 10, "0")
        self.ui.update_possible_moves((9, 10))
        self.board.make_move(10, 11, "X")
        self.ui.update_possible_moves((10, 11))
        self.board.make_move(8, 10, "0")
        self.ui.update_possible_moves((8, 10))
        self.board.make_move(10, 12, "X")
        self.ui.update_possible_moves((10, 12))
        self.board.make_move(7, 10, "0")
        self.ui.update_possible_moves((7, 10))
        self.board.make_move(1, 1, "X")
        self.ui.update_possible_moves((1, 1))
        self.board.make_move(6, 10, "0")
        self.ui.update_possible_moves((6, 10))

        result_move = self.ai.minimax(
            2, True, self.board,
            float("-inf"), float("inf"), self.ui.possible_moves
        )

        self.assertEqual(result_move, (float("-inf"), None))

    def test_evaluate_empty_board(self):
        self.assertEqual(self.ai.evaluate_board(self.board), 0)

    def test_evaluate_2_X_filled_board(self):
        self.board.make_move(1, 1, "X")
        self.board.make_move(2, 1, "X")
        self.assertEqual(self.ai.evaluate_board(self.board), 1)

    def test_evaluate_3_X_filled_board(self):
        self.board.make_move(1, 1, "X")
        self.board.make_move(2, 1, "X")
        self.board.make_move(3, 1, "X")
        self.assertEqual(self.ai.evaluate_board(self.board), 6)

    def test_evaluate_4_X_filled_board(self):
        self.board.make_move(1, 1, "X")
        self.board.make_move(2, 1, "X")
        self.board.make_move(3, 1, "X")
        self.board.make_move(4, 1, "X")
        self.assertEqual(self.ai.evaluate_board(self.board), 56)

    def test_evaluate_0_filled_board(self):
        self.board.make_move(1, 1, "0")
        self.board.make_move(2, 1, "0")
        self.assertEqual(self.ai.evaluate_board(self.board), -1)

    def test_evaluate_correct_no_open_ends_in_direction(self):
        self.board.make_move(8, 9, "X")
        self.board.make_move(8, 10, "X")
        self.board.make_move(8, 11, "X")
        self.board.make_move(8, 12, "X")
        self.board.make_move(8, 13, "0")
        self.board.make_move(8, 14, "0")
        self.assertEqual(self.ai.evaluate_line(
            self.board, 8, 9, "X", 0, 1), (3, 0))

    def test_evaluate_correct_1_open_end(self):
        self.board.make_move(0, 0, "X")
        self.board.make_move(1, 0, "X")
        self.board.make_move(1, 1, "X")
        self.assertEqual(self.ai.evaluate_line(
            self.board, 0, 0, "X", 1, 0), (1, 1))

    def test_evaluate_correct_2_open_ends(self):
        self.board.make_move(5, 5, "X")
        self.assertEqual(self.ai.evaluate_line(
            self.board, 5, 5, "X", 1, 0), (0, 1))
        self.assertEqual(self.ai.evaluate_line(
            self.board, 5, 5, "X", 0, 1), (0, 1))

    def test_evaluate_corner_piece(self):
        self.board.make_move(19, 19, "X")
        self.assertEqual(self.ai.evaluate_line(
            self.board, 19, 19, "X", 0, 0), (4, 0))

    def test_line_evaluation_out_of_bounds(self):
        self.assertEqual(self.ai.evaluate_line(
            self.board, 20, 20, "X", 0, 0), (0, 0))
