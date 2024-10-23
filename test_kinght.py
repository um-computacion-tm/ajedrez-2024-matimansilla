import unittest
from knight import Knight
from board import Board

class TestKnight(unittest.TestCase):
    # Verificar los símbolos de los caballos
    def test_white_knight_symbol(self):
        game_board = Board()
        white_knight = Knight("WHITE", game_board)
        self.assertEqual(white_knight.symbol(), '♘')

    def test_black_knight_symbol(self):
        game_board = Board()
        black_knight = Knight("BLACK", game_board)
        self.assertEqual(black_knight.symbol(), '♞')

    # TEST DE MOVIMIENTOS
    def setUp(self):
        self.game_board = Board()
        self.knight_piece = Knight("WHITE", self.game_board)
        self.game_board.set_piece(4, 4, self.knight_piece)  # Colocación inicial del caballo

    def test_valid_moves_L_shape(self):
        # Verificar movimientos válidos en forma de L
        valid_positions = [
            (6, 5), (6, 3), (5, 6), (5, 2), (3, 6), (3, 2), (2, 5), (2, 3)
        ]
        for position in valid_positions:
            target_row, target_col = position
            self.assertTrue(self.knight_piece.valid_positions(4, 4, target_row, target_col))

    def test_invalid_moves(self):
        # Comprobar movimientos no válidos
        invalid_positions = [
            (4, 5), (5, 4), (6, 4), (4, 6)  # Movimientos no en forma de L
        ]
        for position in invalid_positions:
            target_row, target_col = position
            self.assertFalse(self.knight_piece.valid_positions(4, 4, target_row, target_col))

if __name__ == '__main__':
    unittest.main()
