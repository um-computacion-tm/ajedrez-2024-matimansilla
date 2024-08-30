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
        self.white_str = "♖"
        self.black_str = "♜"

class Pawn(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.white_str = "♙"
        self.black_str = "♟"
