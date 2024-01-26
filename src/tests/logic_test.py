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

    def test_check_horizontal_win(self):
        self.logic.make_move(0, 0, "X")
        self.logic.make_move(0, 1, "X")
        self.logic.make_move(0, 2, "X")
        self.logic.make_move(0, 3, "X")
        self.logic.make_move(0, 4, "X")
        self.assertTrue(self.logic.check_horizontal(0, 0, 'X'))

    def test_check_horizontal_no_win(self):
        self.logic.make_move(0, 0, "X")
        self.logic.make_move(0, 1, "X")
        self.logic.make_move(0, 2, "X")
        self.logic.make_move(0, 3, "X")
        self.assertFalse(self.logic.check_horizontal(0, 0, 'X'))

    def test_check_vertical_win(self):
        self.logic.make_move(0, 0, "X")
        self.logic.make_move(1, 0, "X")
        self.logic.make_move(2, 0, "X")
        self.logic.make_move(3, 0, "X")
        self.logic.make_move(4, 0, "X")
        self.assertTrue(self.logic.check_vertical(0, 0, 'X'))

    def test_check_vertical_no_win(self):
        self.logic.make_move(0, 0, "X")
        self.logic.make_move(1, 0, "X")
        self.logic.make_move(2, 0, "X")
        self.logic.make_move(3, 0, "X")
        self.assertFalse(self.logic.check_vertical(0, 0, 'X'))

    def test_check_diagonals_win_left_to_right(self):
        self.logic.make_move(0, 0, "X")
        self.logic.make_move(1, 1, "X")
        self.logic.make_move(2, 2, "X")
        self.logic.make_move(3, 3, "X")
        self.logic.make_move(4, 4, "X")
        self.assertTrue(self.logic.check_diagonals(0, 0, 'X'))

    def test_check_diagonals_no_win_left_to_right(self):
        self.logic.make_move(0, 0, "X")
        self.logic.make_move(1, 1, "X")
        self.logic.make_move(2, 2, "X")
        self.logic.make_move(3, 3, "X")
        self.assertFalse(self.logic.check_diagonals(0, 0, 'X'))

    def test_check_diagonals_win_right_to_left(self):
        self.logic.make_move(19, 0, "X")
        self.logic.make_move(18, 1, "X")
        self.logic.make_move(17, 2, "X")
        self.logic.make_move(16, 3, "X")
        self.logic.make_move(15, 4, "X")
        self.assertTrue(self.logic.check_diagonals(19, 0, 'X'))

    def test_check_diagonals_no_win_right_to_left(self):
        self.logic.make_move(19, 0, "X")
        self.logic.make_move(18, 1, "X")
        self.logic.make_move(17, 2, "X")
        self.logic.make_move(16, 3, "X")
        self.assertFalse(self.logic.check_diagonals(19, 0, 'X'))

    def test_check_win_after_winning_move(self):
        self.logic.make_move(0, 0, "X")
        self.logic.make_move(1, 0, "X")
        self.logic.make_move(2, 0, "X")
        self.logic.make_move(3, 0, "X")
        self.logic.make_move(4, 0, "X")
        self.assertTrue(self.logic.check_win(0, 0, 'X'))

    def test_check_win_after_normal_move(self):
        self.logic.make_move(0, 0, "X")
        self.logic.make_move(1, 0, "X")
        self.logic.make_move(2, 0, "X")
        self.logic.make_move(3, 0, "X")
        self.assertFalse(self.logic.check_win(0, 0, 'X'))
