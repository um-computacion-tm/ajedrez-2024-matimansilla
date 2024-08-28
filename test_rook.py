import unittest
from pieces import Rook,Pawn
from board import Board

class TestRook(unittest.TestCase):
    def test_str(self):
        board=Board()
        rook=Rook('WHITE',board)
        self.assertEqual(str(rook),'♜')

    def test_move_vertical_desc(self):
        board=Board()
        rook=Rook('WHITE',board)
        possibles=rook.possible_positions_vd(4,1)
        self.assertEqual(possibles,[(5,1),(6,1),(7,1)])

    def test_move_vertical_asc(self):
        board=Board()
        rook=Rook('WHITE',board)
        possibles=rook.possible_positions_va(4,1)
        self.assertEqual(possibles,[(3,1),(2,1),(1,1),(0,1)])
    
    def test_move_vertical_desc_with_own_pieces(self):
        board=Board()
        board.__positions__[6,1]=Pawn('WHITE',board)
        rook=Rook('WHITE',board)
        possibles=rook.possible_positions_vd(4,1)
        self.assertEqual(possibles,[(3,1),(2,1),(1,1),(0,1)])

if __name__=='__main__':
    unittest.main()