from .utils import move_diagonal, move_horizontal_vertical, move_lshaped


def get_queen_moves(column: str | bytes | bytearray, row: int) -> list:
    """
    A function to fetch all possible moves of a Queen at the given position on the board.

    :param ``column``: Pawn column pos in ``str`` Eg. "A" in "A5".
    :param ``row``: Pawn row pos in ``int`` Eg. "5" in "A5".
    """

    queen_moves = []

    # Horizontal - Vertical moves
    queen_moves.extend(move_horizontal_vertical(column, row))

    # Diagonal moves
    queen_moves.extend(move_diagonal(column, row))

    return queen_moves


def get_bishop_moves(column: str | bytes | bytearray, row: int) -> list:
    """
    A function to fetch all possible moves of a Bishop at the given position on the board.

    :param ``column``: Pawn column pos in ``str`` Eg. "A" in "A5".
    :param ``row``: Pawn row pos in ``int`` Eg. "5" in "A5".
    """

    bishop_moves = []

    # Diagonal moves
    bishop_moves.extend(move_diagonal(column, row))

    return bishop_moves


def get_rook_moves(column: str | bytes | bytearray, row: int) -> list:
    """
    A function to fetch all possible moves of a Rook at the given position on the board.

    :param ``column``: Pawn column pos in ``str`` Eg. "A" in "A5".
    :param ``row``: Pawn row pos in ``int`` Eg. "5" in "A5".
    """

    rook_moves = []

    # Horizontal - Vertical moves
    rook_moves.extend(move_horizontal_vertical(column, row))

    return rook_moves


def get_knight_moves(column: str | bytes | bytearray, row: int) -> list:
    """
    A function to fetch all possible moves of a Knight at the given position on the board.

    :param ``column``: Pawn column pos in ``str`` Eg. "A" in "A5".
    :param ``row``: Pawn row pos in ``int`` Eg. "5" in "A5".
    """

    knight_moves = []

    # L-Shaped moves
    knight_moves.extend(move_lshaped(column, row))

    return knight_moves
