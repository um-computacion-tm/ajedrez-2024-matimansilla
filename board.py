from rook import Rook
from pieces import Pawn
from exceptions import OutOfBoard, RowOutOfBoard, ColumnOutOfBoard

class Board:
    def __init__(self, for_test=False):
        # Inicializa el tablero como una lista bidimensional 8x8 con None
        self.__positions__ = []
        for _ in range(8):
            col = [None] * 8  # Inicializa las filas con celdas vacías
            self.__positions__.append(col)
        
        if not for_test:  # Si no es para test, coloca las piezas
            self.rook_positions()
            self.pawn_positions()

    def __str__(self):
        """Devuelve una representación en cadena del tablero."""
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)  # Representación de la pieza
                else:
                    board_str += "."  # Representación para celdas vacías
            board_str += "\n"
        return board_str.strip()  # Eliminar el último salto de línea

    def get_piece(self, row, col):
        """Devuelve la pieza en la posición (row, col) si está dentro de los límites del tablero."""
        if 0 <= row < 8 and 0 <= col < 8:  # Verifica que los índices estén dentro del rango
            return self.__positions__[row][col]
        raise OutOfBoard(f"La posición ({row}, {col}) se encuentra fuera del tablero.")

    def set_piece(self, row, col, piece):
        """Coloca una pieza en la posición (row, col) del tablero, si está dentro de los límites."""
        if 0 <= row < 8 and 0 <= col < 8:  # Verifica que los índices estén dentro del rango
            self.__positions__[row][col] = piece
        elif row >= 8:
            raise RowOutOfBoard(f"La fila {row} está fuera del rango del tablero.")
        elif col >= 8:
            raise ColumnOutOfBoard(f"La columna {col} está fuera del rango del tablero.")
        else:
            raise OutOfBoard(f"La posición ({row}, {col}) está fuera del rango del tablero.")

    def rook_positions(self):
        """Coloca las torres (rooks) en sus posiciones iniciales."""
        self.set_piece(0, 0, Rook("BLACK", self))
        self.set_piece(0, 7, Rook("BLACK", self))
        self.set_piece(7, 0, Rook("WHITE", self))
        self.set_piece(7, 7, Rook("WHITE", self))

    def pawn_positions(self):
        """Coloca los peones (pawns) en sus posiciones iniciales."""
        for col in range(8):
            self.set_piece(1, col, Pawn("BLACK", self))
            self.set_piece(6, col, Pawn("WHITE", self))

    def move(self, from_row, from_col, to_row, to_col):
        """Mueve una pieza de una posición a otra."""
        # Obtiene la pieza en la posición inicial
        origin = self.get_piece(from_row, from_col)

        if origin is None:
            raise ValueError(f"No hay ninguna pieza en la posición inicial ({from_row}, {from_col}).")

        # Coloca la pieza en la posición destino
        self.set_piece(to_row, to_col, origin)

        # Vacía la posición inicial
        self.set_piece(from_row, from_col, None)
