import unittest
from pieces import Pawn, Rook
from board import Board

class TestRook(unittest.TestCase):
    def test_str(self):
        board = Board()
        rook = Rook('WHITE', board)
        self.assertEqual(str(rook), '♖')  # Blanco debería ser ♖, negro ♜

    def test_move_vertical_desc(self):
        board = Board()
        board.__positions__[5][1] = None
        board.__positions__[6][1] = None
        board.__positions__[7][1] = None
        rook = Rook('WHITE', board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1), (6, 1), (7, 1)])

    def test_move_vertical_asc(self):
        board = Board()
        for row in range(4):
            board.__positions__[row][1] = None
        rook = Rook('WHITE', board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(possibles, [(3, 1), (2, 1), (1, 1), (0, 1)])

    def test_move_horizontal_right(self):
        board = Board()
        # Limpia las posiciones a la derecha desde (4,1)
        for col in range(2, 8):
            board.__positions__[4][col] = None
        rook = Rook('WHITE', board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_hr(4, 1)
        self.assertEqual(possibles, [(4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)])

    def test_move_horizontal_left(self):
        board = Board()
        # Limpia las posiciones a la izquierda desde (4,5)
        for col in range(5):
            board.__positions__[4][col] = None
        rook = Rook('WHITE', board)
        board.set_piece(4, 5, rook)
        possibles = rook.possible_positions_hl(4, 5)
        self.assertEqual(possibles, [(4, 4), (4, 3), (4, 2), (4, 1), (4, 0)])

    def test_move_with_enemy_piece(self):
        board = Board()
        # Coloca una pieza enemiga en (6,1)
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook('WHITE', board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1), (6, 1)])  # Puede capturar en (6,1)

    def test_valid_positions(self):
        board = Board()
        # Limpia todas las posiciones a lo largo de filas y columnas
        for i in range(8):
            for j in range(8):
                board.__positions__[i][j] = None
        rook = Rook('WHITE', board)
        board.set_piece(4, 4, rook)
        valid = rook.valid_positions(4, 4, 7, 4)
        self.assertTrue(valid)  # Debería poder moverse a (7, 4)

if __name__ == '__main__':
    unittest.main()
