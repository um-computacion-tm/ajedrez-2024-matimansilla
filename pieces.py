class Piece:
    def __init__(self, color, board):
        self.color = color  # Cambié __color__ a color para acceso directo
        self.__board__ = board
        self._king_queen_directions_ = [
            (-1, -1), (-1, 1), (1, -1), (1, 1),
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]

    def get_directions(self):
        return []

    def get_color(self):
        return self.color  # Acceso al atributo color

    def find_valid_moves(self, row, col, directions, single_step=False):
        valid_moves = []
        position = {'row': row, 'col': col}
        for delta_row, delta_col in directions:
            valid_moves.extend(self.explore_direction(position, delta_row, delta_col, single_step))
        return valid_moves

    def explore_direction(self, position, delta_row, delta_col, single_step):
        row, col = position['row'], position['col']
        current_row, current_col = row + delta_row, col + delta_col
        valid_moves = []
        while self.is_within_board(current_row, current_col):
            target_piece = self.__board__.get_piece(current_row, current_col)
            if target_piece is not None:
                self.handle_target_piece(target_piece, current_row, current_col, valid_moves)
                break
            valid_moves.append((current_row, current_col))
            if single_step:
                break
            current_row, current_col = self.update_position(current_row, current_col, delta_row, delta_col)
        return valid_moves

    def handle_target_piece(self, target_piece, current_row, current_col, valid_moves):
        if target_piece.get_color() != self.get_color():
            valid_moves.append((current_row, current_col))

    def update_position(self, current_row, current_col, delta_row, delta_col):
        return current_row + delta_row, current_col + delta_col

    def is_within_board(self, row, col):
        return all(0 <= x < 8 for x in (row, col))

    def is_own_piece(self, target_piece):
        return target_piece is not None and target_piece.get_color() == self.get_color()
