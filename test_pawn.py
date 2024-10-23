
import unittest
from pawn import Pawn
from board import Board

class TestPawn(unittest.TestCase):

# Simbolos piezas peones (blanco y negro)

    def test_pawn_symbol_white(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        self.assertEqual(pawn.symbol(), '♙')

    def test_pawn_symbol_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        self.assertEqual(pawn.symbol(), '♟')

# TESTEO MOVIMIENTOS

    def setUp(self):
        self.board = Board()
        self.pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, self.pawn)  # Coloca el peón en su posición inicial

    def test_valid_single_move(self):
        # Verifica que el movimiento hacia adelante sea válido
        self.assertTrue(self.pawn.valid_positions(6, 4, 5, 4))

    def test_valid_double_move(self):
        # Verifica que el movimiento doble hacia adelante sea válido
        self.assertTrue(self.pawn.valid_positions(6, 4, 4, 4))

    def test_valid_capture_move(self):
        # Verifica que la captura diagonal sea válida
        opponent_pawn = Pawn("BLACK", self.board)
        self.board.set_piece(5, 5, opponent_pawn)  # Coloca un oponente para capturar
        self.assertTrue(self.pawn.valid_positions(6, 4, 5, 5))  # Captura diagonal derecha

    def test_invalid_move_backwards(self):
        # Verifica que mover hacia atrás no sea válido
        self.assertFalse(self.pawn.valid_positions(6, 4, 7, 4))  # Movimiento hacia atrás

    def test_invalid_move_to_empty_square(self):
        # Verifica que mover a una casilla vacía no válida no sea permitido
        self.assertFalse(self.pawn.valid_positions(6, 4, 6, 5))  # Movimiento no permitido (horizontales)

    def test_invalid_capture_on_empty_square(self):
        # Verifica que la captura en una casilla vacía no sea válida
        self.assertTrue(self.pawn.valid_positions(6, 4, 5, 4))  # Captura no válida (sin pieza)


if __name__ == '__main__':
    unittest.main()