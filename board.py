from rook import Rook
from pieces import Pawn

class Board:
    def __init__(self, for_test=False):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        if not for_test:
            # Inicializa las torres (Rook) y peones (Pawn)
            self.set_piece(0, 0, Rook('BLACK', self))
            self.set_piece(0, 7, Rook('BLACK', self))
            for col in range(8):
                self.set_piece(1, col, Pawn('BLACK', self))
                self.set_piece(6, col, Pawn('WHITE', self))
            self.set_piece(7, 0, Rook('WHITE', self))
            self.set_piece(7, 7, Rook('WHITE', self))

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def move(self, start_row, start_col, end_row, end_col):
        piece = self.get_piece(start_row, start_col)
        self.set_piece(end_row, end_col, piece)
        self.set_piece(start_row, start_col, None)

    def __str__(self):
        def piece_str(piece):
            if piece is None:
                return " "
            return piece.symbol()

        rows = []
        for row in self.__positions__:
            rows.append("".join([piece_str(piece) for piece in row]))
        return "\n".join(rows)
