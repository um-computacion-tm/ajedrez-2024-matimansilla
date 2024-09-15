class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]  # Tablero de 8x8

    def get_piece(self, row, col):
        if row < 0 or row >= 8 or col < 0 or col >= 8:
            raise IndexError("La posición está fuera de los límites del tablero")
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        if row < 0 or row >= 8 or col < 0 or col >= 8:
            raise IndexError("La posición está fuera de los límites del tablero")
        self.__positions__[row][col] = piece

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if not piece:
            raise ValueError("No hay ninguna pieza en la posición de origen.")
        self.set_piece(to_row, to_col, piece)
        self.set_piece(from_row, from_col, None)

    def __str__(self):
        result = ""
        for row in self.__positions__:
            result += " ".join(str(piece) if piece else "." for piece in row) + "\n"
        return result.strip()
