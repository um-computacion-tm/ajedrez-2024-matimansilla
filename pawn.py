from chess.pieces import Piece
from chess.queen import Queen

class Pawn(Piece):

    def __init__(self, color, board):
        super().__init__(color, board)  

    def symbol(self):
        return '♙' if self.get_color() == 'WHITE' else '♟'

    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_moves = self.get_possible_moves(from_row, from_col)
        return any(move == (to_row, to_col) for move in possible_moves)
        
    def get_possible_moves(self, from_row, from_col):
        moves = []
        direction = self.get_move_direction() 
        start_row = self.get_start_row()      
        self.add_forward_moves(from_row, from_col, direction, moves)
        self.add_capture_moves(from_row, from_col, direction, moves)
        return moves

    def add_forward_moves(self, from_row, from_col, direction, moves):
        start_row = self.get_start_row()
        if self.is_empty(from_row + direction, from_col):
            moves.append((from_row + direction, from_col))
            if from_row == start_row and self.is_empty(from_row + 2 * direction, from_col):  # Corregido aquí
                moves.append((from_row + 2 * direction, from_col))

    def add_capture_moves(self, from_row, from_col, direction, moves):
        capture_moves = [(direction, -1), (direction, 1)]
        for move in capture_moves:
            next_row, next_col = from_row + move[0], from_col + move[1]
            if self.is_in_bounds(next_row, next_col) and self.can_capture(next_row, next_col):
                moves.append((next_row, next_col))

    def get_move_direction(self):
        return -1 if self.get_color() == 'WHITE' else 1

    def get_start_row(self):
        return 6 if self.get_color() == 'WHITE' else 1 

    def is_in_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def is_empty(self, row, col):
        return self.is_in_bounds(row, col) and self.__board__.get_piece(row, col) is None

    def can_capture(self, row, col):
        piece = self.__board__.get_piece(row, col)
        return piece is not None and piece.get_color() != self.get_color()
