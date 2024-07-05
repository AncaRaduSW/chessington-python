"""
A module providing a representation of a chess board. The rules of chess are not implemented - 
this is just a "dumb" board that will let you move pieces around as you like.
"""
from PIL.ImageCms import Direction

from chessington.engine.data import Player, Square
from chessington.engine.directions import Directions
from chessington.engine.pieces import Pawn, Knight, Bishop, Rook, Queen, King, Piece
from chessington.engine.directions import Directions

BOARD_SIZE = 8


class Board:
    """
    A representation of the chess board, and the pieces on it.
    """

    def __init__(self, player, board_state):
        self.current_player = Player.WHITE
        self.board = board_state

    @staticmethod
    def empty():
        return Board(Player.WHITE, Board._create_empty_board())

    @staticmethod
    def at_starting_position():
        return Board(Player.WHITE, Board._create_starting_board())

    @staticmethod
    def _create_empty_board():
        return [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    @staticmethod
    def _create_starting_board():

        # Create an empty board
        board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

        # Setup the rows of pawns
        board[1] = [Pawn(Player.WHITE) for _ in range(BOARD_SIZE)]
        board[6] = [Pawn(Player.BLACK) for _ in range(BOARD_SIZE)]

        # Setup the rows of pieces
        piece_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        board[0] = list(map(lambda piece: piece(Player.WHITE), piece_row))
        board[7] = list(map(lambda piece: piece(Player.BLACK), piece_row))

        return board

    def in_bounds(self, square):
        return -1 < square.row < BOARD_SIZE and -1 < square.col < BOARD_SIZE

    def can_take(self, square, player):
        return self.in_bounds(square) and self.get_piece(square) != None and self.get_piece(square).player != player

    def set_piece(self, square, piece):
        """
        Places the piece at the given position on the board.
        """
        self.board[square.row][square.col] = piece

    def get_piece(self, square):
        """
        Retrieves the piece from the given square of the board.
        """
        return self.board[square.row][square.col]

    def find_piece(self, piece_to_find):
        """
        Searches for the given piece on the board and returns its square.
        """
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] is piece_to_find:
                    return Square.at(row, col)
        raise Exception('The supplied piece is not on the board')

    def move_is_diagonal(self, from_square, to_square):
        return abs(from_square.row - to_square.row) == 1 and abs(from_square.col - to_square.col) == 1

    def get_side_direction_from_diagonal(self, from_square, to_square):
        if to_square.col - from_square.col > 0:
            return 'EAST'
        else:
            return 'WEST'

    def move_piece(self, from_square, to_square):
        """
        Moves the piece from the given starting square to the given destination square.
        """
        moving_piece = self.get_piece(from_square)
        final_piece = self.get_piece(to_square)

        # En passant start
        if moving_piece.player == self.current_player:
            if type(moving_piece) is Pawn:
                if self.move_is_diagonal(from_square, to_square):
                    side_direction = self.get_side_direction_from_diagonal(from_square, to_square)
                    square_at_side = Square.at(from_square.row,
                                               from_square.col + Directions.Cardinals[side_direction]['col'])
                    piece_at_side = self.get_piece(square_at_side)

                    if final_piece is None and type(piece_at_side) is Pawn:
                        self.set_piece(square_at_side, None)
        # En passant end

            if moving_piece is not None:
                self.set_piece(to_square, moving_piece)
                self.set_piece(from_square, None)
                self.current_player = self.current_player.opponent()
