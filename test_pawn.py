import unittest
from pawn import Pawn
from board import Board

class TestPawn(unittest.TestCase):

    # Símbolos de las piezas (peones blanco y negro)
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
        """Establece un tablero vacío y coloca el peón en la fila inicial correspondiente."""
        self.board = Board()  # Creamos un nuevo tablero de juego
        self.pawn = Pawn("WHITE", self.board)  # Instanciamos un peón blanco
        self.board.set_piece(1, 3, self.pawn)  # Colocamos el peón en la segunda fila, columna 4

    def test_valid_single_move(self):
        # Verifica que el movimiento hacia adelante sea válido
        self.assertTrue(self.pawn.valid_positions(1, 3, 2, 3))

    def test_valid_double_move(self):
        # Verifica que el movimiento doble hacia adelante sea válido
        self.assertTrue(self.pawn.valid_positions(1, 3, 3, 3))

    def test_valid_capture_move(self):
        # Verifica que la captura diagonal sea válida
        opponent_pawn = Pawn("BLACK", self.board)
        self.board.set_piece(2, 4, opponent_pawn)  # Coloca un oponente para capturar
        self.assertTrue(self.pawn.valid_positions(1, 3, 2, 4))  # Captura diagonal derecha

    def test_invalid_move_backwards(self):
        # Verifica que mover hacia atrás no sea válido
        self.assertFalse(self.pawn.valid_positions(1, 3, 0, 3))  # Movimiento hacia atrás

    def test_invalid_move_to_empty_square(self):
        # Verifica que mover a una casilla vacía no válida no sea permitido
        self.assertFalse(self.pawn.valid_positions(1, 3, 1, 4))  # Movimiento no permitido (horizontales)

    def test_invalid_capture_on_empty_square(self):
        # Verifica que la captura en una casilla vacía no sea válida
        self.assertFalse(self.pawn.valid_positions(1, 3, 2, 3))  # Captura no válida (sin pieza)

if __name__ == '__main__':
    unittest.main()
