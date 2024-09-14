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

    def symbol(self):
        """Devuelve el símbolo de la pieza según su color."""
        return str(self)


class Rook(Piece):
    white_str = "♖"
    black_str = "♜"

    def __init__(self, color, board):
        super().__init__(color, board)


class Pawn(Piece):
    white_str = "♙"
    black_str = "♟"

    def __init__(self, color, board):
        super().__init__(color, board)


class Knight(Piece):
    white_str = "♘"
    black_str = "♞"

    def __init__(self, color, board):
        super().__init__(color, board)
        
    def is_valid_piece_move(self, board, from_row, from_col, to_row, to_col):
        """Verifica si el movimiento es válido para el caballo."""
        return (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or \
               (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2)
