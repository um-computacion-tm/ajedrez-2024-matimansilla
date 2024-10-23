import unittest
from unittest.mock import patch, MagicMock
from chess import Chess
from board import Board
from king import King
from queen import Queen
from exceptions import InvalidMove
from cli import ChessCli

class TestChessCli(unittest.TestCase):

    @patch('builtins.print')
    @patch.object(Chess, 'is_game_over', return_value=True)
    def test_start_game_over(self, mock_is_game_over, mock_print):
        cli = ChessCli()  
        cli.start()
        self.assertEqual(mock_print.call_count, 3)

    @patch('builtins.print')
    @patch.object(Chess, 'get_turn', return_value="WHITE")
    def test_show_turn(self, mock_get_turn, mock_print):
        cli = ChessCli()
        cli.__game__ = MagicMock()  # Simula el juego
        cli.__game__.__board__ = MagicMock()  # Simula el tablero del juego
        cli.show_board()
        mock_print.assert_called_with(cli.__game__.__board__)

    @patch('chess.Chess')
    def test_process_player_move(self, MockChess):
        mock_game = MockChess.return_value
        mock_game.make_move = MagicMock()

        cli = ChessCli()
        cli.__game__ = mock_game  

        with patch('builtins.input', side_effect=["6,4", "5,4"]):
            cli.process_player_move()

        mock_game.make_move.assert_called_once_with(6, 4, 5, 4)

    @patch('chess.Chess')
    def test_process_player_move_exception(self, MockChess):
        mock_game = MockChess.return_value
        mock_game.make_move.side_effect = InvalidMove()

        cli = ChessCli()
        cli.__game__ = mock_game  

        with patch('builtins.input', side_effect=["6,4", "5,4"]), \
             patch('builtins.print') as mock_print:  
            cli.process_player_move()

        mock_print.assert_called_with("Error: Movimiento inválido")

    @patch('chess.Chess')
    def test_process_game_options_exit(self, MockChess):
        cli = ChessCli()
        cli.__game__ = MockChess.return_value  

        with patch('builtins.print') as mock_print, \
             patch('cli.ChessCli.offer_options', return_value='exit'):  # Cambia a 'cli'
            with self.assertRaises(SystemExit):  
                cli.process_game_options()

        mock_print.assert_called_with("Has salido del juego.")

    @patch('chess.Chess')
    def test_process_game_options_draw(self, MockChess):
        cli = ChessCli()
        cli.__game__ = MockChess.return_value  

        with patch('builtins.print') as mock_print, \
             patch('cli.ChessCli.offer_options', return_value='draw'):  # Cambia a 'cli'
            cli.process_game_options()

        mock_print.assert_called_with("Se ha ofrecido un empate.")

if __name__ == "__main__":
    unittest.main()
