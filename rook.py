from pieces import Piece

class Rook(Piece):
    white_str = "♖"
    black_str = "♜"

    def __init__(self, color, board):
        super().__init__(color, board)

    def symbol(self):
        """Devuelve el símbolo de la pieza según su color."""
        return str(self)

    def __str__(self):
        """Devuelve el símbolo correspondiente según el color de la pieza."""
        return self.white_str if self.color == 'white' else self.black_str

    def possible_positions_vd(self, row, col):
        """Movimientos verticales hacia abajo."""
        possibles = []
        if not (0 <= row < 8 and 0 <= col < 8):
            raise ValueError("Posición fuera de los límites del tablero.")
        for next_row in range(row + 1, 8):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is None:
                possibles.append((next_row, col))
            elif other_piece.color != self.color:
                possibles.append((next_row, col))
                break
            else:
                break
        return possibles

    def possible_positions_va(self, row, col):
        """Movimientos verticales hacia arriba."""
        possibles = []
        if not (0 <= row < 8 and 0 <= col < 8):
            raise ValueError("Posición fuera de los límites del tablero.")
        for next_row in range(row - 1, -1, -1):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is None:
                possibles.append((next_row, col))
            elif other_piece.color != self.color:
                possibles.append((next_row, col))
                break
            else:
                break
        return possibles

    def possible_positions_hd(self, row, col):
        """Movimientos horizontales hacia la derecha."""
        possibles = []
        if not (0 <= row < 8 and 0 <= col < 8):
            raise ValueError("Posición fuera de los límites del tablero.")
        for next_col in range(col + 1, 8):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is None:
                possibles.append((row, next_col))
            elif other_piece.color != self.color:
                possibles.append((row, next_col))
                break
            else:
                break
        return possibles

    def possible_positions_ha(self, row, col):
        """Movimientos horizontales hacia la izquierda."""
        possibles = []
        if not (0 <= row < 8 and 0 <= col < 8):
            raise ValueError("Posición fuera de los límites del tablero.")
        for next_col in range(col - 1, -1, -1):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is None:
                possibles.append((row, next_col))
            elif other_piece.color != self.color:
                possibles.append((row, next_col))
                break
            else:
                break
        return possibles

    def possible_positions(self, row, col):
        """Devuelve todas las posibles posiciones (verticales y horizontales)."""
        return (self.possible_positions_vd(row, col) + 
                self.possible_positions_va(row, col) + 
                self.possible_positions_hd(row, col) + 
                self.possible_positions_ha(row, col))
