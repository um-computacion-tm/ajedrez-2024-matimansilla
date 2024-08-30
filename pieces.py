class Piece:
    def __init__(self, color, board):
        self.color = color  # Atributo público
        self.__board__ = board

    def __str__(self):
        if self.color == "WHITE":
            return self.white_str
        else:
            return self.black_str

class Rook(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.white_str = "♖"  # Símbolo para WHITE
        self.black_str = "♜"  # Símbolo para BLACK

    def possible_positions_vd(self, row, col):
        """Devuelve las posiciones posibles hacia abajo (descendente)"""
        positions = []
        for r in range(row + 1, 8):
            if self.__board__.get_piece(r, col) is None:
                positions.append((r, col))
            else:
                break
        return positions

    def possible_positions_va(self, row, col):
        """Devuelve las posiciones posibles hacia arriba (ascendente)"""
        positions = []
        for r in range(row - 1, -1, -1):
            if self.__board__.get_piece(r, col) is None:
                positions.append((r, col))
            else:
                break
        return positions

class Pawn(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.white_str = "♙"
        self.black_str = "♟"
