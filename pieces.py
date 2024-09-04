class Piece:
    def __init__(self, color, board):
        self.color = color  # Atributo público
        self.__board__ = board  # Atributo privado para el tablero
        self.position = None  # Atributo para la posición

    def __str__(self):
        if self.color == "WHITE":
            return self.white_str
        else:
            return self.black_str

    def set_position(self, row, col):
        """Establece la posición de la pieza en el tablero."""
        self.position = (row, col)

class Rook(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.white_str = "♖"  # Símbolo para WHITE
        self.black_str = "♜"  # Símbolo para BLACK

    def possible_positions_vd(self, row, col):
        """Devuelve las posiciones posibles hacia abajo (vertical descendente)."""
        possibles = []
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
        """Devuelve las posiciones posibles hacia arriba (vertical ascendente)."""
        possibles = []
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

class Pawn(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.white_str = "♙"
        self.black_str = "♟"
