from .Piece import Piece


class Bishop(Piece):
    def __init__(self, isWhite):
        Piece.__init__(self, isWhite, "B", "b")

    def validMove(self, move, board):
        return self.checkClearLine(move, board)
