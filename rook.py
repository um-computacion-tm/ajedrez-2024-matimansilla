from pieces import Piece

class Rook(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)  # Se pasa 'board' al constructor de la clase base
        self.board = board
        self.white_str = "♖"
        self.black_str = "♜"

    def __str__(self):
        return self.white_str if self.color == "white" else self.black_str

    def valid_positions(self, start_row, start_col, end_row, end_col):
        # Validamos si el movimiento es válido: solo movimientos en línea recta
        if start_row != end_row and start_col != end_col:
            raise ValueError("La torre solo puede moverse en línea recta.")
        return True

    def possible_positions_va(self, row, col):
        possibles = []
        for r in range(row - 1, -1, -1):
            if self.board.get_piece(r, col) is None:
                possibles.append((r, col))
            else:
                break
        return possibles

    def possible_positions_vd(self, row, col):
        possibles = []
        for r in range(row + 1, 8):
            if self.board.get_piece(r, col) is None:
                possibles.append((r, col))
            else:
                break
        return possibles

    def possible_positions_hr(self, row, col):
        possibles = []
        for c in range(col + 1, 8):
            if self.board.get_piece(row, c) is None:
                possibles.append((row, c))
            else:
                break
        return possibles

    def possible_positions_hl(self, row, col):
        possibles = []
        for c in range(col - 1, -1, -1):
            if self.board.get_piece(row, c) is None:
                possibles.append((row, c))
            else:
                break
        return possibles
