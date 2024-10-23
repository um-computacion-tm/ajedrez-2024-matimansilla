class InvalidMove(Exception):
    message = "Movimiento inválido"
    
    def __str__(self):
        return self.message


class InvalidTurn(InvalidMove):
    message = "No puedes mover pieza de otro jugador"


class EmptyPosition(InvalidMove):
    message = "La posición está vacía"


class OutOfBoard(InvalidMove):
    message = "La posición indicada se encuentra fuera del tablero"


class OriginInvalidMove(InvalidMove):
    message = "Sin piezas en posición de origen"


class DestinationInvalidMove(InvalidMove):
    message = "Movimiento destino inválido"


class SelfCaptureException(InvalidMove):
    message = "No puedes capturar tus propias piezas."


class InvalidCoordinateInputError(InvalidMove):
    message = "Las coordenadas deben ser números."


class InvalidMoveNoPiece(InvalidMove):
    message = "No hay pieza en la posición indicada."


class InvalidMoveRookMove(InvalidMove):
    message = "Movimiento de la torre inválido."


class RowOutOfBoard(OutOfBoard):
    message = "La fila indicada se encuentra fuera del tablero."


class ColumnOutOfBoard(OutOfBoard):
    message = "La columna indicada se encuentra fuera del tablero."
