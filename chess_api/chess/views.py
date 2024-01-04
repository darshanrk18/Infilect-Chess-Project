from django.http import JsonResponse
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from .pawn_movements import (
    get_queen_moves,
    get_rook_moves,
    get_bishop_moves,
    get_knight_moves,
)
from typing import Any
from .constants import Pawns
import json

CACHE_TIMEOUT = 60 * 60 * 24


def get_possible_moves(
    piece: str | bytes | bytearray, position: str | bytes | bytearray
) -> list:
    """
    A function to fetch all possible moves of a pawn among Queen, Rook, Bishop
    and Knight at thier given position on the board.

    :param ``piece``: Pawn name in ``str`` to fetch its possible moves.
    :param ``position``: Position of the pawn on the board in ``str`` Eg."A5".
    """

    try:
        cache_key = f"{piece}_{position}"
        possible_moves = cache.get(cache_key)

        if possible_moves is not None:
            return possible_moves

        column, row = position[0], int(position[1])
        if piece == Pawns.QUEEN.value:
            possible_moves = get_queen_moves(column, row)
        elif piece == Pawns.BISHOP.value:
            possible_moves = get_bishop_moves(column, row)
        elif piece == Pawns.ROOK.value:
            possible_moves = get_rook_moves(column, row)
        elif piece == Pawns.KNIGHT.value:
            possible_moves = get_knight_moves(column, row)

        cache.set(cache_key, possible_moves, CACHE_TIMEOUT)

        return possible_moves

    except Exception as e:
        raise ValidationError(f"Invalid piece or position: {e}")


def get_valid_moves(
    piece: str | bytes | bytearray,
    piece_position: str | bytes | bytearray,
    pawns_positions: str | bytes | bytearray,
) -> list:
    """
    A function to fetch all valid moves (removing the invalid moves) of a pawn among
    Queen, Rook, Bishop and Knight at thier given position on the board.

    :param ``piece``: Pawn name in ``str`` to fetch its valid moves.
    :param ``position``: Position of the pawn on the board in ``str`` Eg."A5".
    :param ``pawns_positions``: Positions of all the pawns captured from the request body.
    """

    try:
        piece_moves = get_possible_moves(piece, piece_position)
        piece_invalid_moves = []

        for pawn in pawns_positions:
            if pawn != piece:
                piece_invalid_moves.extend(
                    get_possible_moves(pawn, pawns_positions[pawn])
                )

        piece_moves = set(piece_moves)
        piece_invalid_moves = set(piece_invalid_moves)

        return list(piece_moves - piece_invalid_moves)

    except Exception as e:
        raise ValidationError(f"Error calculating valid moves: {e}")


@csrf_exempt
def chess_endpoint(request: Any, slug: str) -> JsonResponse:
    try:
        if request.method == "POST":
            data = json.loads(request.body.decode("utf-8"))
            positions = data.get("positions", {})
            slug = slug.capitalize()
            piece_position = positions.get(slug)

            if piece_position is None:
                return JsonResponse(
                    {"error": f"No position provided for {slug}"}, status=400
                )

            valid_moves = get_valid_moves(slug, piece_position, positions)

            return JsonResponse({"valid_moves": valid_moves})

        return JsonResponse({"error": "Invalid request method"}, status=400)

    except ValidationError as ve:
        return JsonResponse({"error": str(ve)}, status=400)

    except Exception as e:
        return JsonResponse({"error": f"Internal Server Error: {e}"}, status=500)
