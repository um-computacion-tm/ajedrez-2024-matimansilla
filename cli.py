from chess import Chess 

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))
    
        chess.move(from_row, from_col, to_row, to_col)
        print("Move successful")  # Agregado para el caso feliz
    
    except ValueError:
        print("Invalid input. Please enter a valid move.")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
