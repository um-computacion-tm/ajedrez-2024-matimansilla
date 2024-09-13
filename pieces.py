class Piece:
    def __init__(self, color, board):
        self.color = color  # Atributo público
        self.__board__ = board  # Atributo privado para el tablero
        self.position = None  # Atributo para la posición

    def __str__(self):
        if self.color == "WHITE":
            return self.white_str
        else:
            return self.black_str

    def set_position(self, row, col):
        """Establece la posición de la pieza en el tablero."""
        self.position = (row, col)

    def symbol(self):
        """Devuelve el símbolo de la pieza según su color."""
        return str(self)


class Rook(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.white_str = "♖"  # Símbolo para WHITE
        self.black_str = "♜"  # Símbolo para BLACK

    def possible_positions_vd(self, row, col):
        """Devuelve las posiciones posibles hacia abajo (vertical descendente)."""
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
        """Devuelve las posiciones posibles hacia arriba (vertical ascendente)."""
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


class Pawn(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.white_str = "♙"  # Símbolo para WHITE
        self.black_str = "♟"  # Símbolo para BLACK


class Knight(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.white_str = "♘"  # Símbolo para el caballo blanco
        self.black_str = "♞"  # Símbolo para el caballo negro
        
    def is_valid_piece_move(self, board, from_row, from_col, to_row, to_col):
        """Verifica si el movimiento es válido para el caballo."""
        # El caballo se mueve en forma de "L"
        return (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or \
               (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2)
