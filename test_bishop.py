import unittest
from knight import Knight
from board import Board

class TestKnight(unittest.TestCase):
    """Clase de pruebas para el comportamiento de la pieza Caballo."""

    def setUp(self):
        """Inicializa el tablero y coloca el caballo en el centro."""
        self.board = Board()
        self.knight = Knight("WHITE", self.board)
        self.board.set_piece(4, 4, self.knight)  # Coloca el caballo en el centro

    # Testeo de símbolos
    def test_knight_symbol_white(self):
        """Verifica que el símbolo del caballo blanco sea el correcto."""
        self.assertEqual(self.knight.symbol(), '♘')

    def test_knight_symbol_black(self):
        """Verifica que el símbolo del caballo negro sea el correcto."""
        black_knight = Knight("BLACK", self.board)
        self.assertEqual(black_knight.symbol(), '♞')

    # Testeo de movimientos válidos
    def test_valid_positions_L_shape(self):
        """Confirma que los movimientos válidos en forma de L se acepten."""
        valid_moves = [
            (6, 5), (6, 3), (5, 6), (5, 2), 
            (3, 6), (3, 2), (2, 5), (2, 3)
        ]
        self._check_moves(valid_moves, True)

    # Testeo de movimientos inválidos
    def test_invalid_positions(self):
        """Verifica que los movimientos que no son en L sean rechazados."""
        invalid_moves = [
            (4, 5), (5, 4), (6, 4), (4, 6)  # Movimientos que no son válidos
        ]
        self._check_moves(invalid_moves, False)

    def _check_moves(self, moves, expected_result):
        """Verifica la validez de una lista de movimientos."""
        for move in moves:
            to_row, to_col = move
            self.assertEqual(self.knight.valid_positions(4, 4, to_row, to_col), expected_result)

if __name__ == '__main__':
    unittest.main()
