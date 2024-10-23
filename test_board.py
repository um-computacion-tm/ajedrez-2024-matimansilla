import unittest



from board import Board
from pieces import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from exceptions import OutOfBoard, RowOutOfBoard, ColumnOutOfBoard


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

    # Cobertura de Casos Generales de Funcionalidad

    def test_get_cell_string_empty(self):
        cell = None
        expected_output = " "
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
        self.assertIsNone(self.board.get_piece(1, 1))  # Verifica que la antigua posición esté vacía

    def test_count_white_pieces(self):
        # Verifica que el conteo de piezas blancas sea correcto
        self.assertEqual(self.board.count_pieces("WHITE"), 18)

    def test_count_black_pieces(self):
        # Verifica que el conteo de piezas negras sea correcto
        self.assertEqual(self.board.count_pieces("BLACK"), 14)

    def test_count_no_pieces(self):
        # Verifica el conteo cuando no hay piezas de un color en el tablero
        self.assertEqual(self.board.count_pieces("RED"), 0)

    # Cobertura de Casos de Error (Manejo de Excepciones)

    def test_get_piece_out_of_range_row_and_col(self):
        with self.assertRaises(OutOfBoard) as exc:
            self.board.get_piece(10, 10)
        self.assertEqual(
            exc.exception.message,
            "La posición (10, 10) se encuentra fuera del tablero."
        )

    def test_get_piece_out_of_range_row(self):
        with self.assertRaises(RowOutOfBoard) as exc:
            self.board.get_piece(10, 0)
        self.assertEqual(
            exc.exception.message,
            "La fila indicada se encuentra fuera del tablero."
        )

    def test_get_piece_out_of_range_col(self):
        with self.assertRaises(ColumnOutOfBoard) as exc:
            self.board.get_piece(0, 10)
        self.assertEqual(
            exc.exception.message,
            "La columna indicada se encuentra fuera del tablero."
        )

    def test_set_piece_out_of_range_row_and_col(self):
        rook = Rook('BLACK', self.board)
        with self.assertRaises(OutOfBoard) as exc:
            self.board.set_piece(10, 10, rook)
        self.assertEqual(
            exc.exception.message,
            "La posición (10, 10) se encuentra fuera del tablero."
        )

    def test_set_piece_out_of_range_row(self):
        rook = Rook('BLACK', self.board)
        with self.assertRaises(RowOutOfBoard) as exc:
            self.board.set_piece(10, 0, rook)
        self.assertEqual(
            exc.exception.message,
            "La fila indicada se encuentra fuera del tablero."
        )

    def test_set_piece_out_of_range_col(self):
        rook = Rook('BLACK', self.board)
        with self.assertRaises(ColumnOutOfBoard) as exc:
            self.board.set_piece(0, 10, rook)
        self.assertEqual(
            exc.exception.message,
            "La columna indicada se encuentra fuera del tablero."
        )

    # Pruebas adicionales del Estado Inicial del Tablero y Movimientos

    def test_rooks_creation(self):
        self.board.rook_positions()  # Coloca las torres
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertEqual(self.board.get_piece(0, 0).color, 'BLACK')
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertEqual(self.board.get_piece(0, 7).color, 'BLACK')
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).color, 'WHITE')
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        self.assertEqual(self.board.get_piece(7, 7).color, 'WHITE')

    def test_pawns_creation(self):
        self.board.pawn_positions()  # Coloca los peones
        self.assertIsInstance(self.board.get_piece(1, 0), Pawn)
        self.assertEqual(self.board.get_piece(1, 0).color, 'BLACK')
        self.assertIsInstance(self.board.get_piece(6, 0), Pawn)
        self.assertEqual(self.board.get_piece(6, 0).color, 'WHITE')

    def test_empty_spaces(self):
        self.assertIsNone(self.board.get_piece(2, 0))
        self.assertIsNone(self.board.get_piece(3, 0))

    def test_move_rook(self):
        rook = Rook(color='BLACK', board=self.board)
        self.board.set_piece(0, 0, rook)
        self.board.move(0, 0, 0, 1)

        self.assertIsInstance(self.board.get_piece(0, 1), Rook)
        self.assertEqual(self.board.get_piece(0, 1).color, 'BLACK')
        self.assertIsNone(self.board.get_piece(0, 0))  # Verifica que la posición inicial esté vacía

        self.assertEqual(
            str(self.board),
            (
                ".♜.....♜\n"
                "♟♟♟♟♟♟♟♟\n"
                "........\n"
                "........\n"
                "........\n"
                "........\n"
                "♙♙♙♙♙♙♙♙\n"
                "♖......♖\n"  # Actualizado el formato del tablero
            )
        )


if __name__ == '__main__':
    unittest.main()
