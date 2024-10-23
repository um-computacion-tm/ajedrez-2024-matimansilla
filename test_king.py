import unittest
from king import King
from board import Board
from chess import Chess

class TestKing(unittest.TestCase):

    def setUp(self):
        self.board = Board()  # Inicializa el tablero
        self.king = King("WHITE", self.board)  # Crea un rey

    def assert_invalid_move(self, from_pos, to_pos):
        """Verifica que un movimiento no válido retorne False."""
        self.assertFalse(self.king.valid_positions(from_pos[0], from_pos[1], to_pos[0], to_pos[1]))

    def assert_valid_move(self, from_pos, to_pos):
        """Verifica que un movimiento válido retorne True."""
        self.assertTrue(self.king.valid_positions(from_pos[0], from_pos[1], to_pos[0], to_pos[1]))

    def test_king_symbol_white(self):
        self.assertEqual(self.king.symbol(), '♔')

    def test_king_symbol_black(self):
        king_black = King("BLACK", self.board)
        self.assertEqual(king_black.symbol(), '♚')

    # TESTEO MOVIMIENTOS

    # Testeo de movimientos válidos
    def test_move_up(self):
        from_pos = (4, 4)
        to_pos = (3, 4)  # Una casilla hacia arriba
        self.assert_valid_move(from_pos, to_pos)

    def test_move_down(self):
        from_pos = (4, 4)
        to_pos = (5, 4)  # Una casilla hacia abajo
        self.assert_valid_move(from_pos, to_pos)

    def test_move_right(self):
        from_pos = (4, 4)
        to_pos = (4, 5)  # Una casilla hacia la derecha
        self.assert_valid_move(from_pos, to_pos)

    def test_move_left(self):
        from_pos = (4, 4)
        to_pos = (4, 3)  # Una casilla hacia la izquierda
        self.assert_valid_move(from_pos, to_pos)

    def test_move_up_right(self):
        from_pos = (4, 4)
        to_pos = (3, 5)  # Diagonal hacia arriba a la derecha
        self.assert_valid_move(from_pos, to_pos)

    def test_move_down_left(self):
        from_pos = (4, 4)
        to_pos = (5, 3)  # Diagonal hacia abajo a la izquierda
        self.assert_valid_move(from_pos, to_pos)

    # Testeo de movimientos inválidos
    def test_invalid_move_up(self):
        from_pos = (4, 4)
        to_pos = (2, 4)  # Dos casillas hacia arriba
        self.assert_invalid_move(from_pos, to_pos)

    def test_invalid_diagonal_move(self):
        from_pos = (4, 4)
        to_pos = (2, 2)  # Dos casillas en diagonal
        self.assert_invalid_move(from_pos, to_pos)

    def test_invalid_horizontal_jump(self):
        from_pos = (4, 4)
        to_pos = (4, 6)  # Dos casillas hacia la derecha
        self.assert_invalid_move(from_pos, to_pos)

    # Testeo de get_possible_moves
    def test_get_possible_moves(self):
        from_pos = (4, 4)
        directions = self.king._king_queen_directions_  # Obtener las direcciones del rey
        possible_moves = self.king.get_possible_moves(from_pos[0], from_pos[1], directions)
        expected_moves = [
            (3, 4), (5, 4), (4, 5), (4, 3), (3, 5), (5, 3)  # Movimientos válidos del rey
        ]
        # Comprobar que todos los movimientos esperados están en los movimientos posibles
        for move in expected_moves:
            self.assertIn(move, possible_moves)

if __name__ == '__main__':
    unittest.main()
