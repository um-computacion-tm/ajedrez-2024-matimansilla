from chess import Chess
from exceptions import *

class ChessCli:

    def __init__(self):
        self.__game__ = Chess()

    def start(self):
        print("¡Bienvenido al juego de Ajedrez!")
        while not self.__game__.is_game_over():
            self.show_board()
            print(f"Turno del jugador {self.__game__.get_turn()}")
            self.process_player_move()
            self.process_game_options()  
        self.end_game()

    def process_player_move(self):
        move = self.get_move()
        if move:
            from_row, from_col, to_row, to_col = move
            try:
                self.__game__.make_move(from_row, from_col, to_row, to_col)
            except Exception as e:
                print(f"Error: {e}")

    def process_game_options(self):
        option = self.offer_options()
        if option == 'exit':
            print("Has salido del juego.")
            raise SystemExit
        elif option == 'draw':
            print("Se ha ofrecido un empate.")

    def show_board(self):
        print(self.__game__.__board__)

    def get_move(self):
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
                print("El empate ha sido rechazido.")
        return None 

    def end_game(self):
        print("¡El juego ha terminado!")
        winner = "BLANCAS" if self.__game__.get_turn() == "BLACK" else "NEGRAS"
        print(f"El ganador es: {winner}")

if __name__ == "__main__":
    cli = ChessCli()
    cli.start()
