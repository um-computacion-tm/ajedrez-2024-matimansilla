import unittest
from pieces import Piece
from board import Board
from unittest.mock import MagicMock

class TestPieces(unittest.TestCase):
    
    def test_get_color(self):
        piece = Piece("BLACK", None)  # Asume que la pieza necesita un color y el tablero
        self.assertEqual(piece.get_color(), "BLACK")

    def setUp(self):
        self.board = MagicMock()  # Mockeamos el tablero
        self.piece = Piece("WHITE", self.board)  
        self.black_piece = Piece(color='BLACK', board=self.board)
        self.white_piece = Piece(color='WHITE', board=self.board)

    # Test para movimiento en una dirección vacía
    def test_empty_board_moves(self):
        self.board.get_piece.side_effect = lambda row, col: None  # Sin piezas en el tablero
        directions = [(0, 1)]  # Dirección hacia la derecha
        
        valid_moves = self.piece.find_valid_moves(3, 3, directions)

        expected_moves = [(3, 4), (3, 5), (3, 6), (3, 7)]  # Movimientos válidos hacia la derecha
        self.assertEqual(valid_moves, expected_moves)

    # Test para movimiento con una captura
    def test_capture_opponent_piece(self):
        mock_opponent_piece = MagicMock()
        mock_opponent_piece.get_color.return_value = "BLACK"
        
        # Nuevo bloque diferenciado para capturar pieza del oponente
        def pieza_oponente(x, y):
            return mock_opponent_piece if (x, y) == (3, 5) else None
        self.board.get_piece.side_effect = pieza_oponente  # Asigna función para simular pieza enemiga
        
        directions = [(0, 1)]  # Dirección hacia la derecha
        valid_moves = self.piece.find_valid_moves(3, 3, directions)

        expected_moves = [(3, 4), (3, 5)]  # Puede moverse y capturar
        self.assertEqual(valid_moves, expected_moves)

    # Test para movimiento restringido a un solo paso
    def test_single_step_move(self):
        self.board.get_piece.side_effect = lambda row, col: None  # Sin piezas en el tablero
        directions = [(0, 1)]  # Dirección hacia la derecha
        
        valid_moves = self.piece.find_valid_moves(3, 3, directions, single_step=True)

        expected_move = [(3, 4)]  # Solo puede moverse un paso a la derecha
        self.assertEqual(valid_moves, expected_move)

    # Test para verificar que se detiene cuando encuentra una pieza amiga
    def test_blocked_by_own_piece(self):
        mock_own_piece = MagicMock()
        mock_own_piece.get_color.return_value = "WHITE"
        
        # Segundo bloque diferenciado para la pieza propia
        self.board.get_piece.side_effect = lambda fila, columna: (
            mock_own_piece if all([fila == 3, columna == 4]) else None
        )  # Asigna pieza propia en la posición (3, 4)

        directions = [(0, 1)]  # Dirección hacia la derecha
        valid_moves = self.piece.find_valid_moves(3, 3, directions)

        expected_moves = []  # No hay movimientos válidos
        self.assertEqual(valid_moves, expected_moves)

    def test_get_directions(self):
        # Verifica que get_directions retorne una lista vacía
        self.assertEqual(self.piece.get_directions(), [], "El método get_directions debe retornar una lista vacía en la clase Piece.")

    def test_is_own_piece(self):
        # Verifica que is_own_piece retorne True para la misma pieza
        self.assertTrue(self.white_piece.is_own_piece(self.white_piece), "Debería retornar True para la misma pieza.")
        
        # Verifica que is_own_piece retorne False para una pieza diferente
        self.assertFalse(self.white_piece.is_own_piece(self.black_piece), "Debería retornar False para una pieza de color diferente.")
        
        # Verifica que is_own_piece retorne False si no hay pieza
        self.assertFalse(self.white_piece.is_own_piece(None), "Debería retornar False si no hay pieza.")

if __name__ == '__main__':
    unittest.main()
