import unittest
from bishop import Bishop
from board import Board

class TestBishop(unittest.TestCase):

    # Simbolos piezas alfiles (blanco y negro)

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
        self.board = Board()  # Inicializa un nuevo tablero antes de cada prueba
        self.bishop = Bishop("WHITE", self.board)  # Crea un alfil blanco
        self.board.set_piece(4, 4, self.bishop)  # Coloca el alfil en el centro

    def test_valid_position_diagonal(self):
        from_row, from_col = 4, 4
        to_row, to_col = 6, 6  # Movimiento válido en diagonal
        self.assertTrue(self.bishop.valid_positions(from_row, from_col, to_row, to_col))  # Verifica que el movimiento sea válido

    def test_invalid_position_non_diagonal(self):
        from_row, from_col = 4, 4
        to_row, to_col = 4, 5  # Movimiento no válido (no es diagonal)
        self.assertFalse(self.bishop.valid_positions(from_row, from_col, to_row, to_col))  # Verifica que el movimiento no sea válido

if __name__ == '__main__':
    unittest.main()  # Ejecuta las pruebas al ejecutar el script
