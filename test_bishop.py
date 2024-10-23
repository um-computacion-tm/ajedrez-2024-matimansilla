import unittest
from bishop import Bishop
from board import Board

class TestBishop(unittest.TestCase):

    # Símbolos de las piezas (alfiles blanco y negro)
    def test_bishop_symbol_white(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        self.assertEqual(bishop.symbol(), '♗')

    def test_bishop_symbol_black(self):
        board = Board()
        bishop = Bishop("BLACK", board)
        self.assertEqual(bishop.symbol(), '♝')

    # TESTEO MOVIMIENTOS
    def setUp(self):
        """Crea un tablero nuevo y coloca el alfil en una posición avanzada para las pruebas."""
        self.board = Board()  # Inicializamos un nuevo tablero de ajedrez
        self.bishop = Bishop("WHITE", self.board)  # Creamos un alfil blanco
        self.board.set_piece(3, 5, self.bishop)  # Posicionamos el alfil en la cuarta fila, sexta columna

    def test_valid_position_diagonal(self):
        from_row, from_col = 3, 5
        to_row, to_col = 5, 7  # Movimiento válido en diagonal
        self.assertTrue(self.bishop.valid_positions(from_row, from_col, to_row, to_col))  # Verifica que el movimiento sea válido

    def test_invalid_position_non_diagonal(self):
        from_row, from_col = 3, 5
        to_row, to_col = 3, 6  # Movimiento no válido (no es diagonal)
        self.assertFalse(self.bishop.valid_positions(from_row, from_col, to_row, to_col))  # Verifica que el movimiento no sea válido

if __name__ == '__main__':
    unittest.main()  # Ejecuta las pruebas al ejecutar el script
