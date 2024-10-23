import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chess import Chess
from exceptions import InvalidMove, InvalidTurn, EmptyPosition, OutOfBoard, OriginInvalidMove

def main():
    """
    Función principal que inicia el juego de ajedrez.
    """
    chess_cli = ChessCli()
    chess_cli.start()

class ChessCli:
    """
    Clase que gestiona la interfaz de línea de comandos del juego de ajedrez.
    """

    def __init__(self):
        """
        Inicializa la interfaz de línea de comandos creando una instancia de la clase Chess.
        """
        self.__game__ = Chess()

    def start(self):
        """
        Inicia el juego de ajedrez. 
        Muestra el tablero y permite que los jugadores alternen turnos hasta que se declare un ganador o se termine el juego.
        """
        print("¡Bienvenido al juego de Ajedrez!")
        while not self.__game__.is_game_over():
            self.show_board()
            print(f"Turno del jugador {self.__game__.get_turn()}")
            self.process_player_move()
            self.process_game_options()

        self.end_game()

    def process_player_move(self):
        """
        Procesa el movimiento del jugador. 
        Solicita las coordenadas de origen y destino, e intenta hacer el movimiento en el tablero.
        """
        move = self.get_move()
        if move:
            from_row, from_col, to_row, to_col = move
            try:
                self.__game__.make_move(from_row, from_col, to_row, to_col)
            except InvalidMove as e:
                print(f"Movimiento inválido: {e}")
            except (OutOfBoard, OriginInvalidMove) as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")

    def process_game_options(self):
        """
        Procesa las opciones adicionales del juego, como salir o ofrecer un empate.
        """
        option = self.offer_options()
        if option == 'exit':
            print("Has salido del juego.")
            raise SystemExit
        elif option == 'draw':
            print("Se ha ofrecido un empate.")

    def show_board(self):
        """
        Muestra el estado actual del tablero de ajedrez.
        """
        print(self.__game__.show_board())

    def get_move(self):
        """
        Solicita al jugador que ingrese las coordenadas de origen y destino en formato fila,columna.
        Devuelve una tupla con las coordenadas si son válidas.
        """
        try:
            from_pos = input("Ingrese la posición de origen (fila,columna): ")
            to_pos = input("Ingrese la posición de destino (fila,columna): ")
            from_row, from_col = map(int, from_pos.split(","))
            to_row, to_col = map(int, to_pos.split(","))
            return from_row, from_col, to_row, to_col
        except ValueError:
            print("Entrada inválida. Por favor ingrese en formato fila,columna.")
            return self.get_move()

    def offer_options(self):
        """
        Ofrece opciones adicionales al jugador como salir o ofrecer un empate.
        """
        print()  
        exit_option = input("Ingrese 'exit' para salir del juego: ")
        if exit_option.lower() == 'exit':
            return 'exit' 

        draw_option = input("¿Ofrecer empate? (y/n): ")
        if draw_option.lower() == 'y':
            accept_draw = input("El otro jugador ofrece un empate. ¿Aceptar? (y/n): ")
            if accept_draw.lower() == 'y':
                print("El empate ha sido aceptado.")
                return 'draw' 
            else:
                print("El empate ha sido rechazado.")
        
        return None

    def end_game(self):
        """
        Finaliza el juego, mostrando el ganador.
        """
        print("¡El juego ha terminado!")
        winner = "BLANCAS" if self.__game__.get_turn() == "BLACK" else "NEGRAS"
        print(f"El ganador es: {winner}")


if __name__ == '__main__':
    main()
