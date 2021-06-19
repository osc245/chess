from .Piece import Piece
from .Rook import Rook
from ..Move import Move


class King(Piece):
    def __init__(self, isWhite):
        Piece.__init__(self, isWhite, "K", "k")
        self.moved = False

    def validMove(self, move, board):
        dy, dx = self.getDiff(move)

        # moving normally
        if abs(dx) <= 1 and abs(dy) <= 1:
            self.moved = True
            return True

        # castling
        if not self.moved and abs(dx) == 2 and dy == 0:
            rookRow = 0 if self.isWhite else 7
            rookCol = 0 if dx == -2 else 7
            if not isinstance(board[rookRow][rookCol], Rook) or board[rookRow][rookCol].moved:
                return False
            rookMove = Move(move.oldRow, move.oldCol, rookRow, rookCol)
            if self.checkClearLine(rookMove, board):
                return True
        return False
