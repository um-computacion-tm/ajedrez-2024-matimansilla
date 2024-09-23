from rook import Rook
from pawn import Pawn

class Board:
    def __init__(self, for_test=False):
        self.__positions__ = []
        for _ in range(8):
            col = [None] * 8  # Inicializa las filas con celdas vacías
            self.__positions__.append(col)
        
        if not for_test:  # Si no es para test, coloca las piezas
            self.rook_positions()
            self.pawn_positions()

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)  # Representación de la pieza
                else:
                    board_str += " "  # Espacio para celdas vacías
            board_str += "\n"
        return board_str.strip()  # Eliminar el último salto de línea

    def get_piece(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:  # Verifica que los índices estén dentro del rango
            return self.__positions__[row][col]
        return None  # Si está fuera de rango, retorna None

    def set_piece(self, row, col, piece):
        if 0 <= row < 8 and 0 <= col < 8:  # Verifica que los índices estén dentro del rango
            self.__positions__[row][col] = piece

    def rook_positions(self):
        self.__positions__[0][0] = Rook("BLACK", self)
        self.__positions__[0][7] = Rook("BLACK", self)
        self.__positions__[7][7] = Rook("WHITE", self)
        self.__positions__[7][0] = Rook("WHITE", self)

    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)

    def pawn_positions(self):
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK", self)
            self.__positions__[6][col] = Pawn("WHITE", self)