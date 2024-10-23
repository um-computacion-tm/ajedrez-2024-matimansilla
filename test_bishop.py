import unittest
from bishop import Bishop
from board import Board

class TestBishop(unittest.TestCase):

    # Símbolos de las piezas (alfiles blanco y negro)
    def test_bishop_white_symbol(self):
        board_instance = Board()
        white_bishop = Bishop("WHITE", board_instance)
        self.assertEqual(white_bishop.symbol(), '♗', "El símbolo del alfil blanco debería ser '♗'.")

    def test_bishop_black_symbol(self):
        board_instance = Board()
        black_bishop = Bishop("BLACK", board_instance)
        self.assertEqual(black_bishop.symbol(), '♝', "El símbolo del alfil negro debería ser '♝'.")

    # TESTEO MOVIMIENTOS
    def setUp(self):
        """Inicializa un nuevo tablero y coloca el alfil en una posición específica para las pruebas."""
        self.board = Board()  # Creamos un nuevo tablero
        self.bishop = Bishop("WHITE", self.board)  # Instanciamos un alfil blanco
        self.board.set_piece(3, 5, self.bishop)  # Colocamos el alfil en la posición (3, 5)

    def check_bishop_can_move_diagonally(self):
        start_row = 3
        start_col = 5
        end_row = 5
        end_col = 7  # Movimiento diagonal permitido
        move_result = self.bishop.valid_positions(start_row, start_col, end_row, end_col)
        self.assertIs(move_result, True, "Se esperaba que el movimiento diagonal fuera válido.")

    def confirm_bishop_cannot_move_laterally(self):
        start_row = 3
        start_col = 5
        end_row = 3
        end_col = 6  # Movimiento lateral no permitido
        is_valid_move = self.bishop.valid_positions(start_row, start_col, end_row, end_col)
        self.assertIs(is_valid_move, False, "Se esperaba que el movimiento lateral no fuera permitido.")

if __name__ == '__main__':
    unittest.main()  # Ejecuta las pruebas al ejecutar el script
