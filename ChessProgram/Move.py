class Move:
    def __init__(self, oldRow, oldCol, newRow, newCol, qsCastle=False, ksCastle=False, promotion=False, promotionPiece="",
                 enPassant=False):
        self.oldRow = oldRow
        self.oldCol = oldCol
        self.newRow = newRow
        self.newCol = newCol
        self.qsCastle = qsCastle
        self.ksCastle = ksCastle
        self.promotion = promotion
        self.promotionPiece = promotionPiece
        self.enPassant = enPassant
