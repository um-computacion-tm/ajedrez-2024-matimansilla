import unittest
from queen import Queen
from board import Board
from unittest.mock import MagicMock

class TestQueenValidPositions(unittest.TestCase):

# Simbolos piezas reinas (blanco y negro)

    def test_queen_symbol_white(self):
        board = Board()
        queen = Queen("WHITE", board)
        self.assertEqual(queen.symbol(), '♕')

    def test_queen_symbol_black(self):
        board = Board()
        queen = Queen("BLACK", board)
        self.assertEqual(queen.symbol(), '♛')

# TESTEO MOVIMIENTOS

    def setUp(self):
        self.board = MagicMock()  # Simulamos el tablero
        self.white_queen = Queen("WHITE", self.board)  # Instancia de la reina blanca

    # Testea un movimiento válido en dirección vertical
    def test_valid_move_vertical(self):
        move = {'from_row': 3, 'from_col': 3, 'to_row': 5, 'to_col': 3}
        self.white_queen.get_possible_moves = MagicMock(return_value=[(5, 3), (4, 3)])
        is_valid = self.white_queen.valid_positions(move['from_row'], move['from_col'], move['to_row'], move['to_col'])
        self.assertTrue(is_valid)  # Debe ser verdadero

    # Testea un movimiento válido en dirección horizontal
    def test_valid_move_horizontal(self):
        move = {'from_row': 3, 'from_col': 3, 'to_row': 3, 'to_col': 5}
        self.white_queen.get_possible_moves = MagicMock(return_value=[(3, 5), (3, 4)])
        is_valid = self.white_queen.valid_positions(move['from_row'], move['from_col'], move['to_row'], move['to_col'])
        self.assertTrue(is_valid)  # Debe ser verdadero

    # Testea un movimiento válido en dirección diagonal
    def test_valid_move_diagonal(self):
        move = {'from_row': 3, 'from_col': 3, 'to_row': 5, 'to_col': 5}
        self.white_queen.get_possible_moves = MagicMock(return_value=[(5, 5), (4, 4)])
        is_valid = self.white_queen.valid_positions(move['from_row'], move['from_col'], move['to_row'], move['to_col'])
        self.assertTrue(is_valid)  # Debe ser verdadero

    # Testea un movimiento inválido que no es ni ortogonal ni diagonal
    def test_invalid_move(self):
        move = {'from_row': 3, 'from_col': 3, 'to_row': 5, 'to_col': 4}
        self.white_queen.get_possible_moves = MagicMock(return_value=[(5, 5), (4, 4)])
        is_valid = self.white_queen.valid_positions(move['from_row'], move['from_col'], move['to_row'], move['to_col'])
        self.assertFalse(is_valid)  # Debe ser falso

    def test_get_possible_moves_calls_find_valid_moves(self):
        from_row, from_col = 3, 3
        directions = [(1, 0), (0, 1), (1, 1), (-1, 0)]  # Ejemplo de direcciones ortogonales y diagonales

        # Mock de find_valid_moves para rastrear si es llamado correctamente
        self.white_queen.find_valid_moves = MagicMock(return_value=[(5, 3), (3, 5), (5, 5)])

        # Llamamos a get_possible_moves
        possible_moves = self.white_queen.get_possible_moves(from_row, from_col, directions)

        # Verificamos si find_valid_moves fue llamado con los parámetros correctos
        self.white_queen.find_valid_moves.assert_called_once_with(from_row, from_col, directions, single_step=False)

        # Verificamos que el resultado sea correcto
        self.assertEqual(possible_moves, [(5, 3), (3, 5), (5, 5)])


if __name__ == "__main__":
    unittest.main()