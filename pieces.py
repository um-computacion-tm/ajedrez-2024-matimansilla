class Piece: 
    def __init__ (self, color):
        self.__color__ = color 
class Rook(Piece):
    def __init__(self, color):
        self.color = color  # Atributo público

    def __str__(self):
        return "R" if self.color == "WHITE" else "r"

    ...
class Pawn(Piece):
    ...

       
