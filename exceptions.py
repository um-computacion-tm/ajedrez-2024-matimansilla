class InvalidMove(Exception):
    __message__ = "Movimiento inválido"
    
    def __str__(self):
        return self.__message__

class InvalidTurn(InvalidMove):
    __message__ = "No es tu turno"

class EmptyPosition(InvalidMove):
    __message__ = "No hay ninguna pieza en la posición de origen"

class OutOfBoard(InvalidMove):
    __message__ = "Movimiento fuera de tablero"

class OriginInvalidMove(InvalidMove):
    __message__ = "Sin piezas en posición origen"

class DestinationInvalidMove(InvalidMove):
    __message__ = "Movimiento destino inválido"

class SelfCaptureException(InvalidMove):
    __message__ = "No puedes capturar tus propias piezas."

class InvalidCoordinateInputError(InvalidMove):
    __message__ = "Las coordenadas deben ser números."

class RowOutOfBoard(InvalidMove):
    __message__ = "La fila está fuera del tablero."

class ColumnOutOfBoard(InvalidMove):
    __message__ = "La columna está fuera del tablero."
