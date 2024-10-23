from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn
from exceptions import OutOfBoard, RowOutOfBoard, ColumnOutOfBoard, OriginInvalidMove

class Board:
    """
    Clase que representa el tablero de ajedrez.
    Gestiona las posiciones de las piezas y las operaciones sobre el tablero.
    """

    def __init__(self, for_test=False):
        """
        Inicializa el tablero de ajedrez como una matriz de 8x8 con valores
        None en todas las posiciones. Coloca las piezas en sus posiciones iniciales
        si for_test es False.
        """
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        if not for_test:
            self.setup_pieces()

    def __str__(self):
        """
        Convierte el estado actual del tablero en una cadena de texto con símbolos.
        """
        return self.build_board_string()

    def setup_pieces(self):
        """
        Coloca todas las piezas en las posiciones iniciales.
        """
        # Piezas negras
        self.__positions__[0][0] = Rook('BLACK', self)
        self.__positions__[0][1] = Knight('BLACK', self)
        self.__positions__[0][2] = Bishop('BLACK', self)
        self.__positions__[0][3] = Queen('BLACK', self)
        self.__positions__[0][4] = King('BLACK', self)
        self.__positions__[0][5] = Bishop('BLACK', self)
        self.__positions__[0][6] = Knight('BLACK', self)
        self.__positions__[0][7] = Rook('BLACK', self)
        for i in range(8):
            self.__positions__[1][i] = Pawn('BLACK', self)

        # Piezas blancas
        self.__positions__[7][0] = Rook('WHITE', self)
        self.__positions__[7][1] = Knight('WHITE', self)
        self.__positions__[7][2] = Bishop('WHITE', self)
        self.__positions__[7][3] = Queen('WHITE', self)
        self.__positions__[7][4] = King('WHITE', self)
        self.__positions__[7][5] = Bishop('WHITE', self)
        self.__positions__[7][6] = Knight('WHITE', self)
        self.__positions__[7][7] = Rook('WHITE', self)
        for i in range(8):
            self.__positions__[6][i] = Pawn('WHITE', self)

    def build_board_string(self):
        """
        Construye la representación del tablero como una cadena de texto.
        """
        board_str = "   0  1  2  3  4  5  6  7\n"
        for i, row in enumerate(self.__positions__):
            board_str += f"{i}  "  # Número de fila
            for cell in row:
                board_str += self.get_cell_string(cell) + "  "
            board_str += "\n"
        return board_str.strip()

    def get_cell_string(self, cell):
        """
        Devuelve el símbolo de la pieza o un espacio si está vacía.
        """
        return cell.symbol() if cell is not None else "."

    def validate_position(self, row, col):
        """
        Verifica si una posición está dentro de los límites del tablero.
        """
        if row < 0 or row >= 8:
            raise RowOutOfBoard()
        if col < 0 or col >= 8:
            raise ColumnOutOfBoard()

    def get_piece(self, row, col):
        """
        Obtiene la pieza en una posición específica del tablero.
        """
        self.validate_position(row, col)
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        """
        Coloca una pieza en una posición específica del tablero.
        """
        self.validate_position(row, col)
        self.__positions__[row][col] = piece

    def move(self, from_row, from_col, to_row, to_col):
        """
        Mueve una pieza de una posición a otra.
        """
        self.validate_position(from_row, from_col)
        self.validate_position(to_row, to_col)
        origin = self.get_piece(from_row, from_col)
        if origin is None:
            raise OriginInvalidMove()
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)

    def count_pieces(self, color):
        """
        Cuenta cuántas piezas de un color específico están en el tablero.
        """
        count = 0
        for row in self.__positions__:
            count += self.count_color_in_row(row, color)
        return count

    def count_color_in_row(self, row, color):
        """
        Cuenta cuántas piezas de un color específico están en una fila.
        """
        count = 0
        for piece in row:
            if self.is_piece_color(piece, color):
                count += 1
        return count

    def is_piece_color(self, piece, color):
        """
        Verifica si una pieza es de un color específico.
        """
        return piece is not None and piece.get_color() == color
