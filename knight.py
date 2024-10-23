from pieces import Piece

class Knight(Piece):

    def symbol(self):
        return '♘' if self.get_color() == 'WHITE' else '♞'

    def valid_positions(self, from_row, from_col, to_row, to_col):
        valid_moves = self.get_possible_moves(from_row, from_col)
        return (to_row, to_col) in valid_moves  

    def get_possible_moves(self, from_row, from_col):
        knight_moves = [
            (from_row + 2, from_col + 1), (from_row + 2, from_col - 1),
            (from_row - 2, from_col + 1), (from_row - 2, from_col - 1),
            (from_row + 1, from_col + 2), (from_row + 1, from_col - 2),
            (from_row - 1, from_col + 2), (from_row - 1, from_col - 2)
        ]
        return knight_moves
