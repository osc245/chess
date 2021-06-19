from .Piece import Piece

class Pawn(Piece):
    # enPassant field indicates whether the opponent can en passant capture it
    def __init__(self, isWhite):
        Piece.__init__(self, isWhite, "P", "p")
        self.enPassant = False

    def validMove(self, move, board):
        dy, dx = self.getDiff(move)

        # check if pawn is promoting it is moving to the last rank
        if move.promotion and not ((self.isWhite and move.newRow == 7) or (not self.isWhite and move.newRow == 0)):
            return False

        # moving
        if dx == 0:
            # square immediately in front of pawn is free
            if board[move.oldRow + dy // abs(dy)][move.oldCol] is not None:
                return False

            # moving one square
            if (self.isWhite and dy == 1) or (not self.isWhite and dy == -1):
                self.enPassant = False
                return True

            # moving two squares
            if (self.isWhite and dy == 2 and move.oldRow == 1) or (not self.isWhite and dy == -2 and move.oldRow == 6):
                if board[move.oldRow + dy][move.oldCol] is None:  # square two squares in front of pawn is free
                    self.enPassant = True
                    return True

        # capturing
        if abs(dx) == 1:
            if (self.isWhite and dy == 1) or (not self.isWhite and dy == -1):
                # capturing normally
                if board[move.newRow][move.newCol] is not None:
                    self.enPassant = False
                    return True

                # capturing en passant
                if (self.isWhite and dy == 1) or (not self.isWhite and dy == -1):
                    capturedPiece = board[move.oldRow][move.newCol]
                    if isinstance(capturedPiece, Pawn) and capturedPiece.enPassant \
                            and capturedPiece.isWhite != board[move.oldRow][move.oldCol].isWhite:
                        return True
        return False
