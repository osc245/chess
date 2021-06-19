# ChessProgram
This program allows you to input moves (one or many) in the command line and the program will show the updated board either after all the moves have been done or up to the first invalid move if there is one. It also includes a couple dozen unit tests

The chess notation the program uses:
For normal moves or captures: oldPosition-newPosition i.e. e3-e4
You don't need to prefix the position with the piece type like in normal chess notation i.e. c3-b2 instead of Bc3-b2
To capture en passant: a5-b6ep
To promote: a7-a8=Q where the possible promotion pieces are Q, B, N, R
To castle: O-O (kingside) and O-O-O (queenside)

The program doesn't check if the king moves through check while castling and doesn't check for checkmates and stalemates.
