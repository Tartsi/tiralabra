import unittest
from services.logic import Logic
from services.board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.logic = Logic(Board())

    def test_make_legal_move(self):
        self.assertEqual(self.logic.make_move(1, 1, "0"), True)

    def test_make_illegal_move(self):
        self.logic.make_move(1, 1, "0")
        self.assertFalse(self.logic.make_move(1, 1, "0"))

    def test_make_move_out_of_bounds_row(self):
        self.assertFalse(self.logic.make_move(20, 1, "0"))

    def test_make_move_out_of_bounds_column(self):
        self.assertFalse(self.logic.make_move(1, 20, "0"))

    def test_draw_if_board_full(self):
        logic = Logic(Board(2))
        logic.make_move(0, 0, "0")
        logic.make_move(0, 1, "X")
        logic.make_move(1, 0, "0")
        logic.make_move(1, 1, "X")
        self.assertTrue(logic.check_draw())

    def test_draw_if_board_not_full(self):
        self.assertFalse(self.logic.check_draw())
