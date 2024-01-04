from .constants import KNIGHT_MOVES


def move_diagonal(column: str | bytes | bytearray, row: int) -> list:
    """
    A function to fetch all possible diagonal moves of a pawn among Queen, Rook, Bishop
    and Knight at thier given position on the board.

    :param ``column``: Pawn column pos in ``str`` Eg. "A" in "A5".
    :param ``row``: Pawn row pos in ``int`` Eg. "5" in "A5".
    """

    diagonal_moves = []

    for i in range(1, 9):
        #  Right upward diagonal
        if 1 <= row + i <= 8 and 1 <= ord(column) - ord("A") + 1 + i <= 8:
            diagonal_moves.append(f"{chr(ord(column) + i)}{row + i}")

        #  Right downward diagonal
        if 1 <= row - i <= 8 and 1 <= ord(column) - ord("A") + 1 + i <= 8:
            diagonal_moves.append(f"{chr(ord(column) + i)}{row - i}")

        #  Left upward diagonal
        if 1 <= row + i <= 8 and 1 <= ord(column) - ord("A") + 1 - i <= 8:
            diagonal_moves.append(f"{chr(ord(column) - i)}{row + i}")

        #  Left downward diagonal
        if 1 <= row - i <= 8 and 1 <= ord(column) - ord("A") + 1 - i <= 8:
            diagonal_moves.append(f"{chr(ord(column) - i)}{row - i}")

    return diagonal_moves


def move_horizontal_vertical(column: str | bytes | bytearray, row: int) -> list:
    """
    A function to fetch all possible horizontal and vertical moves of a pawn among
    Queen, Rook, Bishop and Knight at thier given position on the board.

    :param ``column``: Pawn column pos in ``str`` Eg. "A" in "A5".
    :param ``row``: Pawn row pos in ``int`` Eg. "5" in "A5".
    """

    horizontal_vertical_moves = []

    for i in range(1, 9):
        # Vertical movement
        if i != row:
            horizontal_vertical_moves.append(f"{column}{i}")

        # Horizontal movement
        if i != ord(column) - ord("A") + 1:
            horizontal_vertical_moves.append(f"{chr(ord('A') + i - 1)}{row}")

    return horizontal_vertical_moves


def move_lshaped(column: str | bytes | bytearray, row: int) -> list:
    """
    A function to fetch all possible L-shaped moves of a pawn among Queen, Rook, Bishop
    and Knight at thier given position on the board.

    :param ``column``: Pawn column pos in ``str`` Eg. "A" in "A5".
    :param ``row``: Pawn row pos in ``int`` Eg. "5" in "A5".
    """

    l_moves = []

    for move in KNIGHT_MOVES:
        new_row = row + move[1]
        new_column = chr(ord(column) + move[0])
        if 1 <= new_row <= 8 and 1 <= ord(new_column) - ord("A") + 1 <= 8:
            l_moves.append(f"{new_column}{new_row}")

    return l_moves
