import unittest
from bishop import Bishop
from board import Board
from pawn import Pawn

class TestBishop(unittest.TestCase):
    """Clase de pruebas para el comportamiento de la pieza Alfil en el juego de ajedrez."""

    # Pruebas para verificar los símbolos de las piezas Alfil (blanco y negro)
    def test_bishop_symbol_white(self):
        board = Board()  # Crea un nuevo tablero de ajedrez
        bishop = Bishop("WHITE", board)  # Crea un alfil blanco
        self.assertEqual(bishop.symbol(), '♗')  # Verifica que el símbolo del alfil blanco sea correcto

    def test_bishop_symbol_black(self):
        board = Board()  # Crea un nuevo tablero de ajedrez
        bishop = Bishop("BLACK", board)  # Crea un alfil negro
        self.assertEqual(bishop.symbol(), '♝')  # Verifica que el símbolo del alfil negro sea correcto

    # Métodos de configuración para las pruebas de movimiento
    def setUp(self):
        self.board = Board()  # Inicializa un nuevo tablero antes de cada prueba
        self.bishop = Bishop("WHITE", self.board)  # Crea un alfil blanco
        self.board.set_piece(4, 4, self.bishop)  # Coloca el alfil en la posición central del tablero

    # Prueba para validar un movimiento diagonal permitido
    def test_valid_position_diagonal(self):
        from_row, from_col = 4, 4  # Posición de origen
        to_row, to_col = 6, 6  # Posición de destino válida (diagonal)
        self.assertTrue(self.bishop.valid_positions(from_row, from_col, to_row, to_col))  # Verifica que el movimiento sea válido

    # Prueba para verificar un movimiento no diagonal
    def test_invalid_position_non_diagonal(self):
        from_row, from_col = 4, 4  # Posición de origen
        to_row, to_col = 4, 5  # Posición de destino no válida (no es diagonal)
        self.assertFalse(self.bishop.valid_positions(from_row, from_col, to_row, to_col))  # Verifica que el movimiento no sea válido

if __name__ == '__main__':
    unittest.main()  # Ejecuta las pruebas al ejecutar el script
