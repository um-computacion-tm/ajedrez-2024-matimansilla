from pieces import Piece

class Queen(Piece):
    white_str = "♕"  # Símbolo de la reina blanca
    black_str = "♛"  # Símbolo de la reina negra

    def symbol(self):
        """Devuelve el símbolo correspondiente a la reina según su color."""
        return '♕' if self.get_color() == 'WHITE' else '♛'

    def valid_positions(self, from_row, from_col, to_row, to_col):
        """Verifica si el movimiento de la reina desde una posición inicial a una posición destino es válido."""
        return self._is_valid_move(from_row, from_col, to_row, to_col)

    def _is_valid_move(self, from_row, from_col, to_row, to_col):
        """Determina si el movimiento a la posición de destino es válido."""
        directions = self._king_queen_directions_  # Direcciones en las que la reina puede moverse
        possible_positions = self.get_possible_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions  # Retorna True si la posición de destino es válida

    def get_possible_moves(self, from_row, from_col, directions):
        """Obtiene todas las posiciones válidas a las que la reina puede moverse desde su posición actual."""
        return self.find_valid_moves(from_row, from_col, directions, single_step=False)

    def get_possible_positions(self, from_row, from_col):
        """Devuelve las posiciones posibles que la reina puede alcanzar, combinando movimientos ortogonales y diagonales."""
        return self.possible_orthogonal_positions(from_row, from_col) + \
               self.possible_diagonal_positions(from_row, from_col)
