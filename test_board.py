import unittest
from board import Board
from pieces import Rook, Pawn

class TestBoard(unittest.TestCase):

    def test_board_initialization(self):
        board = Board()

        # Verificar que las torres estén en las posiciones correctas
        self.assertIsInstance(board.get_piece(0, 0), Rook)
        self.assertEqual(board.get_piece(0, 0).color, 'BLACK')
        self.assertIsInstance(board.get_piece(0, 7), Rook)
        self.assertEqual(board.get_piece(0, 7).color, 'BLACK')
        self.assertIsInstance(board.get_piece(7, 0), Rook)
        self.assertEqual(board.get_piece(7, 0).color, 'WHITE')
        self.assertIsInstance(board.get_piece(7, 7), Rook)
        self.assertEqual(board.get_piece(7, 7).color, 'WHITE')

        # Verificar que los peones estén en las posiciones correctas
        for col in range(8):
            self.assertIsInstance(board.get_piece(6, col), Pawn)
            self.assertEqual(board.get_piece(6, col).color, 'WHITE')
            self.assertIsInstance(board.get_piece(1, col), Pawn)
            self.assertEqual(board.get_piece(1, col).color, 'BLACK')

        # Verificar que las posiciones vacías sean realmente None
        for row in range(8):
            for col in range(8):
                if row in (0, 7) and col in (0, 7):
                    continue  # Las posiciones con torres
                if row == 6 or row == 1:
                    continue  # Las posiciones con peones
                self.assertIsNone(board.get_piece(row, col))

    def test_str_representation(self):
        board = Board()
        board_str = str(board)
        # Definir la representación esperada del tablero
        expected_board_str = (
            "♜        ♜\n"
            "♟♟♟♟♟♟♟♟\n"
            "        \n"
            "        \n"
            "        \n"
            "        \n"
            "♙♙♙♙♙♙♙♙\n"
            "♖        ♖\n"
        )
        self.assertEqual(board_str.strip(), expected_board_str.strip())
    
    def test_str_representation(self):
        board = Board()
        board_str = str(board)
        print("Generated board string:")
        print(board_str)
    
        expected_board_str = (
            "♜        ♜\n"
            "♟♟♟♟♟♟♟♟\n"
            "        \n"
            "        \n"
            "        \n"
            "        \n"
            "♙♙♙♙♙♙♙♙\n"
            "♖        ♖\n"
        )



if __name__ == '__main__':
    unittest.main()
