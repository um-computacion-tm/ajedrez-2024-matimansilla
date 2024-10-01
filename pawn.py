from pieces import Piece

class Pawn(Piece):
    white_str='♟'
    black_str='♙'

    # POSSIBLE POSITIONS TO MOVE PAWN INCLUDIONG MOVE AND EAT
    
    def valid_positions(self,from_row,from_col):
        possible_positions=self.possible_positions_move(from_row, from_col)+self.possible_positions_eat(from_row, from_col)
        return possible_positions
   
    # PAWN EATING A PIECE

    def possible_positions_eat(self, from_row, from_col):
        possible=[]
        if self.__color__ == "BLACK":
            other_piece_right = self.__board__.get_piece(from_row + 1, from_col + 1)
            other_piece_left = self.__board__.get_piece(from_row + 1, from_col - 1)
            if other_piece_right is not None and other_piece_right.__color__ == "WHITE":
                possible.append((from_row+1,from_col+1))
            if other_piece_left is not None and other_piece_left.__color__=='WHITE':
                possible.append((from_row+1,from_col-1))
        elif self.__color__=='WHITE':
            other_piece_right = self.__board__.get_piece(from_row - 1, from_col + 1)
            other_piece_left = self.__board__.get_piece(from_row - 1, from_col - 1)
            if other_piece_right is not None and other_piece_right.__color__ == "BLACK":
                possible.append((from_row-1,from_col+1))
            if other_piece_left is not None and other_piece_left.__color__=='BLACK':
                possible.append((from_row-1,from_col-1))
        return possible
    

    # MOVING A PAWN RULES

    def possible_positions_move(self, from_row, from_col):
        if self.__color__ == "BLACK":
            if self.__board__.get_piece(from_row + 1, from_col) is None:
                if from_row == 1 and self.__board__.get_piece(from_row + 2, from_col) is None:
                    return [(from_row + 1, from_col),(from_row + 2, from_col)]
                else: return [(from_row + 1, from_col)]
            else: return []
        else:
            if self.__board__.get_piece(from_row-1,from_col) is None:
                if from_row==6 and self.__board__.get_piece(from_row-2,from_col) is None:
                    return [(from_row-1,from_col),(from_row-2,from_col)]
                else: return [(from_row-1,from_col)]
            else: return []