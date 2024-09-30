from pieces import Piece

class Rook(Piece):
    def valid_positions(self, start_row, start_col, end_row, end_col):
        # La torre solo se mueve en línea recta, por lo que debe estar en la misma fila o columna.
        if start_row == end_row or start_col == end_col:
            return True
        return False

    def possible_positions_va(self, row, col):
        """
        Retorna las posiciones válidas hacia arriba (ascendente) desde la posición actual.
        """
        positions = []
        for r in range(row - 1, -1, -1):  # Recorre hacia arriba (menores índices de fila)
            if not self.board.is_empty(r, col):
                if self.board.is_enemy(r, col, self.color):
                    positions.append((r, col))  # Puede capturar la pieza enemiga
                break  # Si encuentra cualquier pieza, no puede avanzar más allá
            positions.append((r, col))
        return positions

    def possible_positions_vd(self, row, col):
        """
        Retorna las posiciones válidas hacia abajo (descendente) desde la posición actual.
        """
        positions = []
        for r in range(row + 1, 8):  # Recorre hacia abajo (mayores índices de fila)
            if not self.board.is_empty(r, col):
                if self.board.is_enemy(r, col, self.color):
                    positions.append((r, col))  # Puede capturar la pieza enemiga
                break  # Si encuentra cualquier pieza, no puede avanzar más allá
            positions.append((r, col))
        return positions

    def possible_positions_hr(self, row, col):
        """
        Retorna las posiciones válidas hacia la derecha (horizontalmente) desde la posición actual.
        """
        positions = []
        for c in range(col + 1, 8):  # Recorre hacia la derecha (mayores índices de columna)
            if not self.board.is_empty(row, c):
                if self.board.is_enemy(row, c, self.color):
                    positions.append((row, c))  # Puede capturar la pieza enemiga
                break  # Si encuentra cualquier pieza, no puede avanzar más allá
            positions.append((row, c))
        return positions

    def possible_positions_hl(self, row, col):
        """
        Retorna las posiciones válidas hacia la izquierda (horizontalmente) desde la posición actual.
        """
        positions = []
        for c in range(col - 1, -1, -1):  # Recorre hacia la izquierda (menores índices de columna)
            if not self.board.is_empty(row, c):
                if self.board.is_enemy(row, c, self.color):
                    positions.append((row, c))  # Puede capturar la pieza enemiga
                break  # Si encuentra cualquier pieza, no puede avanzar más allá
            positions.append((row, c))
        return positions

