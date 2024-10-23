import unittest
from unittest.mock import patch, MagicMock
from chess import Chess
from cli import ChessCli
from exceptions import InvalidMove

class TestChessCli(unittest.TestCase):

    # Prueba para verificar el símbolo del caballo
    @patch('builtins.print')  # Simular el print
    @patch.object(Chess, 'is_game_over', return_value=True)  # Simular que el juego termina
    def test_start_game_over(self, mock_is_game_over, mock_print):
        cli = ChessCli()  
        cli.start()  # Inicia el juego
        self.assertEqual(mock_print.call_count, 3)  # Verifica el número de impresiones al inicio y fin del juego

    # Prueba para mostrar el turno actual
    @patch('builtins.print')  # Simular el print
    @patch.object(Chess, 'get_turn', return_value="WHITE")  # Simular el turno del jugador
    def test_show_turn(self, mock_get_turn, mock_print):
        cli = ChessCli()
        cli.show_board()
        mock_print.assert_called_with(cli.__game__.__board__)  # Verifica que se muestra el tablero correctamente

    # Prueba para procesar el movimiento del jugador
    @patch('chess.cli.Chess')
    def test_process_player_move(self, MockChess):
        mock_game = MockChess.return_value
        mock_game.make_move = MagicMock()

        cli = ChessCli()
        cli.__game__ = mock_game  # Asignar el mock al juego

        # Simular la entrada del usuario
        with patch('builtins.input', side_effect=["6,4", "5,4"]):
            cli.process_player_move()

        # Verificar que make_move fue llamado con los parámetros correctos
        mock_game.make_move.assert_called_once_with(6, 4, 5, 4)

    # Prueba para manejar excepciones de movimiento inválido
    @patch('chess.cli.Chess')
    def test_process_player_move_exception(self, MockChess):
        mock_game = MockChess.return_value
        mock_game.make_move.side_effect = InvalidMove()

        cli = ChessCli()
        cli.__game__ = mock_game  # Asignar el mock al juego

        with patch('builtins.input', side_effect=["6,4", "5,4"]), \
             patch('builtins.print') as mock_print:
            cli.process_player_move()

        # Verificar que se imprime el mensaje de error correcto
        mock_print.assert_called_with("Error: Movimiento inválido")

    # Prueba para procesar opciones del juego y salir
    @patch('chess.cli.Chess')
    def test_process_game_options_exit(self, MockChess):
        cli = ChessCli()
        cli.__game__ = MockChess.return_value  # Asignar el mock al juego

        with patch('builtins.print') as mock_print, \
             patch('chess.cli.ChessCli.offer_options', return_value='exit'):
            with self.assertRaises(SystemExit):  # Verificar que se lanza SystemExit
                cli.process_game_options()

        # Verificar que se imprime el mensaje de salida correcto
        mock_print.assert_called_with("Has salido del juego.")

    # Prueba para procesar opciones del juego y ofrecer empate
    @patch('chess.cli.Chess')
    def test_process_game_options_draw(self, MockChess):
        cli = ChessCli()
        cli.__game__ = MockChess.return_value  # Asignar el mock al juego

        with patch('builtins.print') as mock_print, \
             patch('chess.cli.ChessCli.offer_options', return_value='draw'):
            cli.process_game_options()

        # Verificar que se imprime el mensaje de empate correcto
        mock_print.assert_called_with("Se ha ofrecido un empate.")

    # Pruebas para la función de movimiento de piezas
    @patch('builtins.input', side_effect=['1', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        cli = ChessCli()  # Inicializa el CLI para la interacción
        cli.__game__ = chess  # Asigna el juego al CLI
        cli.process_player_move()  # Llama a la función que procesa el movimiento
        self.assertEqual(mock_input.call_count, 4)  # Verifica que se pidieron 4 entradas
        self.assertEqual(mock_print.call_count, 2)  # Verifica el número de impresiones
        self.assertEqual(mock_chess_move.call_count, 1)  # Verifica que se llamó al movimiento

    @patch('builtins.input', side_effect=['hola', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_wrong_entry_1(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        cli = ChessCli()
        cli.__game__ = chess
        cli.process_player_move()
        self.assertEqual(mock_input.call_count, 1)  # Verifica que se pidieron 1 entrada antes de la excepción
        self.assertEqual(mock_print.call_count, 3)  # Verifica el número de impresiones
        self.assertEqual(mock_chess_move.call_count, 0)  # Verifica que no se llamó al movimiento

    @patch('builtins.input', side_effect=['1', 'hola', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_wrong_entry_2(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        cli = ChessCli()
        cli.__game__ = chess
        cli.process_player_move()
        self.assertEqual(mock_input.call_count, 2)  # Verifica que se pidieron 2 entradas
        self.assertEqual(mock_print.call_count, 3)  # Verifica el número de impresiones
        self.assertEqual(mock_chess_move.call_count, 0)  # Verifica que no se llamó al movimiento

    @patch('builtins.input', side_effect=['1', '1', 'hola', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_wrong_entry_3(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        cli = ChessCli()
        cli.__game__ = chess
        cli.process_player_move()
        self.assertEqual(mock_input.call_count, 3)  # Verifica que se pidieron 3 entradas
        self.assertEqual(mock_print.call_count, 3)  # Verifica el número de impresiones
        self.assertEqual(mock_chess_move.call_count, 0)  # Verifica que no se llamó al movimiento

    @patch('builtins.input', side_effect=['1', '1', '2', 'hola'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_wrong_entry_4(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        cli = ChessCli()
        cli.__game__ = chess
        cli.process_player_move()
        self.assertEqual(mock_input.call_count, 4)  # Verifica que se pidieron 4 entradas
        self.assertEqual(mock_print.call_count, 3)  # Verifica el número de impresiones
        self.assertEqual(mock_chess_move.call_count, 0)  # Verifica que no se llamó al movimiento

    @patch('builtins.input', side_effect=['1', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move', side_effect=InvalidMove())
    def test_invalid_move(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        cli = ChessCli()
        cli.__game__ = chess
        cli.process_player_move()
        self.assertEqual(mock_input.call_count, 4)  # Verifica que se pidieron 4 entradas
        self.assertEqual(mock_print.call_count, 3)  # Verifica el número de impresiones
        self.assertEqual(mock_chess_move.call_count, 1)  # Verifica que se llamó al movimiento

if __name__ == "__main__":
    unittest.main()
