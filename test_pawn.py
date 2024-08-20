import unittest
from pieces import Pawn

class TestPawn(unittest.TestCase):
    def setUp(self):
        self.white_pawn = Pawn('WHITE', 'pawn1_white')
        self.black_pawn = Pawn('BLACK', 'pawn1_black')

    def test_initial_attributes(self):
        # Verifica los atributos iniciales del peón
        self.assertEqual(self.white_pawn.__color__, 'WHITE')
        self.assertEqual(self.white_pawn.__name__, 'pawn1_white')
        self.assertEqual(self.black_pawn.__color__, 'BLACK')
        self.assertEqual(self.black_pawn.__name__, 'pawn1_black')

    def test_pawn_possible_moves(self):
        # Verifica los movimientos posibles del peón desde una posición inicial
        # Este es un ejemplo; ajusta según tu implementación de get_possible_moves
        moves = self.white_pawn.get_possible_moves()
        self.assertIn((1, 0), moves)  # Movimiento de un espacio hacia adelante
        self.assertIn((2, 0), moves)  # Movimiento de dos espacios hacia adelante

if __name__ == '__main__':
    unittest.main()
