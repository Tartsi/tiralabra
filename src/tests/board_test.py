import io
import sys
import unittest
from services.board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_set_up_board_default(self):
        self.assertEqual(len(self.board.board), (20))
        self.assertEqual(len(self.board.moves_made), 0)

    def test_set_up_board_with_given_value(self):
        board = Board(5)
        self.assertEqual(len(board.board), (5))
        self.assertEqual(len(self.board.moves_made), 0)

    def test_make_legal_move(self):
        self.assertEqual(self.board.make_move(1, 1, "0"), True)
        self.assertEqual(self.board.moves_made[0], (1, 1, "-"))

    def test_make_illegal_move(self):
        self.board.make_move(1, 1, "0")
        self.assertFalse(self.board.make_move(1, 1, "0"))
        self.assertEqual(self.board.moves_made[0], (1, 1, "-"))

    def test_undo_move_empty_board(self):
        self.assertFalse(self.board.undo_move())

    def test_undo_move_after_legal_move(self):
        self.board.make_move(1, 1, "0")
        self.assertTrue(self.board.undo_move())

    def test_undo_move_after_illegal_move(self):
        self.board.make_move(1, 1, "0")
        self.board.make_move(1, 1, "0")
        self.assertTrue(self.board.undo_move())
        self.assertFalse(self.board.undo_move())
