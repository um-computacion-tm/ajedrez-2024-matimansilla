import unittest
from board import Board
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn
from exceptions import *


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.pawn_white1 = Pawn("WHITE", self.board)
        self.pawn_white2 = Pawn("WHITE", self.board)
        self.pawn_black = Pawn("BLACK", self.board)
        # Coloca algunas piezas en el tablero
        self.board.set_piece(0, 0, self.pawn_white1)
        self.board.set_piece(1, 1, self.pawn_black)
        self.board.set_piece(0, 1, self.pawn_white2)

    def test_get_cell_string_empty(self):
        cell = None
        expected_output = "."
        self.assertEqual(self.board.get_cell_string(cell), expected_output)

    def test_get_cell_string_with_piece(self):
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(0, 0, pawn)  # Coloca un peón en la celda (0, 0)

        expected_output = pawn.symbol()  # Se espera que devuelva el símbolo del peón
        self.assertEqual(self.board.get_cell_string(self.board.get_piece(0, 0)), expected_output)

    def test_move_valid(self):
        # Mueve el peón de (1, 1) a (2, 1)
        self.board.move(1, 1, 2, 1)
        self.assertEqual(self.board.get_piece(2, 1), self.pawn_black)
        # Verifica que la antigua posición está vacía
        self.assertIsNone(self.board.get_piece(1, 1))

    def test_count_white_pieces(self):
        # Verifica que el conteo de piezas blancas sea correcto
        self.assertEqual(self.board.count_pieces("WHITE"), 18)

    def test_count_black_pieces(self):
        # Verifica que el conteo de piezas negras sea correcto
        self.assertEqual(self.board.count_pieces("BLACK"), 14)

    def test_count_no_pieces(self):
        # Verifica el conteo cuando no hay piezas de un color en el tablero
        self.assertEqual(self.board.count_pieces("RED"), 0)


if __name__ == '__main__':
    unittest.main()