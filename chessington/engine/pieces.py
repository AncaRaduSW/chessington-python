from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, List

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

    def get_available_moves(self, board) -> List[Square]:
        moves_list = []
        current_square = board.find_piece(self)

        if self.player == Player.BLACK:
            # Check the square one below
            square_in_front = Square.at(current_square.row - 1, current_square.col)
            if board.in_bounds(square_in_front):

                square_in_right = Square.at(current_square.row - 1, current_square.col + 1)
                square_in_left = Square.at(current_square.row - 1, current_square.col - 1)

                if board.can_take(square_in_right, self.player):
                    moves_list.append(square_in_right)
                if board.can_take(square_in_left, self.player):
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

                if board.can_take(square_in_right, self.player):
                    moves_list.append(square_in_right)
                if board.can_take(square_in_left, self.player):
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
        moves_list = []
        current_square = board.find_piece(self)

        # Check the square up left
        # . * . . .
        # . . . . .
        # . . K . .
        # . . . . .
        # . . . . .
        square = Square.at(current_square.row + 2, current_square.col - 1)

        if board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)

        # Check the square up right
        # . . . * .
        # . . . . .
        # . . K . .
        # . . . . .
        # . . . . .
        square = Square.at(current_square.row + 2, current_square.col + 1)

        if board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)

        # Check the square sideways right up
        # . . . . .
        # . . . . *
        # . . K . .
        # . . . . .
        # . . . . .
        square = Square.at(current_square.row + 1, current_square.col + 2)

        if board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)

        # Check the square sideways right down
        # . . . . .
        # . . . . .
        # . . K . .
        # . . . . *
        # . . . . .
        square = Square.at(current_square.row - 1, current_square.col + 2)

        if board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)

        # Check the square down left
        # . . . . .
        # . . . . .
        # . . K . .
        # . . . . .
        # . * . . .
        square = Square.at(current_square.row - 2, current_square.col - 1)

        if board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)

        # Check the square down right
        # . . . . .
        # . . . . .
        # . . K . .
        # . . . . .
        # . . . * .
        square = Square.at(current_square.row - 2, current_square.col + 1)

        if board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)

        # Check the square sideways left up
        # . . . . .
        # * . . . .
        # . . K . .
        # . . . . .
        # . . . . .
        square = Square.at(current_square.row + 1, current_square.col - 2)

        if board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)

        # Check the square sideways left down
        # . . . . .
        # . . . . .
        # . . K . .
        # * . . . .
        # . . . . .
        square = Square.at(current_square.row - 1, current_square.col - 2)

        if board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)

        return moves_list


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        moves_list = []
        current_square = board.find_piece(self)

        # Go up right
        row = current_square.row + 1
        col = current_square.col + 1
        square = Square.at(row, col)
        while board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)
            else:
                break

            row += 1
            col += 1
            square = Square.at(row, col)

        # Go up left
        row = current_square.row + 1
        col = current_square.col - 1
        square = Square.at(row, col)
        while board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)
            else:
                break

            row += 1
            col -= 1
            square = Square.at(row, col)

        # Go down right
        row = current_square.row - 1
        col = current_square.col + 1
        square = Square.at(row, col)
        while board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)
            else:
                break

            row -= 1
            col += 1
            square = Square.at(row, col)

        # Go down left
        row = current_square.row - 1
        col = current_square.col - 1
        square = Square.at(row, col)
        while board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)
            else:
                break

            row -= 1
            col -= 1
            square = Square.at(row, col)

        return moves_list


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        moves_list = []
        current_square = board.find_piece(self)

        # Go up
        row = current_square.row + 1
        col = current_square.col
        square = Square.at(row, col)
        while board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)
            else:
                break

            row += 1
            square = Square.at(row, col)

        # Go down
        row = current_square.row - 1
        col = current_square.col
        square = Square.at(row, col)
        while board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)
            else:
                break

            row -= 1
            square = Square.at(row, col)

        # Go right
        row = current_square.row
        col = current_square.col + 1
        square = Square.at(row, col)
        while board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)
            else:
                break

            col += 1
            square = Square.at(row, col)

        # Go left
        row = current_square.row
        col = current_square.col - 1
        square = Square.at(row, col)
        while board.in_bounds(square):
            if board.get_piece(square) == None or board.can_take(square, self.player):
                moves_list.append(square)
            else:
                break

            col -= 1
            square = Square.at(row, col)

        return moves_list


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