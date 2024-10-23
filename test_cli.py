import unittest
from unittest.mock import patch, MagicMock
from chess import Chess
from board import Board
from king import King
from queen import Queen
from chess import Chess
from exceptions import *
from cli import ChessCli

class TestChessCli(unittest.TestCase):

    @patch('builtins.print')  # Simular el print
    @patch.object(Chess, 'is_game_over', return_value=True)  # Simular que el juego termina
    def test_start_game_over(self, mock_is_game_over, mock_print):
        cli = ChessCli()  
        cli.start()  # Inicia el juego
        self.assertEqual(mock_print.call_count, 3)  # Se imprime el mensaje de inicio y fin de juego


    @patch('builtins.print')  # Simular el print
    @patch.object(Chess, 'get_turn', return_value="WHITE")  # Simular el turno del jugador
    def test_show_turn(self, mock_get_turn, mock_print):
        cli = ChessCli()
        cli.show_board()
        mock_print.assert_called_with(cli.__game__.__board__)  # Verificar que se muestra el tablero


    @patch('chess.cli.Chess')
    def test_process_player_move(self, MockChess):
        # Configurar el juego simulado
        mock_game = MockChess.return_value
        mock_game.make_move = MagicMock()

        # Crear una instancia de ChessCli
        cli = ChessCli()
        cli.__game__ = mock_game  # Asignar el mock al juego

        # Simular la entrada del usuario
        with patch('builtins.input', side_effect=["6,4", "5,4"]):
            cli.process_player_move()

        # Verificar que make_move fue llamado con los parámetros correctos
        mock_game.make_move.assert_called_once_with(6, 4, 5, 4)


    @patch('chess.cli.Chess')
    def test_process_player_move_exception(self, MockChess):
        # Crear una instancia simulada del juego
        mock_game = MockChess.return_value
        # Simular que se lanza una InvalidMove al intentar hacer un movimiento
        mock_game.make_move.side_effect = InvalidMove()

        cli = ChessCli()
        cli.__game__ = mock_game  # Asignar el mock al juego

        with patch('builtins.input', side_effect=["6,4", "5,4"]), \
             patch('builtins.print') as mock_print:  # Mock para capturar la salida de print
            cli.process_player_move()

        # Verificar que se imprime el mensaje de error correcto
        mock_print.assert_called_with("Error: Movimiento inválido")


    @patch('chess.cli.Chess')
    def test_process_game_options_exit(self, MockChess):
        cli = ChessCli()
        cli.__game__ = MockChess.return_value  # Asignar el mock al juego

        with patch('builtins.print') as mock_print, \
             patch('chess.cli.ChessCli.offer_options', return_value='exit'):  # Mock para ofrecer opciones
            with self.assertRaises(SystemExit):  # Verificar que se lanza SystemExit
                cli.process_game_options()

        # Verificar que se imprime el mensaje de salida correcto
        mock_print.assert_called_with("Has salido del juego.")

    @patch('chess.cli.Chess')
    def test_process_game_options_draw(self, MockChess):
        cli = ChessCli()
        cli.__game__ = MockChess.return_value  # Asignar el mock al juego

        with patch('builtins.print') as mock_print, \
             patch('chess.cli.ChessCli.offer_options', return_value='draw'):  # Mock para ofrecer empate
            cli.process_game_options()

        # Verificar que se imprime el mensaje de empate correcto
        mock_print.assert_called_with("Se ha ofrecido un empate.")
        

if __name__ == "__main__":
    unittest.main()