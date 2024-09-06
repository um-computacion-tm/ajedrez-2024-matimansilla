import unittest
from board import Board
from pieces import Pawn
from rook import Rook
from exceptions import OutOfBoard, RowOutOfBoard, ColumnOutOfBoard

class TestBoard(unittest.TestCase):
    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♖      ♖\n"
                "♙♙♙♙♙♙♙♙\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♟♟♟♟♟♟♟♟\n"
                "♜      ♜\n"
            )
        )
        
    def test_get_piece_in_range(self):
        board = Board()
        self.assertIsInstance(board.get_piece(0, 0), Rook)
        self.assertIsNone(board.get_piece(2, 0))

    def test_get_piece_out_of_range_row_and_col(self):
        board = Board(for_test=True)
        with self.assertRaises(OutOfBoard) as exc:
            board.get_piece(10, 10)
        self.assertEqual(
            exc.exception.message,
            "La posición está fuera de los límites del tablero"
        )

    def test_get_piece_out_of_range_row(self):
        board = Board(for_test=True)
        with self.assertRaises(RowOutOfBoard) as exc:
            board.get_piece(10, 0)
        self.assertEqual(
            exc.exception.message,
            "La fila seleccionada está fuera del tablero"
        )

    def test_get_piece_out_of_range_col(self):
        board = Board(for_test=True)
        with self.assertRaises(ColumnOutOfBoard) as exc:
            board.get_piece(0, 10)
        self.assertEqual(
            exc.exception.message,
            "La columna seleccionada está fuera del tablero"
        )

    def test_set_piece_in_range(self):
        board = Board(for_test=True)
        rook = Rook('BLACK', board)
        self.assertIsNone(board.get_piece(0, 0))
        board.set_piece(0, 0, rook)
        self.assertIsInstance(board.get_piece(0, 0), Rook)

    def test_set_piece_out_of_range_row_and_col(self):
        board = Board(for_test=True)
        rook = Rook('BLACK', board)
        with self.assertRaises(OutOfBoard) as exc:
            board.set_piece(10, 10, rook)
        self.assertEqual(
            exc.exception.message,
            "La posición está fuera de los límites del tablero"
        )

    def test_set_piece_out_of_range_row(self):
        board = Board(for_test=True)
        rook = Rook('BLACK', board)
        with self.assertRaises(RowOutOfBoard) as exc:
            board.set_piece(10, 0, rook)
        self.assertEqual(
            exc.exception.message,
            "La fila seleccionada está fuera del tablero"
        )
    
    def test_set_piece_out_of_range_col(self):
        board = Board(for_test=True)
        rook = Rook('BLACK', board)
        with self.assertRaises(ColumnOutOfBoard) as exc:
            board.set_piece(0, 10, rook)
        self.assertEqual(
            exc.exception.message,
            "La columna seleccionada está fuera del tablero"
        )

    def test_rooks_creation(self):
        board = Board()
        self.assertIsInstance(board.get_piece(0, 0), Rook)
        self.assertEqual(board.get_piece(0, 0).color, 'BLACK')
        self.assertIsInstance(board.get_piece(0, 7), Rook)
        self.assertEqual(board.get_piece(0, 7).color, 'BLACK')
        self.assertIsInstance(board.get_piece(7, 0), Rook)
        self.assertEqual(board.get_piece(7, 0).color, 'WHITE')
        self.assertIsInstance(board.get_piece(7, 7), Rook)
        self.assertEqual(board.get_piece(7, 7).color, 'WHITE')

    def test_pawns_creation(self):
        board = Board()
        for col in range(8):
            self.assertIsInstance(board.get_piece(1, col), Pawn)
            self.assertEqual(board.get_piece(1, col).color, 'BLACK')
            self.assertIsInstance(board.get_piece(6, col), Pawn)
            self.assertEqual(board.get_piece(6, col).color, 'WHITE')

    def test_empty_spaces(self):
        board = Board()
        for row in range(2, 6):
            for col in range(8):
                self.assertIsNone(board.get_piece(row, col))

    def test_move(self):
        board = Board(for_test=True)
        rook = Rook(color='BLACK', board=board)
        board.set_piece(0, 0, rook)
        board.move(0, 0, 0, 1)

        self.assertIsInstance(board.get_piece(0, 1), Rook)
        self.assertEqual(
            str(board),
            (
                " ♖      \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
            )
        )


if __name__ == '__main__':
    unittest.main()
