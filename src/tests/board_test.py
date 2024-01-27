import io
import sys
import unittest
from services.board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_set_up_board_default(self):
        self.assertEqual(len(self.board.board), (20))

    def test_set_up_board_with_given_value(self):
        board = Board(5)
        self.assertEqual(len(board.board), (5))

    def test_make_legal_move(self):
        self.assertEqual(self.board.make_move(1, 1, "0"), True)

    def test_make_illegal_move(self):
        self.board.make_move(1, 1, "0")
        self.assertFalse(self.board.make_move(1, 1, "0"))

    def test_board_print_empty(self):
        sys.stdout = io.StringIO()
        board = Board(3)
        board.print_board()
        expected = "- - -\n- - -\n- - -\n\n"
        self.assertEqual(sys.stdout.getvalue(), expected)

    def test_board_print_after_legal_move(self):
        sys.stdout = io.StringIO()
        board = Board(3)
        board.make_move(1, 1, "0")
        board.print_board()
        expected = "- - -\n- 0 -\n- - -\n\n"
        self.assertEqual(sys.stdout.getvalue(), expected)

    def test_board_print_after_illegal_move(self):
        sys.stdout = io.StringIO()
        board = Board(3)
        board.make_move(1, 1, "0")
        board.make_move(1, 1, "0")
        board.print_board()
        expected = "- - -\n- 0 -\n- - -\n\n"
        self.assertEqual(sys.stdout.getvalue(), expected)

    def test_get_possible_moves_empty_board(self):
        board = Board(3)
        expected_possible_moves = 9
        self.assertEqual(len(board.get_possible_moves()),
                         expected_possible_moves)

    def test_get_possible_moves_non_empty_board(self):
        board = Board(3)
        board.make_move(1, 1, "0")
        expected_possible_moves = 8
        self.assertEqual(len(board.get_possible_moves()),
                         expected_possible_moves)
