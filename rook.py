from pieces import Piece

class Rook(Piece):
    white_str = "♜"
    black_str = "♖"

    def possible_positions_vd(self, row, col):
        possibles = []
        # Mover hacia abajo (vertical descendente)
        for next_row in range(row + 1, 8):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))  # Captura
                break  # Bloqueo
            possibles.append((next_row, col))
        return possibles
    
    def possible_positions_va(self, row, col):
        possibles = []
        # Mover hacia arriba (vertical ascendente)
        for next_row in range(row - 1, -1, -1):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))  # Captura
                break  # Bloqueo
            possibles.append((next_row, col))
        return possibles

    def possible_positions_hr(self, row, col):
        possibles = []
        # Mover hacia la derecha (horizontal)
        for next_col in range(col + 1, 8):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row, next_col))  # Captura
                break  # Bloqueo
            possibles.append((row, next_col))
        return possibles
    
    def possible_positions_hl(self, row, col):
        possibles = []
        # Mover hacia la izquierda (horizontal)
        for next_col in range(col - 1, -1, -1):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row, next_col))  # Captura
                break  # Bloqueo
            possibles.append((row, next_col))
        return possibles

    def valid_positions(self, from_row, from_col, to_row, to_col):
        # Unir todas las posiciones posibles (verticales y horizontales)
        possible_positions = (
            self.possible_positions_vd(from_row, from_col)
            + self.possible_positions_va(from_row, from_col)
            + self.possible_positions_hr(from_row, from_col)
            + self.possible_positions_hl(from_row, from_col)
        )
        return (to_row, to_col) in possible_positions
