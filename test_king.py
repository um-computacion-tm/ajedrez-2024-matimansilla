
import unittest
from king import King
from board import Board
from chess import Chess

class TestKing(unittest.TestCase):

    def test_king_symbol_white(self):
        board = Board()
        king = King("WHITE", board)
        self.assertEqual(king.symbol(), '♔')

    def test_king_symbol_black(self):
        board = Board()
        king = King("BLACK", board)
        self.assertEqual(king.symbol(), '♚')

# TESTEO MOVIMIENTOS


    # Testeo de movimientos válidos
    def test_move_up(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (3, 4)  # Una casilla hacia arriba
        self.assertTrue(king.valid_positions(from_pos[0], from_pos[1], to_pos[0], to_pos[1]))

    def test_move_down(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (5, 4)  # Una casilla hacia abajo
        self.assertTrue(king.valid_positions(from_pos[0], from_pos[1], to_pos[0], to_pos[1]))

    def test_move_right(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (4, 5)  # Una casilla hacia la derecha
        self.assertTrue(king.valid_positions(from_pos[0], from_pos[1], to_pos[0], to_pos[1]))

    def test_move_left(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (4, 3)  # Una casilla hacia la izquierda
        self.assertTrue(king.valid_positions(from_pos[0], from_pos[1], to_pos[0], to_pos[1]))

    def test_move_up_right(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (3, 5)  # Diagonal hacia arriba a la derecha
        self.assertTrue(king.valid_positions(from_pos[0], from_pos[1], to_pos[0], to_pos[1]))

    def test_move_down_left(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (5, 3)  # Diagonal hacia abajo a la izquierda
        self.assertTrue(king.valid_positions(from_pos[0], from_pos[1], to_pos[0], to_pos[1]))

    # Testeo de movimientos inválidos
    def test_invalid_move_up(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (2, 4)  # Dos casillas hacia arriba
        self.assertFalse(king.valid_positions(from_pos[0], from_pos[1], to_pos[0], to_pos[1]))

    def test_invalid_diagonal_move(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (2, 2)  # Dos casillas en diagonal
        self.assertFalse(king.valid_positions(from_pos[0], from_pos[1], to_pos[0], to_pos[1]))

    def test_invalid_horizontal_jump(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (4, 6)  # Dos casillas hacia la derecha
        self.assertFalse(king.valid_positions(from_pos[0], from_pos[1], to_pos[0], to_pos[1]))



if __name__ == '__main__':
    unittest.main()