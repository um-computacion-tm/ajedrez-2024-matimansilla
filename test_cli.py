import unittest
from unittest.mock import patch, call
from chess import Chess
from cli import play

class TestCli(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        
        # Verificación de la cantidad de llamadas
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 1)  # Solo un mensaje de éxito
        self.assertEqual(mock_chess_move.call_count, 1)
        
        # Verificación de argumentos pasados a Chess.move
        self.assertEqual(mock_chess_move.call_args[0], (1, 1, 2, 2))
        
        # Verificación de mensajes impresos
        self.assertIn(call("Move successful"), mock_print.mock_calls)

    @patch('builtins.input', side_effect=['hola', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_not_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        
        # Verificación de la cantidad de llamadas
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_print.call_count, 1)  # Solo un mensaje de error
        self.assertEqual(mock_chess_move.call_count, 0)
        
        # Verificación de mensajes impresos
        self.assertIn(call("Invalid input. Please enter a valid move."), mock_print.mock_calls)

    @patch('builtins.input', side_effect=['1', '1', '2', 'hola'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_more_not_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        
        # Verificación de la cantidad de llamadas
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 1)  # Solo un mensaje de error final
        self.assertEqual(mock_chess_move.call_count, 0)
        
        # Verificación de mensajes impresos
        self.assertIn(call("Invalid input. Please enter a valid move."), mock_print.mock_calls)

if __name__ == '__main__':
    unittest.main()
