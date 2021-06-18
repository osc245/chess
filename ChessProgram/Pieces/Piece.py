class Piece:
    def __init__(self, isWhite, upperChar, lowerChar):
        self.isWhite = isWhite
        self.displayChar = upperChar if isWhite else lowerChar

    # should be implemented in subclasses
    def toString(self):
        return displayChar


