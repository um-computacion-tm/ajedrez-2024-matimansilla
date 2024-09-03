import unittest
from rook import Rook
from board import Board

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_move_vertical_asc(self):
        # Crear una torre blanca
        rook = Rook("WHITE", self.board)
        # Colocar la torre en una posición inicial
        self.board.place_piece(rook, 4, 1)
        # Obtener las posiciones posibles hacia arriba
        possibles = rook.possible_positions_va(4, 1)
        # La torre puede moverse a todas las posiciones vacías hacia arriba
        self.assertEqual(possibles, [(3, 1), (2, 1), (1, 1), (0, 1)])

    def test_move_vertical_desc(self):
        # Crear una torre blanca
        rook = Rook("WHITE", self.board)
        # Colocar la torre en una posición inicial
        self.board.place_piece(rook, 4, 1)
        # Obtener las posiciones posibles hacia abajo
        possibles = rook.possible_positions_vd(4, 1)
        # La torre puede moverse a todas las posiciones vacías hacia abajo
        self.assertEqual(possibles, [(5, 1), (6, 1), (7, 1)])

    def test_move_vertical_desc_with_not_own_piece(self):
        # Crear una torre blanca
        rook = Rook("WHITE", self.board)
        # Crear una pieza negra y colocarla en la posición (5, 1)
        other_piece = Rook("BLACK", self.board)
        self.board.place_piece(other_piece, 5, 1)
        # Colocar la torre en una posición inicial
        self.board.place_piece(rook, 4, 1)
        # Obtener las posiciones posibles hacia abajo
        possibles = rook.possible_positions_vd(4, 1)
        # La torre puede moverse hasta la pieza negra en (5, 1), pero no más allá
        self.assertEqual(possibles, [(5, 1)])

    def test_move_vertical_desc_with_own_piece(self):
        # Crear una torre blanca
        rook = Rook("WHITE", self.board)
        # Crear otra pieza blanca y colocarla en la posición (5, 1)
        other_piece = Rook("WHITE", self.board)
        self.board.place_piece(other_piece, 5, 1)
        # Colocar la torre en una posición inicial
        self.board.place_piece(rook, 4, 1)
        # Obtener las posiciones posibles hacia abajo
        possibles = rook.possible_positions_vd(4, 1)
        # La torre puede moverse hasta la pieza blanca en (5, 1), pero no más allá
        self.assertEqual(possibles, [(5, 1)])

    def test_str(self):
        # Crear una torre blanca
        rook = Rook("WHITE", self.board)
        self.assertEqual(str(rook), "♖")

if __name__ == "__main__":
    unittest.main()
