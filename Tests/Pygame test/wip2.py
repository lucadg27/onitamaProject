import pygame

class Chess():

    def __init__(self):
        pass

    def promotion(self):
        pass

    def move(self):
        pass



class Board():

    def __init__(self):
        pass

    def print_board(self):
        pass



class Piece():

    def __init__(self):
        pass

    def is_valid_move(self):
        pass

    def is_white(self):
        pass

    def __str__(self):
        pass

        
class Rook(Piece):
    def __init__(self, color):
        super().__init__()
        pass

        def is_valid_move(self, board, start, to):
            pass

class Knight(Piece):
    def __init__(self):
        super().__init__()
        pass

    def is_valid_move(self):
        pass

class Bishop(Piece):
    def __init__(self):
        super().__init__()
        pass

    def is_valid_move(self):
        pass

class Queen(Piece):
    def __init__(self):
        super().__init__()
        pass

    def is_valid_move(self):
        pass

class King(Piece):
    def __init__(self):
        super().__init__()
        pass

    def is_valid_move(self):
        pass

    # I added an extra method for the King class
    def can_castle(self):
        pass

# Class to represent a pseudo pawn that can be taken when
# en passant is possible
class GhostPawn(Piece):
    def __init__(self, color):
        super().__init__()
        pass

    def is_valid_move(self):
        return False

class Pawn(Piece):
    def __init__(self):
        super().__init__()
        pass

    def is_valid_move(self):
        pass
