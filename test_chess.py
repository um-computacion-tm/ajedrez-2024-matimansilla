import unittest
from chess import Chess
from exceptions import *
from board import Board
from unittest.mock import MagicMock, patch

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()  # Inicializa un nuevo juego de ajedrez
        self.chess.__turn__ = "WHITE"  # Establece el turno en blanco
        self.chess.__board__ = MagicMock()  # Simula el tablero

        self.piece = MagicMock()

    def test_is_game_over(self):
        self.chess.__board__.count_pieces.return_value = 0  # Simula que no quedan piezas de uno de los jugadores
        self.assertTrue(self.chess.is_game_over())  # Verifica que el juego esté terminado

        self.chess.__board__.count_pieces.return_value = 1  # Simula que aún quedan piezas
        self.assertFalse(self.chess.is_game_over())  # Verifica que el juego no esté terminado

    def test_make_move_valid(self):
        self.chess.__board__.get_piece.return_value = self.piece  # Simula una pieza en el tablero
        self.piece.get_color.return_value = "WHITE"  # Simula que la pieza es blanca
        self.piece.valid_positions.return_value = True  # Simula un movimiento válido

        self.chess.make_move(4, 4, 5, 4)  # Movimiento válido
        self.chess.__board__.move.assert_called_once_with(4, 4, 5, 4)  # Verifica que se llamó al método de movimiento del tablero
        self.assertEqual(self.chess.get_turn(), "BLACK")  # Verifica que el turno cambió a negro

    def test_make_move_empty_position(self):
        # Configura el mock para que devuelva None al intentar obtener la pieza de la posición (0, 0)
        self.chess.__board__.get_piece.return_value = None
        
        # Intentar mover desde una posición vacía (0, 0)
        with self.assertRaises(EmptyPosition) as context:
            self.chess.make_move(0, 0, 1, 0)  # Desde una posición vacía hacia (1, 0)
        self.assertEqual(str(context.exception), "No hay ninguna pieza en la posición de origen")  # Verifica el mensaje de la excepción

    def test_make_move_invalid_turn(self):
        # Configura el mock para simular que la pieza es negra
        self.chess.__board__.get_piece.return_value = self.piece
        self.piece.get_color.return_value = "BLACK"  # Simula que la pieza es negra
        
        # Intentar mover una pieza que no es del turno actual
        with self.assertRaises(InvalidTurn) as context:
            self.chess.make_move(4, 4, 5, 4)  # Movimiento válido, pero de una pieza negra
        self.assertEqual(str(context.exception), "No es tu turno")  # Verifica el mensaje de la excepción

    def test_make_move_invalid_destination(self):
        # Configura el mock para que devuelva una pieza blanca y que el movimiento no sea válido
        self.chess.__board__.get_piece.return_value = self.piece
        self.piece.get_color.return_value = "WHITE"  # Simula que la pieza es blanca
        self.piece.valid_positions.return_value = False  # Simula un movimiento inválido
        
        # Intentar hacer un movimiento inválido
        with self.assertRaises(DestinationInvalidMove) as context:
            self.chess.make_move(4, 4, 5, 4)  # Movimiento inválido
        self.assertEqual(str(context.exception), "Movimiento destino inválido")  # Verifica el mensaje de la excepción


if __name__ == '__main__':
    unittest.main()