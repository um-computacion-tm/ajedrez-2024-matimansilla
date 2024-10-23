import unittest
from knight import Knight
from board import Board

class TestKnight(unittest.TestCase):
    """Clase de pruebas para la pieza Caballo en el juego de ajedrez."""

    # Verificación de los símbolos correspondientes a los caballos (blanco y negro)
    def test_knight_symbol_white(self):
        board = Board()  # Crea un nuevo tablero de ajedrez
        knight = Knight("WHITE", board)  # Inicializa un caballo blanco
        self.assertEqual(knight.symbol(), '♘')  # Comprueba que el símbolo del caballo blanco sea correcto

    def test_knight_symbol_black(self):
        board = Board()  # Crea un nuevo tablero de ajedrez
        knight = Knight("BLACK", board)  # Inicializa un caballo negro
        self.assertEqual(knight.symbol(), '♞')  # Comprueba que el símbolo del caballo negro sea correcto

    # Métodos de configuración para las pruebas de movimientos
    def setUp(self):
        self.board = Board()  # Inicializa un nuevo tablero antes de cada prueba
        self.knight = Knight("WHITE", self.board)  # Crea un caballo blanco
        self.board.set_piece(4, 4, self.knight)  # Ubica el caballo en la posición central

    def test_valid_position_L_shape(self):
        # Evaluación de movimientos válidos en forma de L
        valid_moves = [
            (6, 5), (6, 3), (5, 6), (5, 2), (3, 6), (3, 2), (2, 5), (2, 3)
        ]
        for move in valid_moves:
            to_row, to_col = move
            self.assertTrue(self.knight.valid_positions(4, 4, to_row, to_col))  # Verifica que cada movimiento sea válido

    def test_invalid_position(self):
        # Evaluación de movimientos no permitidos
        invalid_moves = [
            (4, 5), (5, 4), (6, 4), (4, 6)  # Estos no cumplen con la forma de L
        ]
        for move in invalid_moves:
            to_row, to_col = move
            self.assertFalse(self.knight.valid_positions(4, 4, to_row, to_col))  # Verifica que cada movimiento sea inválido

if __name__ == '__main__':
    unittest.main()  # Ejecuta las pruebas al correr este archivo
