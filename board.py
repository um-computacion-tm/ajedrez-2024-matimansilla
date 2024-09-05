from pieces import Rook, Pawn

class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]

        # Inicializar las torres
        self.__positions__[0][0] = Rook("BLACK", self)
        self.__positions__[0][7] = Rook("BLACK", self)
        self.__positions__[7][0] = Rook("WHITE", self)
        self.__positions__[7][7] = Rook("WHITE", self)

        # Inicializar los peones
        for col in range(8):
            self.__positions__[6][col] = Pawn("WHITE", self)
            self.__positions__[1][col] = Pawn("BLACK", self)

    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    def place_piece(self, piece, row, col):
        """Coloca una pieza en la posición dada y actualiza su posición interna."""
        self.set_piece(row, col, piece)
        piece.set_position(row, col)  # Asegura que la pieza tenga la posición actualizada

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str
