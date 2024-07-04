from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn
from chessington.engine.pieces import Knight

class TestKnights:

    @staticmethod
    def test_knights_can_move_up_L_shape():

        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(3, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(5, 3) in moves
        assert Square.at(5, 5) in moves

    @staticmethod
    def test_knights_can_move_sideways_up_L_shape():

        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(3, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(4, 2) in moves
        assert Square.at(4, 6) in moves

    @staticmethod
    def test_knights_can_move_down_L_shape():

        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(3, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(1, 3) in moves
        assert Square.at(1, 5) in moves

    @staticmethod
    def test_knights_can_move_sideways_down_L_shape():

        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(3, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(2, 2) in moves
        assert Square.at(2, 6) in moves

    @staticmethod
    def test_white_knight_cannot_move_if_white_piece_at_landing_spot():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(3, 4)
        board.set_piece(square, knight)

        obstructing_square = Square.at(5, 3)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(5, 5)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(4, 2)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(4, 6)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(1, 3)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(1, 5)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(2, 2)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(2, 6)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert len(moves) == 0


    @staticmethod
    def test_black_knight_cannot_move_if_black_piece_at_landing_spot():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(3, 4)
        board.set_piece(square, knight)

        obstructing_square = Square.at(5, 3)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(5, 5)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(4, 2)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(4, 6)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(1, 3)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(1, 5)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(2, 2)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(2, 6)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_knight_cannot_move_right():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(2, 6)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(1, 8) not in moves
        assert Square.at(3, 8) not in moves

    @staticmethod
    def test_knight_cannot_move_left():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(2, 1)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(1, -1) not in moves
        assert Square.at(3, -1) not in moves

    @staticmethod
    def test_knight_cannot_move_up():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(6, 2)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(8, 1) not in moves
        assert Square.at(8, 3) not in moves

    @staticmethod
    def test_knight_cannot_move_down():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(1, 2)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(-1, 1) not in moves
        assert Square.at(-1, 3) not in moves


    @staticmethod
    def test_WHITE_Knight_can_capture():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(3, 4)
        board.set_piece(square, knight)

        obstructing_square = Square.at(5, 3)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(5, 5)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(4, 2)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(4, 6)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(1, 3)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(1, 5)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(2, 2)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square = Square.at(2, 6)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(5, 3) in moves
        assert Square.at(5, 5) in moves
        assert Square.at(4, 2) in moves
        assert Square.at(4, 6) in moves
        assert Square.at(1, 3) in moves
        assert Square.at(1, 5) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(2, 6) in moves

        @staticmethod
        def test_black_knight_can_capture():
            # Arrange
            board = Board.empty()
            knight = Knight(Player.BLACK)
            square = Square.at(3, 4)
            board.set_piece(square, knight)

            obstructing_square = Square.at(5, 3)
            obstruction = Pawn(Player.WHITE)
            board.set_piece(obstructing_square, obstruction)

            obstructing_square = Square.at(5, 5)
            obstruction = Pawn(Player.WHITE)
            board.set_piece(obstructing_square, obstruction)

            obstructing_square = Square.at(4, 2)
            obstruction = Pawn(Player.WHITE)
            board.set_piece(obstructing_square, obstruction)

            obstructing_square = Square.at(4, 6)
            obstruction = Pawn(Player.WHITE)
            board.set_piece(obstructing_square, obstruction)

            obstructing_square = Square.at(1, 3)
            obstruction = Pawn(Player.WHITE)
            board.set_piece(obstructing_square, obstruction)

            obstructing_square = Square.at(1, 5)
            obstruction = Pawn(Player.WHITE)
            board.set_piece(obstructing_square, obstruction)

            obstructing_square = Square.at(2, 2)
            obstruction = Pawn(Player.WHITE)
            board.set_piece(obstructing_square, obstruction)

            obstructing_square = Square.at(2, 6)
            obstruction = Pawn(Player.WHITE)
            board.set_piece(obstructing_square, obstruction)

            # Act
            moves = knight.get_available_moves(board)

            # Assert
            assert Square.at(5, 3) in moves
            assert Square.at(5, 5) in moves
            assert Square.at(4, 2) in moves
            assert Square.at(4, 6) in moves
            assert Square.at(1, 3) in moves
            assert Square.at(1, 5) in moves
            assert Square.at(2, 2) in moves
            assert Square.at(2, 6) in moves
