import unittest
from board import Board
from rook import Rook
from exceptions import InvalidMoveRookMove

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_move_vertical_desc(self):
        rook = Rook(white=True)
        self.board.place_piece(rook, 4, 1)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(3, 1), (2, 1), (1, 1), (0, 1)])

    def test_move_vertical_asc(self):
        rook = Rook(white=True)
        self.board.place_piece(rook, 4, 1)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(possibles, [(5, 1), (6, 1), (7, 1)])

    def test_move_vertical_desc_with_own_piece(self):
        rook = Rook(white=True)
        pawn = Rook(white=True)  # Usamos una torre blanca como obstrucción
        self.board.place_piece(rook, 4, 1)
        self.board.place_piece(pawn, 2, 1)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(3, 1)])

    def test_move_vertical_desc_with_not_own_piece(self):
        rook = Rook(white=True)
        pawn = Rook(white=False)  # Usamos una torre negra como obstrucción
        self.board.place_piece(rook, 4, 1)
        self.board.place_piece(pawn, 2, 1)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(3, 1), (2, 1)])

    def test_move_horizontal_right(self):
        rook = Rook(white=True)
        self.board.place_piece(rook, 4, 1)
        possibles = rook.possible_positions_hr(4, 1)
        self.assertEqual(possibles, [(4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)])

    def test_move_horizontal_right_with_own_piece(self):
        rook = Rook(white=True)
        pawn = Rook(white=True)
        self.board.place_piece(rook, 4, 1)
        self.board.place_piece(pawn, 4, 3)
        possibles = rook.possible_positions_hr(4, 1)
        self.assertEqual(possibles, [(4, 2)])

    def test_move_horizontal_right_with_not_own_piece(self):
        rook = Rook(white=True)
        pawn = Rook(white=False)
        self.board.place_piece(rook, 4, 1)
        self.board.place_piece(pawn, 4, 3)
        possibles = rook.possible_positions_hr(4, 1)
        self.assertEqual(possibles, [(4, 2), (4, 3)])

    def test_move_horizontal_left(self):
        rook = Rook(white=True)
        self.board.place_piece(rook, 4, 4)
        possibles = rook.possible_positions_hl(4, 4)
        self.assertEqual(possibles, [(4, 3), (4, 2), (4, 1), (4, 0)])

    def test_move_diagonal(self):
        rook = Rook(white=True)
        self.board.place_piece(rook, 0, 0)
        with self.assertRaises(InvalidMoveRookMove):
            is_possible = rook.valid_positions(0, 0, 1, 1)  # Intentamos mover la torre diagonalmente.

    def test_str(self):
        rook = Rook(white=True)
        self.assertEqual(str(rook), "♖")  # El símbolo para la torre blanca es ♖.

if __name__ == '__main__':
    unittest.main()
