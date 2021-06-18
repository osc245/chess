from ChessProgram.Pieces.Piece import Piece


class Bishop(Piece):
    def __init__(self, isWhite):
        Piece.__init__(self, isWhite, "B", "b")

    @staticmethod
    def validMove(pos, board):
        if not (Piece.validCapture(pos, board) or Piece.validMove(pos, board)):
            return False
        return Piece.checkClearDiagonal(pos, board)


