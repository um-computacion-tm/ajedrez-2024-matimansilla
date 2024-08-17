import unittest
from board import Board
from rook import Rook  # Ajusta el import si 'Rook' está en otro módulo

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_get_piece(self):
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsNone(self.board.get_piece(2, 0))

    def test_rooks_creation(self):
        rooks_positions = [
            (0, 0, 'BLACK'), (0, 7, 'BLACK'),
            (7, 0, 'WHITE'), (7, 7, 'WHITE')
        ]
        for row, col, color in rooks_positions:
            piece = self.board.get_piece(row, col)
            self.assertIsInstance(piece, Rook)
            self.assertEqual(piece.__color__, color)

    def test_empty_spaces(self):
        empty_rows = [2, 3, 4, 5]
        for row in empty_rows:
            for col in range(8):
                self.assertIsNone(self.board.get_piece(row, col))

if __name__ == '__main__':
    unittest.main()

