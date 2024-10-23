import unittest
from king import King
from board import Board
from chess import Chess

class TestKing(unittest.TestCase):

    def setUp(self):
        self.board = Board()  # Inicializa el tablero
        self.king = King("WHITE", self.board)  # Crea un rey

    def check_invalid_move(self, start_pos, end_pos):
        """Confirma que un movimiento no válido produzca un resultado falso."""
        result = self.king.valid_positions(start_pos[0], start_pos[1], end_pos[0], end_pos[1])
        self.assertFalse(result)

    def check_valid_move(self, start_pos, end_pos):
        """Confirma que un movimiento válido produzca un resultado verdadero."""
        result = self.king.valid_positions(start_pos[0], start_pos[1], end_pos[0], end_pos[1])
        self.assertTrue(result)

    def test_king_symbol_white(self):
        self.assertEqual(self.king.symbol(), '♔')

    def test_king_symbol_black(self):
        king_black = King("BLACK", self.board)
        self.assertEqual(king_black.symbol(), '♚')

    # TESTEO MOVIMIENTOS

    # Testeo de movimientos válidos
    def test_movement_up(self):
        start = (4, 4)
        end = (3, 4)  # Avanza una posición hacia arriba
        self.check_valid_move(start, end)

    def test_downward_movement(self):
        initial_position = (4, 4)
        target_position = (5, 4)  # Se mueve hacia abajo
        self.check_valid_move(initial_position, target_position)

    def test_shift_right(self):
        origin = (4, 4)
        destination = (4, 5)  # Movimiento hacia la derecha
        self.check_valid_move(origin, destination)

    def test_slide_left(self):
        position_start = (4, 4)
        position_end = (4, 3)  # Movimiento hacia la izquierda
        self.check_valid_move(position_start, position_end)

    def test_diag_up_right(self):
        coord_initial = (4, 4)
        coord_final = (3, 5)  # Movimiento en diagonal superior derecha
        self.check_valid_move(coord_initial, coord_final)

    def test_diag_down_left(self):
        pos_from = (4, 4)
        pos_to = (5, 3)  # Diagonal hacia la izquierda y abajo
        self.check_valid_move(pos_from, pos_to)

    # Testeo de movimientos inválidos
    def test_invalid_vertical_movement(self):
        start_pos = (4, 4)
        move_to = (2, 4)  # Salta dos posiciones hacia arriba
        self.check_invalid_move(start_pos, move_to)

    def test_wrong_diag_move(self):
        begin = (4, 4)
        finish = (2, 2)  # Mueve dos posiciones en diagonal, movimiento ilegal
        self.check_invalid_move(begin, finish)

    def test_illegal_horizontal_jump(self):
        start_coord = (4, 4)
        end_coord = (4, 6)  # Salta dos casillas hacia la derecha, lo cual no es permitido
        self.check_invalid_move(start_coord, end_coord)

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
