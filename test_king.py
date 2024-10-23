import unittest
from king import King
from board import Board
from chess import Chess

class TestKing(unittest.TestCase):

    def setUp(self):
        self.board = Board()  # Inicializa el tablero
        self.king = King("WHITE", self.board)  # Crea un rey

    def check_invalid_move(self, start_pos, end_pos):
        """Verifica que un movimiento inválido no sea permitido."""
        x_origen = start_pos[0]
        y_origen = start_pos[1]
        x_destino = end_pos[0]
        y_destino = end_pos[1]

        resultado_movimiento = self.king.valid_positions(x_origen, y_origen, x_destino, y_destino)

        self.assertFalse(resultado_movimiento)

    def check_valid_move(self, start_pos, end_pos):
        """Confirma que un movimiento válido produzca un resultado verdadero."""
        fila_inicial, columna_inicial = start_pos
        fila_final, columna_final = end_pos

        movimiento_es_valido = self.king.valid_positions(fila_inicial, columna_inicial, fila_final, columna_final)

        self.assertTrue(movimiento_es_valido)

    def test_king_symbol_white(self):
        self.assertEqual(self.king.symbol(), '♔')

    def test_king_symbol_black(self):
        king_black = King("BLACK", self.board)
        self.assertEqual(king_black.symbol(), '♚')

    # TESTEO MOVIMIENTOS

    # Testeo de movimientos válidos
    def test_movement_up(self):
        """Verifica que el rey se desplace hacia arriba de forma correcta."""
        start = (4, 4)
        end = (start[0] - 1, start[1])  # Mueve una fila hacia arriba
        self.check_valid_move(start, end)

    def test_downward_movement(self):
        """Confirma que el rey se desplace hacia abajo correctamente."""
        initial_position = (4, 4)
        target_position = (initial_position[0] + 1, initial_position[1])  # Se mueve una fila hacia abajo
        self.check_valid_move(initial_position, target_position)

    def test_shift_right(self):
        """Evalúa si el rey puede moverse a la derecha de forma válida."""
        position_start = (4, 4)
        position_end = (position_start[0], position_start[1] + 1)  # Movimiento hacia la derecha
        self.check_valid_move(position_start, position_end)

    def test_slide_left(self):
        """Confirma que el rey puede desplazarse a la izquierda de manera válida."""
        position_start = (4, 4)
        position_end = (position_start[0], position_start[1] - 1)  # Mueve una posición a la izquierda
        self.check_valid_move(position_start, position_end)

    def test_diag_up_right(self):
        """Verifica un movimiento diagonal válido hacia la parte superior derecha."""
        coord_initial = (4, 4)
        coord_final = (coord_initial[0] - 1, coord_initial[1] + 1)  # Diagonal superior derecha
        self.check_valid_move(coord_initial, coord_final)

    def test_diag_down_left(self):
        """Confirma que un movimiento diagonal hacia la esquina inferior izquierda es válido."""
        pos_from = (4, 4)
        pos_to = (pos_from[0] + 1, pos_from[1] - 1)  # Diagonal hacia abajo y a la izquierda
        self.check_valid_move(pos_from, pos_to)

    # Testeo de movimientos inválidos
    def test_invalid_vertical_movement(self):
        """Asegura que el rey no pueda saltar verticalmente dos espacios."""
        inicio = (4, 4)  # Coordenada inicial del rey
        objetivo = (inicio[0] - 2, inicio[1])  # Intento de movimiento de dos posiciones hacia arriba
        movimiento_valido = self.king.valid_positions(inicio[0], inicio[1], objetivo[0], objetivo[1])
        
        # Verifica que el movimiento no sea válido
        self.assertFalse(movimiento_valido, "El rey no debe ser capaz de saltar dos espacios verticalmente.")

    def test_wrong_diag_move(self):
        """Valida que un movimiento diagonal largo sea considerado inválido."""
        begin = (4, 4)
        finish = (begin[0] - 2, begin[1] - 2)  # Mueve dos posiciones en diagonal, movimiento ilegal
        self.check_invalid_move(begin, finish)

    def test_illegal_horizontal_jump(self):
        """Asegura que el rey no pueda saltar horizontalmente más de una casilla."""
        start_coord = (4, 4)
        end_coord = (start_coord[0], start_coord[1] + 2)  # Salta dos casillas hacia la derecha, lo cual no es permitido
        self.check_invalid_move(start_coord, end_coord)

    # Testeo de get_possible_moves
    def test_get_possible_moves(self):
        """Evalúa los movimientos posibles del rey en el tablero."""
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
