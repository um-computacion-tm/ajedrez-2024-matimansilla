import unittest
from unittest.mock import patch
from chess import Chess
from cli import play

class TestCli(unittest.TestCase):
    @patch(
        'builtins.input',
        side_effect=['1', '1', '2', '2'],
    )
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 1)  # 1 mensaje 'Move made.'
        self.assertEqual(mock_chess_move.call_count, 1)

    @patch(
        'builtins.input',
        side_effect=['hola', '1', '2', '2'],
    )
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_not_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)  # 1 intento inválido seguido por 3 válidos
        self.assertEqual(mock_print.call_count, 2)  # 1 mensaje de error, 1 'Move made.'
        self.assertEqual(mock_chess_move.call_count, 1)

    @patch(
        'builtins.input',
        side_effect=['1', '1', '2', 'hola', '3'],
    )
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_more_not_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 5)  # 4 válidas y 1 inválida
        self.assertEqual(mock_print.call_count, 2)  # 1 mensaje de error, 1 'Move made.'
        self.assertEqual(mock_chess_move.call_count, 1)

if __name__ == '__main__':
    unittest.main()