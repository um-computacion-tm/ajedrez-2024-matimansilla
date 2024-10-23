import unittest
from rook import Rook
from board import Board

class TestRook(unittest.TestCase):

    # Símbolos de las piezas (torres blanco y negro)
    def test_rook_symbol_white(self):
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(rook.symbol(), '♖')

    def test_rook_symbol_black(self):
        board = Board()
        rook = Rook("BLACK", board)
        self.assertEqual(rook.symbol(), '♜') 

    # Inicializa el tablero
    def setUp(self):
        """Inicializa el tablero y coloca la torre en una fila lateral para verificar movimientos verticales."""
        self.board = Board()  # Creamos una instancia del tablero
        self.rook = Rook("WHITE", self.board)  # Instanciamos una torre blanca
        self.board.set_piece(7, 0, self.rook)  # Colocamos la torre en la esquina superior izquierda

    # TESTEO MOVIMIENTOS

    # Testea un movimiento válido hacia arriba
    def test_valid_move_up(self):
        is_possible = self.rook.valid_positions(7, 0, 6, 0)
        self.assertTrue(is_possible)

    # Testea un movimiento válido hacia abajo
    def test_valid_move_down(self):
        is_possible = self.rook.valid_positions(7, 0, 8, 0)
        self.assertFalse(is_possible)  # No debería ser posible moverse hacia abajo fuera del tablero

    # Testea un movimiento válido hacia la izquierda
    def test_valid_move_left(self):
        is_possible = self.rook.valid_positions(7, 0, 7, -1)
        self.assertFalse(is_possible)  # No debería ser posible moverse hacia la izquierda fuera del tablero

    # Testea un movimiento válido hacia la derecha
    def test_valid_move_right(self):
        is_possible = self.rook.valid_positions(7, 0, 7, 1)
        self.assertTrue(is_possible)

    # Testea un movimiento inválido en diagonal
    def test_invalid_move_diagonal(self):
        is_possible = self.rook.valid_positions(7, 0, 6, 1)
        self.assertFalse(is_possible)

    # Testea un movimiento válido de dos casillas hacia arriba (parte del movimiento ortogonal)
    def test_valid_move_two_steps_up(self):
        is_possible = self.rook.valid_positions(7, 0, 5, 0)
        self.assertTrue(is_possible)

if __name__ == '__main__':
    unittest.main()
