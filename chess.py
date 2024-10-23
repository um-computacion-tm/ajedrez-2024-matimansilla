from board import Board
from exceptions import InvalidMove, InvalidTurn, EmptyPosition

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def make_move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition("No hay ninguna pieza en la posición de origen")
        if piece.get_color() != self.__turn__:
            raise InvalidTurn("No es tu turno")
        if not piece.valid_positions(to_row, to_col):
            raise InvalidMove("Movimiento destino inválido")
        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

    def get_turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def is_game_over(self):
        return self.__board__.count_pieces("WHITE") == 0 or self.__board__.count_pieces("BLACK") == 0
