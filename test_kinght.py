import unittest
from knight import Knight
from board import Board

class TestKnight(unittest.TestCase):
    """Clase de pruebas para la pieza Caballo."""

    def setUp(self):
        """Inicializa el tablero y coloca el caballo en el centro."""
        self.game_board = Board()
        self.knight_piece = Knight("WHITE", self.game_board)
        self.game_board.set_piece(4, 4, self.knight_piece)  # Colocación inicial del caballo

    # Verificar los símbolos de los caballos
    def test_knight_symbol_white(self):
        """Confirma que el símbolo para el caballo blanco sea correcto."""
        white_knight = Knight("WHITE", self.game_board)
        symbol_result = white_knight.symbol()
        expected_symbol = '♘'
        self.assertEqual(symbol_result, expected_symbol)

    def test_knight_symbol_black(self):
        """Confirma que el símbolo para el caballo negro sea correcto."""
        black_knight = Knight("BLACK", self.game_board)
        symbol_result = black_knight.symbol()
        expected_symbol = '♞'
        self.assertEqual(symbol_result, expected_symbol)

    # Testeo de movimientos válidos
    def test_L_shape_valid_moves(self):
        """Confirma que los movimientos válidos en forma de L sean aceptados."""
        valid_moves = [
            (6, 5), 
            (6, 3), 
            (5, 6), 
            (5, 2), 
            (3, 6), 
            (3, 2), 
            (2, 5), 
            (2, 3)
        ]
        self._validate_moves(valid_moves, expected_result=True)

    # Testeo de movimientos inválidos
    def test_invalid_moves(self):
        """Verifica que los movimientos que no son en L sean rechazados."""
        invalid_moves = [
            (4, 5), (5, 4), (6, 4), (4, 6)  # Movimientos que no son válidos
        ]
        self._validate_moves(invalid_moves, expected_result=False)

    def _validate_moves(self, moves, expected_result):
        """Valida una lista de movimientos."""
        for move in moves:
            target_row, target_col = move
            result = self.knight_piece.valid_positions(4, 4, target_row, target_col)
            self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
