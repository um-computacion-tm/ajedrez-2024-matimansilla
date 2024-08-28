class Piece:
    def __init__(self,color,board):
        self.__color__=color
        self.__board__=board
    def str(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else: return self.black_str
        
class Rook(Piece):
    white_str='♜'
    black_str='♖'

    def possible_positions_vd(self,row,col):
        possibles=[]
        for next_row in range(row+1,8):
            if self.board.get_piece[next_row][col] is None:
                possibles.append((next_row,col))
        return possibles

    def possible_positions_va(self,row,col):
        possibles=[]
        for next_row in range(row-1,-1,-1):
            possibles.append((next_row,col))
        return possibles
    
    #def valid_positions(self,from_row,from_col,to_row,to_col):
    #    possible_positions=(possible_positions_vd(from_row,from_col)+possible_positions_va(from_row,from_col))
    #   return (to_row,to_col) in possible_positions

class Pawn(Piece):
    def __init__(self,color,board):
        super().__init__(color,board)
    
    def __str__(self):
        if self.__color__=="WHITE":
            return "♟"
        else: return "♙"