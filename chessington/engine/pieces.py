from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, List
from chessington.engine.directions import Directions

BOARD_SIZE = 8

if TYPE_CHECKING:
    from chessington.engine.board import Board


class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player: Player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board: Board) -> List[Square]:
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    moved = False
    just_moved_2_squares = False

    def get_moves_for_certain_player(self, board, direction):

        moves_list = []
        current_square = board.find_piece(self)

        # Check the square one below
        square_in_front = Square.at(current_square.row + Directions.Cardinals[direction]['row'], current_square.col + Directions.Cardinals[direction]['col'])
        if board.in_bounds(square_in_front):

            for side_direction in ['EAST', 'WEST']:
                square_at_front_and_side = Square.at(square_in_front.row + Directions.Cardinals[side_direction]['row'],
                                           square_in_front.col + Directions.Cardinals[side_direction]['col'])
                if board.can_take(square_at_front_and_side, self.player):
                    moves_list.append(square_at_front_and_side)

            if board.get_piece(square_in_front) is None:
                moves_list.append(square_in_front)

                # Check the square two below
                if not self.moved:
                    square_2_in_front = Square.at(square_in_front.row + Directions.Cardinals[direction]['row'], square_in_front.col + Directions.Cardinals[direction]['col'])
                    if board.in_bounds(square_2_in_front) and board.get_piece(square_2_in_front) is None:
                        moves_list.append(square_2_in_front)

            # En-Passant start
            for direction in ['EAST', 'WEST']:
                square_at_front_and_side = Square.at(square_in_front.row + Directions.Cardinals[direction]['row'],
                                                     square_in_front.col + Directions.Cardinals[direction]['col'])

                if board.in_bounds(square_at_front_and_side) and board.get_piece(square_at_front_and_side) is None:
                    square_at_side = Square.at(current_square.row + Directions.Cardinals[direction]['row'], current_square.col + Directions.Cardinals[direction]['col'])

                    if type(board.get_piece(square_at_side)) is Pawn:
                        en_passant_pawn = board.get_piece(square_at_side)
                        if en_passant_pawn.just_moved_2_squares:
                            moves_list.append(square_at_front_and_side)
            # En-

        return moves_list

    def get_available_moves(self, board) -> List[Square]:
        if self.player == Player.BLACK:
            return self.get_moves_for_certain_player(board, 'SOUTH')
        else:
            return self.get_moves_for_certain_player(board, 'NORTH')

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


        if abs(current_square.row - new_square.row) == 2:
            self.just_moved_2_squares = True
        else:
            self.just_moved_2_squares = False

        self.moved = True


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        moves_list = []
        current_square = board.find_piece(self)

        for direction in Directions.KnightDirections:
            square = Square.at(current_square.row + Directions.KnightDirections[direction]['row'],
                               current_square.col + Directions.KnightDirections[direction]['col'])
            if board.in_bounds(square):
                if board.get_piece(square) is None or board.can_take(square, self.player):
                    moves_list.append(square)

        return moves_list


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        moves_list = []
        current_square = board.find_piece(self)

        for direction in Directions.Corners:

            square = Square.at(current_square.row + Directions.Corners[direction]['row'], current_square.col + Directions.Corners[direction]['col'])
            while board.in_bounds(square):
                if board.can_take(square, self.player):
                    moves_list.append(square)
                    break
                elif board.get_piece(square) is None:
                    moves_list.append(square)
                else:
                    break

                square = Square.at(square.row + Directions.Corners[direction]['row'], square.col + Directions.Corners[direction]['col'])

        return moves_list


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        moves_list = []
        current_square = board.find_piece(self)

        for direction in Directions.Cardinals:

            square = Square.at(current_square.row + Directions.Cardinals[direction]['row'],
                               current_square.col + Directions.Cardinals[direction]['col'])
            while board.in_bounds(square):
                if board.can_take(square, self.player):
                    moves_list.append(square)
                    break
                elif board.get_piece(square) is None:
                    moves_list.append(square)
                else:
                    break

                square = Square.at(square.row + Directions.Cardinals[direction]['row'],
                                   square.col + Directions.Cardinals[direction]['col'])

        return moves_list


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        moves_list = []
        current_square = board.find_piece(self)

        for direction in Directions.Corners:

            square = Square.at(current_square.row + Directions.Corners[direction]['row'],
                               current_square.col + Directions.Corners[direction]['col'])
            while board.in_bounds(square):
                if board.can_take(square, self.player):
                    moves_list.append(square)
                    break
                elif board.get_piece(square) is None:
                    moves_list.append(square)
                else:
                    break

                square = Square.at(square.row + Directions.Corners[direction]['row'],
                                   square.col + Directions.Corners[direction]['col'])

        for direction in Directions.Cardinals:

            square = Square.at(current_square.row + Directions.Cardinals[direction]['row'],
                               current_square.col + Directions.Cardinals[direction]['col'])
            while board.in_bounds(square):
                if board.can_take(square, self.player):
                    moves_list.append(square)
                    break
                elif board.get_piece(square) is None:
                    moves_list.append(square)
                else:
                    break

                square = Square.at(square.row + Directions.Cardinals[direction]['row'],
                                   square.col + Directions.Cardinals[direction]['col'])

        return moves_list


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        moves_list = []
        current_square = board.find_piece(self)

        for direction in Directions.Corners:

            square = Square.at(current_square.row + Directions.Corners[direction]['row'],
                               current_square.col + Directions.Corners[direction]['col'])
            if board.in_bounds(square):
                if board.get_piece(square) is None or board.can_take(square, self.player):
                    moves_list.append(square)

        for direction in Directions.Cardinals:

            square = Square.at(current_square.row + Directions.Cardinals[direction]['row'],
                               current_square.col + Directions.Cardinals[direction]['col'])
            if board.in_bounds(square):
                if board.get_piece(square) is None or board.can_take(square, self.player):
                    moves_list.append(square)

        return moves_list
