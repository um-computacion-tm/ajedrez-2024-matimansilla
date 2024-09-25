class Piece:
    def __init__(self, color, board):
        self.color = color
        self.__board__ = board
        self.position = None

    def __str__(self):
        if self.color == "WHITE":
            return self.white_str
        else:
            return self.black_str

    def set_position(self, row, col):
        """Establece la posición de la pieza en el tablero."""
        self.position = (row, col)

    def symbol(self):
        """Devuelve el símbolo de la pieza."""
        return str(self)

    def possible_moves(self):
        """Método base para obtener movimientos posibles (a ser sobrescrito por las piezas específicas)."""
        raise NotImplementedError("Este método debe ser sobrescrito por cada pieza.")

class Rook(Piece):
    white_str = "♖"
    black_str = "♜"

    def __init__(self, color, board):
        super().__init__(color, board)

    def possible_moves(self):
        """Devuelve una lista de posibles movimientos para la torre."""
        return self.__board__.possible_positions_vd(self.position) + \
               self.__board__.possible_positions_va(self.position)


class Pawn(Piece):
    white_str = "♙"
    black_str = "♟"

    def __init__(self, color, board):
        super().__init__(color, board)

    def possible_moves(self):
        """Devuelve una lista de posibles movimientos para el peón."""
        # Lógica específica del peón
        return []  # Ejemplo simplificado


class Knight(Piece):
    white_str = "♘"
    black_str = "♞"

    def __init__(self, color, board):
        super().__init__(color, board)

    def possible_moves(self):
        """Devuelve una lista de posibles movimientos para el caballo."""
        # Lógica específica del caballo
        return []  # Ejemplo simplificado
