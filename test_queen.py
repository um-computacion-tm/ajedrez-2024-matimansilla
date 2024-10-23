import unittest
from queen import Queen
from board import Board
from unittest.mock import MagicMock

class TestQueenValidPositions(unittest.TestCase):

    def test_queen_symbol_white(self):
        board = Board()
        queen = Queen("WHITE", board)
        self.assertEqual(queen.symbol(), '♕')

    def test_queen_symbol_black(self):
        board = Board()
        queen = Queen("BLACK", board)
        self.assertEqual(queen.symbol(), '♛')

    def setUp(self):
        self.board = MagicMock()
        self.white_queen = Queen("WHITE", self.board)

    def test_valid_move(self):
        test_cases = [
            {'from_row': 3, 'from_col': 3, 'to_row': 5, 'to_col': 3, 'expected': True},   # Vertical
            {'from_row': 3, 'from_col': 3, 'to_row': 3, 'to_col': 5, 'expected': True},   # Horizontal
            {'from_row': 3, 'from_col': 3, 'to_row': 5, 'to_col': 5, 'expected': True},   # Diagonal
            {'from_row': 3, 'from_col': 3, 'to_row': 5, 'to_col': 4, 'expected': False},  # Movimiento no válido
        ]

        for case in test_cases:
            move = {
                'from_row': case['from_row'],
                'from_col': case['from_col'],
                'to_row': case['to_row'],
                'to_col': case['to_col']
            }
            self.white_queen.get_possible_moves = MagicMock(return_value=self.get_mocked_moves(move, case['expected']))
            is_valid = self.white_queen.valid_positions(move['from_row'], move['from_col'], move['to_row'], move['to_col'])
            self.assertEqual(is_valid, case['expected'])

    def get_mocked_moves(self, move, expected):
        if expected:  # Para movimientos válidos
            if move['from_row'] == move['to_row']:  # Horizontal
                start_col = min(move['from_col'], move['to_col'])
                end_col = max(move['from_col'], move['to_col'])
                return [(move['to_row'], col) for col in range(start_col, end_col + 1)]
            elif move['from_col'] == move['to_col']:  # Vertical
                start_row = min(move['from_row'], move['to_row'])
                end_row = max(move['from_row'], move['to_row'])
                return [(row, move['to_col']) for row in range(start_row, end_row + 1)]
            else:  # Diagonal
                return [(move['from_row'] + i, move['from_col'] + i) for i in range(-1, 3)
                        if 0 <= move['from_row'] + i < 8 and 0 <= move['from_col'] + i < 8]
        return [(5, 5), (4, 4)]  # Retorna movimientos no válidos por defecto

    def mock_possible_positions(self, orthogonal_positions, diagonal_positions):
        self.white_queen.possible_orthogonal_positions = MagicMock(return_value=orthogonal_positions)
        self.white_queen.possible_diagonal_positions = MagicMock(return_value=diagonal_positions)

    def test_get_possible_moves_calls_find_valid_moves(self):
        from_row, from_col = 3, 3
        directions = [(1, 0), (0, 1), (1, 1), (-1, 0)]
        self.white_queen.find_valid_moves = MagicMock(return_value=[(5, 3), (3, 5), (5, 5)])
        possible_moves = self.white_queen.get_possible_moves(from_row, from_col, directions)
        self.white_queen.find_valid_moves.assert_called_once_with(from_row, from_col, directions, single_step=False)
        self.assertEqual(possible_moves, [(5, 3), (3, 5), (5, 5)])

    def test_get_possible_positions(self):
        from_row, from_col = 3, 3
        
        # Utiliza el nuevo método para establecer los mocks
        self.mock_possible_positions(
            orthogonal_positions=[(3, 4), (3, 5), (4, 3), (5, 3)],
            diagonal_positions=[(4, 4), (5, 5), (2, 2), (1, 1)]
        )
        
        expected_positions = [
            (3, 4), (3, 5), (4, 3), (5, 3),  # Movimientos ortogonales
            (4, 4), (5, 5), (2, 2), (1, 1)   # Movimientos diagonales
        ]
        
        possible_positions = self.white_queen.get_possible_positions(from_row, from_col)
        
        self.assertEqual(possible_positions, expected_positions)

if __name__ == "__main__":
    unittest.main()
