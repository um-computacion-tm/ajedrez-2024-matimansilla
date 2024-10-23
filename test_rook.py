import unittest
from board import Board
from rook import Rook

class TestRookMovements(unittest.TestCase):
    def setUp(self):
        # Inicializa el tablero y las torres sin el tercer argumento innecesario
        self.board = Board(for_test=True)  
        self.white_rook = Rook("White", self.board)  # Solo se pasan dos argumentos
        self.black_rook = Rook("Black", self.board)  # Solo se pasan dos argumentos
        
    def test_white_str(self):
        # Verifica el símbolo de la torre blanca
        self.assertEqual(self.white_rook.symbol(), "♖")

    def test_black_str(self):
        # Verifica el símbolo de la torre negra
        self.assertEqual(self.black_rook.symbol(), "♜")

    def test_possible_positions_white_rook(self):
        # Coloca la torre blanca en el tablero y verifica sus posiciones posibles
        self.board.place_piece(4, 4, self.white_rook)
        possibles = self.white_rook.possible_positions(4, 4, [(-1, 0), (1, 0), (0, -1), (0, 1)], True)
        expected = [
            (3, 4), (2, 4), (1, 4), (0, 4),
            (5, 4), (6, 4), (7, 4),
            (4, 3), (4, 2), (4, 1), (4, 0),
            (4, 5), (4, 6), (4, 7)
        ]
        self.assertEqual(possibles, expected)

    def test_white_rook_board_edge(self):
        # Coloca la torre blanca en el borde del tablero y verifica sus posiciones posibles
        self.board.place_piece(0, 0, self.white_rook)
        possibles = self.white_rook.possible_positions(0, 0, [(-1, 0), (1, 0), (0, -1), (0, 1)], True)
        expected = [
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)
        ]
        self.assertEqual(possibles, expected)

    def test_possible_positions_black_rook(self):
        # Coloca la torre negra en el tablero y verifica sus posiciones posibles
        self.board.place_piece(4, 4, self.black_rook)
        possibles = self.black_rook.possible_positions(4, 4, [(-1, 0), (1, 0), (0, -1), (0, 1)], True)
        expected = [
            (3, 4), (2, 4), (1, 4), (0, 4),
            (5, 4), (6, 4), (7, 4),
            (4, 3), (4, 2), (4, 1), (4, 0),
            (4, 5), (4, 6), (4, 7)
        ]
        self.assertEqual(possibles, expected)

    def test_black_rook_board_edge(self):
        # Coloca la torre negra en el borde del tablero y verifica sus posiciones posibles
        self.board.place_piece(0, 0, self.black_rook)
        possibles = self.black_rook.possible_positions(0, 0, [(-1, 0), (1, 0), (0, -1), (0, 1)], True)
        expected = [
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)
        ]
        self.assertEqual(possibles, expected)

if __name__ == '__main__':
    unittest.main()
