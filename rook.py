from pieces import Piece

class Rook(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)

    def symbol(self):
        """Retorna el símbolo correspondiente a la torre según su color"""
        return 'R' if self.color == 'WHITE' else 'r'

    def possible_positions(self, row, col):
        """Retorna todas las posiciones posibles (verticales y horizontales)"""
        positions = []
        positions += self.possible_positions_vertical_asc(row, col)
        positions += self.possible_positions_vertical_desc(row, col)
        positions += self.possible_positions_horizontal_left(row, col)
        positions += self.possible_positions_horizontal_right(row, col)
        return positions

    def possible_positions_vertical_asc(self, row, col):
        """Movimiento vertical ascendente"""
        positions = []
        for r in range(row - 1, -1, -1):
            if not self.add_position_if_valid(positions, r, col):
                break
        return positions

    def possible_positions_vertical_desc(self, row, col):
        """Movimiento vertical descendente"""
        positions = []
        for r in range(row + 1, 8):
            if not self.add_position_if_valid(positions, r, col):
                break
        return positions

    def possible_positions_horizontal_left(self, row, col):
        """Movimiento horizontal hacia la izquierda"""
        positions = []
        for c in range(col - 1, -1, -1):
            if not self.add_position_if_valid(positions, row, c):
                break
        return positions

    def possible_positions_horizontal_right(self, row, col):
        """Movimiento horizontal hacia la derecha"""
        positions = []
        for c in range(col + 1, 8):
            if not self.add_position_if_valid(positions, row, c):
                break
        return positions

    def add_position_if_valid(self, positions, row, col):
        """Verifica si una posición es válida y, si es así, la añade a la lista"""
        piece = self.board.get_piece(row, col)
        if piece is None:
            positions.append((row, col))
            return True
        elif piece.color != self.color:
            positions.append((row, col))
        return False
