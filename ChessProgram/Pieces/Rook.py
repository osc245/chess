from .Piece import Piece

class Rook(Piece):
    def __init__(self, isWhite):
        Piece.__init__(self, isWhite, "R", "r")
        self.moved = False

    def validMove(self, move, board):
        if self.checkClearLine(move, board):
            self.moved = True
            return True
        return False
