from pieces import Piece

class Rook:
    def __init__(self, color):
        self.color = color  # Atributo público

    def __str__(self):
        return "R" if self.color == "WHITE" else "r"
