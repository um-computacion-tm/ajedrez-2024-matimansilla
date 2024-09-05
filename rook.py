from pieces import Piece

class Rook(Piece):
    white_str = "♖"
    black_str = "♜"

    def __init__(self, color, board):
        super().__init__(color, board)
        # El método set_position se utilizará para establecer la posición en el tablero

    def possible_positions_vd(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is None:
                possibles.append((next_row, col))
            elif other_piece.color != self.color:
                possibles.append((next_row, col))
                break
            else:
                break
        return possibles

    def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is None:
                possibles.append((next_row, col))
            elif other_piece.color != self.color:
                possibles.append((next_row, col))
                break
            else:
                break
        return possibles
