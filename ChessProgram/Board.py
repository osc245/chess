import copy
from .Pieces.Bishop import Bishop
from .Pieces.Knight import Knight
from .Pieces.Queen import Queen
from .Pieces.King import King
from .Pieces.Rook import Rook
from .Pieces.Pawn import Pawn
from .Move import Move


class Board:
    def __init__(self):
        self.board = [[Rook(True), Knight(True), Bishop(True), Queen(True), King(True), Bishop(True), Knight(True),
                       Rook(True)],
                      [Pawn(True) for _ in range(8)],
                      [None] * 8, [None] * 8, [None] * 8, [None] * 8,
                      [Pawn(False) for _ in range(8)],
                      [Rook(False), Knight(False), Bishop(False), Queen(False), King(False), Bishop(False),
                       Knight(False), Rook(False)]]
        self.whitesTurn = True

    def toString(self):
        board = ""
        for i in range(7, -1, -1):
            board += str(i + 1) + "|"
            for j in range(8):
                board += "_|" if self.board[i][j] is None else self.board[i][j].toString() + "|"
            board += "\n"
        board += "  a b c d e f g h\n"
        return board

    # updates board with given move, if possible and returns True or False depending on whether the move could be made
    def move(self, move):
        if self.checkMove(move):
            self.doMove(move)
            return True
        else:
            return False

    # checks whether the given piece can move to a given square
    def checkMove(self, move):
        print(move.oldRow, move.oldCol, move.newRow, move.newCol)
        print(1)
        # check that the move is valid
        if not self.validMovement(move):
            return False
        print(2)

        # make a copy of the board, make the move then see if making that move would put the player's king in check
        tempBoard = copy.deepcopy(self)
        tempBoard.doMove(move)
        if tempBoard.inCheck(self.whitesTurn):
            return False
        return True

    # checks whether the proposed movement is valid
    # doesn't check that the players king isn't in check
    def validMovement(self, move):
        # moving to the same square
        if move.oldRow == move.newRow and move.oldCol == move.newCol:
            return False

        # there is not piece in initial position
        if self.board[move.oldRow][move.oldCol] is None:
            return False

        # trying to move opponents piece
        if self.whitesTurn != self.board[move.oldRow][move.oldCol].isWhite:
            return False

        # check that the square the given piece is trying to move on doesn't have a piece belonging to current player
        # this means either the piece is moving normally or capturing opponents piece
        if self.board[move.newRow][move.newCol] is not None and self.board[move.newRow][move.newCol].isWhite == self.whitesTurn:
            return False

        # check that the piece can move in those direction/s
        if not self.board[move.oldRow][move.oldCol].validMove(move, self.board):
            return False

        # if the player is castling check that the rook can move as well
        if move.ksCastle or move.qsCastle:
            backRank = move.oldRow
            oldRookCol, newRookCol = (7, 5) if move.ksCastle else (0, 3)
            rookMove = Move(backRank, oldRookCol, backRank, newRookCol)
            if not self.checkMove(rookMove):
                return False
        return True

    # checks whether the player specified by the parameter is in check
    def inCheck(self, white):
        self.whitesTurn = not white
        pieces = self.getPieces(not white)
        kingRow, kingCol = self.getKing(white)
        for pieceRow, pieceCol in pieces:
            if self.validMovement(Move(pieceRow, pieceCol, kingRow, kingCol)):
                return True
        return False

    # will update the board with a given move
    def doMove(self, move):
        # move the piece on to the new square and remove it from the old square
        self.board[move.newRow][move.newCol] = self.board[move.oldRow][move.oldCol]
        self.board[move.oldRow][move.oldCol] = None

        # if the pawn is capturing en passant also remove the captured pawn
        if move.enPassant:
            self.board[move.oldRow][move.newCol] = None

        # move rook if there is a castle
        if move.ksCastle or move.qsCastle:
            row = 0 if self.whitesTurn else 7
            if move.ksCastle:
                self.board[row][5] = self.board[row][7]
                self.board[row][7] = None
            else:
                self.board[row][3] = self.board[row][0]
                self.board[row][0] = None

        # change pawn to given piece if it is promoting
        if move.promotion:
            if move.promotionPiece == "N":
                self.board[move.newRow][move.newCol] = Knight(self.whitesTurn)
            elif move.promotionPiece == "B":
                self.board[move.newRow][move.newCol] = Bishop(self.whitesTurn)
            elif move.promotionPiece == "R":
                self.board[move.newRow][move.newCol] = Rook(self.whitesTurn)
            elif move.promotionPiece == "Q":
                self.board[move.newRow][move.newCol] = Queen(self.whitesTurn)

    # get all the positions of all pieces of the given player
    def getPieces(self, white):
        return [[i, j] for i in range(8) for j in range(8) if self.board[i][j] is not None and
                not isinstance(self.board[i][j], King) and self.board[i][j].isWhite == white]

    # get the position of the king of the given player
    def getKing(self, white):
        return [[i, j] for i in range(8) for j in range(8) if isinstance(self.board[i][j], King) and
                self.board[i][j].isWhite == white][0]
