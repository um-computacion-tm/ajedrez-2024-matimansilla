from pieces import Piece

class Bishop(Piece):
    """Clase que representa un alfil en el juego de ajedrez."""
    
    def __init__(self, color, board):
        super().__init__(color, board)  # Inicializa el color y el tablero en la clase base
        self.white_str = '♗'  # Símbolo del alfil blanco
        self.black_str = '♝'  # Símbolo del alfil negro

    def symbol(self):
        """Devuelve el símbolo del alfil dependiendo de su color."""
        return self.white_str if self.color == "WHITE" else self.black_str

    def valid_positions(self, from_row, from_col, to_row, to_col):
        """Verifica si el movimiento es válido en diagonal."""
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        # Verifica que el movimiento sea diagonal
        return row_diff == col_diff and row_diff > 0

    def get_possible_positions(self, from_row, from_col):
        """Devuelve las posiciones diagonales posibles para el alfil."""
        return self.possible_diagonal_positions(from_row, from_col)

    def possible_diagonal_positions(self, from_row, from_col):
        """Genera las posiciones diagonales posibles."""
        possible_positions = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonales: arriba-izquierda, arriba-derecha, abajo-izquierda, abajo-derecha
        
        for direction in directions:
            row, col = from_row, from_col
            
            while 0 <= row < 8 and 0 <= col < 8:  # Asegura que las posiciones están dentro del tablero
                possible_positions.append((row, col))
                row += direction[0]
                col += direction[1]

        return possible_positions
