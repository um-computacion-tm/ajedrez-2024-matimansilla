import unittest
from rook import Rook
from board import Board

class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rook = Rook('WHITE', self.board)

    def test_move_vertical_asc(self):
        self.board.place_piece(self.rook, 4, 1)
        possibles = self.rook.possible_positions_va(4, 1)
        self.assertEqual(possibles, [(3, 1), (2, 1), (1, 1), (0, 1)])

    def test_move_vertical_desc(self):
        self.board.place_piece(self.rook, 4, 1)
        possibles = self.rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1), (6, 1), (7, 1)])

    def test_move_vertical_desc_with_not_own_piece(self):
        other_piece = Rook('BLACK', self.board)
        self.board.place_piece(self.rook, 4, 1)
        self.board.place_piece(other_piece, 5, 1)
        possibles = self.rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1)])

    def test_move_vertical_desc_with_own_piece(self):
        self.board.place_piece(self.rook, 4, 1)
        self.board.place_piece(Rook('WHITE', self.board), 5, 1)
        possibles = self.rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [])

    def test_str(self):
        self.assertEqual(str(self.rook), "♖")

if __name__ == '__main__':
    unittest.main()
