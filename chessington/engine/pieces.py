from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, List

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

    def get_available_moves(self, board) -> List[Square]:
        moves_list = []
        current_square = board.find_piece(self)

        if self.player == Player.BLACK:
            # Check the square one below
            square_in_front = Square.at(current_square.row - 1, current_square.col)
            if board.in_bounds(square_in_front):

                square_in_right = Square.at(current_square.row - 1, current_square.col + 1)
                square_in_left = Square.at(current_square.row - 1, current_square.col - 1)



                if board.in_bounds(square_in_right) and board.get_piece(square_in_right) != None and board.get_piece(square_in_right).player != self.player:
                    moves_list.append(square_in_right)
                if board.in_bounds(square_in_left) and board.get_piece(square_in_left) != None and board.get_piece(square_in_left).player != self.player:
                    moves_list.append(square_in_left)

                if board.get_piece(square_in_front) == None:
                    moves_list.append(square_in_front)

                    # Check the square two below
                    if self.moved == False:
                        square_in_front = Square.at(current_square.row - 2, current_square.col)
                        if board.in_bounds(square_in_front) and board.get_piece(square_in_front) == None:
                            moves_list.append(square_in_front)
        else:
            # Check the square one above
            square_in_front = Square.at(current_square.row + 1, current_square.col)
            if board.in_bounds(square_in_front):

                square_in_right = Square.at(current_square.row + 1, current_square.col + 1)
                square_in_left = Square.at(current_square.row + 1, current_square.col - 1)

                if board.in_bounds(square_in_right) and board.get_piece(square_in_right) != None and board.get_piece(square_in_right).player != self.player:
                    moves_list.append(square_in_right)
                if board.in_bounds(square_in_left) and board.get_piece(square_in_left) != None and board.get_piece(square_in_left).player != self.player:
                    moves_list.append(square_in_left)

                if board.get_piece(square_in_front) == None:
                    moves_list.append(square_in_front)

                    # Check the square two above
                    if self.moved == False:
                        square_in_front = Square.at(current_square.row + 2, current_square.col)
                        if board.in_bounds(square_in_front) and board.get_piece(square_in_front) == None:
                            moves_list.append(square_in_front)

        return moves_list

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)
        self.moved = True


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []