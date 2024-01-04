from enum import Enum

class Pawns(Enum):
    QUEEN = "Queen"
    KNIGHT = "Knight"
    ROOK = "Rook"
    BISHOP = "Bishop"

KNIGHT_MOVES = [
    (2, 1),
    (1, 2),
    (-2, 1),
    (-1, 2),
    (2, -1),
    (1, -2),
    (-2, -1),
    (-1, -2),
]
