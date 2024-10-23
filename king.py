from pieces import Piece

class King(Piece):

    def symbol(self):
        return '♔' if self.get_color() == 'WHITE' else '♚'

    def valid_positions(self, from_row, from_col, to_row, to_col):
        if not self.is_within_board(to_row, to_col):
            return False 
        directions = self._king_queen_directions_
        possible_positions = self.get_possible_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions

    def get_possible_moves(self, from_row, from_col, directions):
        return self.find_valid_moves(from_row, from_col, directions, single_step=True)
