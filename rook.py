from pieces import Piece

class Rook(Piece):

    def symbol(self):
        return '♖' if self.get_color() == 'WHITE' else '♜'

    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_moves = self.get_possible_moves(from_row, from_col)
        return (to_row, to_col) in [(move[0], move[1]) for move in possible_moves]  

    def get_possible_moves(self, from_row, from_col):
        directions = self.get_rook_directions()
        return self.find_valid_moves(from_row, from_col, directions)

    def get_rook_directions(self):
        return [(1, 0), (-1, 0), (0, -1), (0, 1)]
