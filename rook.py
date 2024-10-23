from pieces import Piece

class Rook(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.white_str = "♖"
        self.black_str = "♜"

    def symbol(self):
        return self.white_str if self.color == "WHITE" else self.black_str

    def valid_positions(self, start_row, start_col, end_row, end_col):
        if not (start_row == end_row or start_col == end_col):
            raise ValueError("La torre solo puede moverse en línea recta.")
        return True

    def possible_positions_va(self, row, col):
        """Movimientos verticales hacia arriba"""
        positions = []
        for r in range(row - 1, -1, -1):  # Mueve hacia arriba en las filas
            other_piece = self.board.get_piece(r, col)
            if other_piece is None:
                positions.append((r, col))
            else:
                if other_piece.color != self.color:
                    positions.append((r, col))  # Puede capturar la pieza enemiga
                break  # Detiene el bucle si encuentra cualquier pieza
        return positions

    def possible_positions_vd(self, row, col):
        """Movimientos verticales hacia abajo"""
        positions = []
        for r in range(row + 1, 8):  # Mueve hacia abajo en las filas
            other_piece = self.board.get_piece(r, col)
            if other_piece is None:
                positions.append((r, col))
            else:
                if other_piece.color != self.color:
                    positions.append((r, col))  # Puede capturar la pieza enemiga
                break  # Detiene el bucle si encuentra cualquier pieza
        return positions

    def possible_positions_hr(self, row, col):
        """Movimientos horizontales hacia la derecha"""
        positions = []
        for c in range(col + 1, 8):  # Mueve hacia la derecha en las columnas
            other_piece = self.board.get_piece(row, c)
            if other_piece is None:
                positions.append((row, c))
            else:
                if other_piece.color != self.color:
                    positions.append((row, c))  # Puede capturar la pieza enemiga
                break  # Detiene el bucle si encuentra cualquier pieza
        return positions

    def possible_positions_hl(self, row, col):
        """Movimientos horizontales hacia la izquierda"""
        positions = []
        for c in range(col - 1, -1, -1):  # Mueve hacia la izquierda en las columnas
            other_piece = self.board.get_piece(row, c)
            if other_piece is None:
                positions.append((row, c))
            else:
                if other_piece.color != self.color:
                    positions.append((row, c))  # Puede capturar la pieza enemiga
                break  # Detiene el bucle si encuentra cualquier pieza
        return positions

    def is_row_col_in_valid_positions(self, to_row, to_col, possible_positions):
        """
        Verifica si la posición destino (to_row, to_col) está dentro de las posiciones posibles.
        """
        return (to_row, to_col) in possible_positions
