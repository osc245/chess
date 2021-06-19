from .Piece import Piece

class Queen(Piece):
    def __init__(self, isWhite):
        Piece.__init__(self, isWhite, "Q", "q")

    def validMove(self, move, board):
        return self.checkClearLine(move, board)

