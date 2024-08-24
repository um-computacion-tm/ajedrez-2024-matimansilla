from chess import Chess 

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    print("Inicio de play()")
    try:
        from_x = int(input("Enter from X: "))
        from_y = int(input("Enter from Y: "))
        to_x = int(input("Enter to X: "))
        to_y = int(input("Enter to Y: "))

        print(f"Moviendo de ({from_x}, {from_y}) a ({to_x}, {to_y})")

        result = chess.move(from_x, from_y, to_x, to_y)
        print("Resultado del movimiento:", result)

    except ValueError:
        print("Entrada no válida, por favor ingrese números enteros.")  # Manejo de errores

if __name__ == '__main__':
    main()
