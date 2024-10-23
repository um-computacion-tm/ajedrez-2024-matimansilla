from chess.pieces import Piece

class King(Piece):
    white_str = "♔"
    black_str = "♚"

    def symbol(self):
        return self.white_str if self.get_color() == 'WHITE' else self.black_str

    def valid_positions(self, from_row, from_col, to_row, to_col):
        if not self.is_within_board(to_row, to_col):
            return False
        directions = self._king_queen_directions_
        possible_positions = self.get_possible_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions

    def get_possible_moves(self, from_row, from_col, directions):
        return self.find_valid_moves(from_row, from_col, directions, single_step=True)

    def get_possible_positions(self, from_row, from_col):
        possibles = self.possible_orthogonal_positions(from_row, from_col) + self.possible_diagonal_positions(from_row, from_col)
        possible_king = []
        for (possible_row, possible_col) in possibles:
            if abs(from_row - possible_row) <= 1 and abs(from_col - possible_col) <= 1:
                possible_king.append((possible_row, possible_col))
        return possible_king
