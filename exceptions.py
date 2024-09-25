class InvalidMove(Exception):
    message = "Movimiento inválido en el tablero"
    def __str__(self):
        return self.message


class InvalidTurn(InvalidMove):
    message = "No es tu turno para mover esa pieza"


class EmptyPosition(InvalidMove):
    message = "No hay pieza en la posición seleccionada"


class InvalidMoveRookMove(InvalidMove):
    message = "Movimiento ilegal para la torre en esa dirección"


class OutOfBoard(InvalidMove):
    message = "La posición indicada se encuentra fuera del tablero"


class RowOutOfBoard(OutOfBoard):
    message = "La Fila indicada se encuentra fuera del tablero"


class ColumnOutOfBoard(OutOfBoard):
    message = "La Columna indicada se encuentra fuera del tablero"
