from .Piece import Piece

class Knight(Piece):
    def __init__(self, isWhite):
        Piece.__init__(self, isWhite, "N", "n")
        self.moved = False

    def validMove(self, move, board):
        dy, dx = self.getDiff(move)
        return (abs(dy) == 1 and abs(dx) == 2) or (abs(dy) == 2 and abs(dx) == 1)
