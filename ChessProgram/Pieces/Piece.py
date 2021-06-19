class Piece:
    def __init__(self, isWhite, upperChar, lowerChar):
        self.isWhite = isWhite
        self.displayChar = upperChar if isWhite else lowerChar

    def toString(self):
        return self.displayChar

    # checks that there are no pieces in between the piece's old and new positions
    # it also checks that the piece is moving horizontally, vertically or diagonally
    def checkClearLine(self, move, board):
        dy, dx = self.getDiff(move)

        # vertical movement
        if dx == 0:
            direction = 1 if move.oldRow < move.newRow else -1
            for i in range(1, abs(dy)):
                if board[move.oldRow + i * direction][move.oldCol] is not None:
                    return False
            return True

        # horizontal movement
        if dy == 0:
            direction = 1 if move.oldCol < move.newCol else -1
            for i in range(1, abs(dx)):
                if board[move.oldRow][move.oldCol + i * direction] is not None:
                    return False
            return True

        # diagonal movement
        if abs(dx) == abs(dy):
            yDir = 1 if move.oldRow < move.newRow else -1
            xDir = 1 if move.oldCol < move.newCol else -1
            for i in range(1, abs(dx)):
                if board[move.oldRow + i * yDir][move.oldCol + i * xDir] is not None:
                    return False
            return True
        return False

    # returns the change in rows and columns from a move
    @staticmethod
    def getDiff(move):
        return move.newRow - move.oldRow, move.newCol - move.oldCol
