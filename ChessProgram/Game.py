from ChessProgram.Board import Board
from ChessProgram import Parser


# enter all the moves given so far but stops if an invalid move is given (either wrong notation or illegal move)
# returns true if the game is still going or false if it has finished
def doMoves(moves, currBoard):
    algebraicMoves = moves.split()
    moveObjects = Parser.parseMoves(moves)
    for i in range(len(moveObjects)):
        if not currBoard.move(moveObjects[i]):
            print("Illegal move: {}\n".format(algebraicMoves[i]))
            return
        currBoard.whitesTurn = not currBoard.whitesTurn


if __name__ == "__main__":
    board = Board()
    while True:
        print(board.toString())
        doMoves(input(), board)
