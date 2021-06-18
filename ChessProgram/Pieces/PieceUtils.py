# there is a piece of opposite colour on capturing square
@staticmethod
def validCapture(pos, board):
    opPiece = board[pos[2]][pos[3]]
    return opPiece is not None and opPiece.isWhite != board[pos[0]][pos[1]].isWhite

# no piece on the square about to be moved to
@staticmethod
def validMove(pos, board):
    return board[pos[2]][pos[3]] is None

@staticmethod
def checkClearLine(pos, board):
    dy, dx = Piece.getDiff(pos)
    if dx == 0:
        direction = 1 if pos[0] < pos[2] else -1
        for i in range(1, abs(dy)):
            if board[pos[0] + i * direction][pos[1]] is not None:
                return False
        return True
    if dy == 0:
        direction = 1 if pos[1] < pos[3] else -1
        for i in range(1, abs(dx)):
            if board[pos[0]][pos[1] + i * direction] is not None:
                return False
        return True
    return False

@staticmethod
def checkClearDiagonal(pos, board):
    dy, dx = Piece.getDiff(pos)
    if abs(dx) != abs(dy):
        return False
    yDir = 1 if pos[0] < pos[2] else -1
    xDir = 1 if pos[1] < pos[3] else -1
    for i in range(1, abs(dx)):
        if board[pos[0] + i * yDir][pos[1] + i * xDir] is not None:
            return False
    return True

# returns the change in rows and columns from a move
@staticmethod
def getDiff(pos):
    return [pos[2] - pos[0], pos[3] - pos[1]]
