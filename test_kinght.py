import unittest
from knight import Knight
from board import Board
class TestKnight(unittest.TestCase):
# Simbolos piezas caballos (blanco y negro)
    def test_knight_symbol_white(self):
        board = Board()
        knight = Knight("WHITE", board)
        self.assertEqual(knight.symbol(), '♘')
    def test_knight_symbol_black(self):
        board = Board()
        knight = Knight("BLACK", board)
        self.assertEqual(knight.symbol(), '♞')
# TESTEO MOVIMIENTOS
    def setUp(self):
        self.board = Board()
        self.knight = Knight("WHITE", self.board)
        self.board.set_piece(4, 4, self.knight)  # Coloca el caballo en el centro
    def test_valid_position_L_shape(self):
        # Movimientos válidos en forma de L
        valid_moves = [
            (6, 5), (6, 3), (5, 6), (5, 2), (3, 6), (3, 2), (2, 5), (2, 3)
        ]
        for move in valid_moves:
            to_row, to_col = move
            self.assertTrue(self.knight.valid_positions(4, 4, to_row, to_col))
    def test_invalid_position(self):
        # Movimientos no válidos
        invalid_moves = [
            (4, 5), (5, 4), (6, 4), (4, 6)  # Estos no son movimientos en L
        ]
        for move in invalid_moves:
            to_row, to_col = move
            self.assertFalse(self.knight.valid_positions(4, 4, to_row, to_col))
if __name__ == '__main__':
    unittest.main()