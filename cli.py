from chess import Chess

def main():
    chess = Chess()
    print("Welcome to Chess!")
    print("Enter your moves by specifying row and column numbers.")
    print("Type 'q' at any prompt to quit the game.\n")

    while True:
        if not play(chess):
            break
    print("Thank you for playing!")

def play(chess):
    try:
        from_row = get_input("From row: ")
        from_col = get_input("From col: ")
        to_row = get_input("To row: ")
        to_col = get_input("To col: ")

        if from_row is None or from_col is None or to_row is None or to_col is None:
            return  # Sale de la función si hay una entrada inválida

        chess.move(from_row, from_col, to_row, to_col)
        print("Move made.")
    
    except Exception as e:
        print("Error:", e)


    return True  # Continue the loop

def get_input(prompt):
    user_input = input(prompt)
    if user_input.lower() == 'q':
        return None
    try:
        return int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")
        return get_input(prompt)

if __name__ == '__main__':
    main()

    