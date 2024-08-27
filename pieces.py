class Piece:
    def __init__(self, color):
        self.__color__ = color

    def get_color(self):
        return self.__color__

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.color = color

    def __str__(self):
        return "R" if self.color == "WHITE" else "r"

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.color = color
        self.name = 'Pawn'
    
    def __str__(self):
        return "P" if self.color == "WHITE" else "p"
    
    def possible_moves(self, current_position, board):
        moves = []
        row, col = current_position
        direction = -1 if self.color == 'WHITE' else 1  # Blancos hacia arriba, negros hacia abajo
        
        # Movimiento simple hacia adelante
        new_row = row + direction
        if 0 <= new_row < 8 and board.get_piece(new_row, col) is None:
            moves.append((new_row, col))
            
            # Movimiento doble desde la posición inicial
            if (self.color == 'WHITE' and row == 6) or (self.color == 'BLACK' and row == 1):
                new_row = row + 2 * direction
                if board.get_piece(new_row, col) is None:
                    moves.append((new_row, col))
        
        # Captura en diagonal
        for new_col in [col - 1, col + 1]:
            if 0 <= new_col < 8:
                piece = board.get_piece(row + direction, new_col)
                if piece is not None and piece.get_color() != self.get_color():
                    moves.append((row + direction, new_col))
        
        return moves

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.color = color
        self.name = 'Knight'

    def __str__(self):
        return "N" if self.color == "WHITE" else "n"

    def possible_moves(self, current_position, board):
        moves = []
        row, col = current_position
        move_offsets = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for offset in move_offsets:
            new_row = row + offset[0]
            new_col = col + offset[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:  # Dentro del tablero
                piece = board.get_piece(new_row, new_col)
                if piece is None or piece.get_color() != self.get_color():
                    moves.append((new_row, new_col))
        
        return moves
