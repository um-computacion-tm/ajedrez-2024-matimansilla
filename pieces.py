class Piece:
    def __init__(self, color, board):
        self.color = color
        self.__board__ = board
        self.position = None

    def __str__(self):
        if self.color == "WHITE":
            return self.white_str
        else:
            return self.black_str

    def set_position(self, row, col):
        """Establece la posición de la pieza en el tablero."""
        self.position = (row, col)

    def symbol(self):
        """Devuelve el símbolo de la pieza."""
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
