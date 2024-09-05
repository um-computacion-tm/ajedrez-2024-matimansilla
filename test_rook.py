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
        # Limpia las posiciones hacia abajo desde (4,1)
        board.__positions__[5][1] = None
        board.__positions__[6][1] = None
        board.__positions__[7][1] = None
        rook = Rook('WHITE', board)  
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1), (6, 1), (7, 1)])

    def test_move_vertical_asc(self):
        board = Board()
        # Limpia las posiciones hacia arriba desde (4,1)
        for row in range(4):
            board.__positions__[row][1] = None
        rook = Rook('WHITE', board)  
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(possibles, [(3, 1), (2, 1), (1, 1), (0, 1)])

    def test_move_vertical_desc_with_own_pieces(self):
        board = Board()
        board.__positions__[5][1] = None
        board.__positions__[6][1] = Pawn("BLACK", board)
        rook = Rook("BLACK", board)  
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1)])

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)  
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(possibles, [(5, 1), (6, 1)])

if __name__ == '__main__':
    unittest.main()

