import re
from .Move import Move

# for converting the column letter to its corresponding index
toNum = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}


# converts a list of chess moves in algebraic notation to move objects
def parseMoves(coOrdinates):
    moves = []
    moveList = coOrdinates.split()
    whitesTurn = True

    for move in moveList:
        backRank = 0 if whitesTurn else 7

        # castling
        if move[0:5] == "O-O-O":
            moves.append(Move(backRank, 4, backRank, 2, qsCastle=True))
        elif move[0:3] == "O-O":
            moves.append(Move(backRank, 4, backRank, 6, ksCastle=True))
        else:  # normal moves
            # check expression is in right format
            regex = re.compile("[a-h][1-8]-[a-h][1-8](ep)?(=[NBRQ])?$")
            if not regex.match(move):
                print("Invalid notation:", move)
                return moves
            moveObject = Move(int(move[1]) - 1, toNum[move[0]], int(move[4]) - 1, toNum[move[3]])

            # check if there is a promotion or en passant
            if len(move) == 7:
                if re.match(".*=[NBRQ]$", move):
                    moveObject.promotion = True
                    moveObject.promotionPiece = move[6]
                elif re.match(".*ep$", move):
                    moveObject.enPassant = True

            moves.append(moveObject)
        whitesTurn = not whitesTurn
    return moves
