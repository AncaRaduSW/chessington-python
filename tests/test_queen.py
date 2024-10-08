from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn
from chessington.engine.pieces import Queen

class TestQueens:

    @staticmethod
    def test_queen_can_move_up():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(1, 3)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(5, 3) in moves

    @staticmethod
    def test_queen_can_move_down():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(3, 3)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) in moves
        assert Square.at(1, 3) in moves
        assert Square.at(0, 3) in moves

    @staticmethod
    def test_queen_can_move_left():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(3, 3)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(3, 2) in moves
        assert Square.at(3, 1) in moves
        assert Square.at(3, 0) in moves

    @staticmethod
    def test_queen_can_move_right():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(3, 3)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 6) in moves
        assert Square.at(3, 7) in moves
    @staticmethod

    @staticmethod
    def test_queen_can_move_up_right_corner_direction():

        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(0, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(1, 1) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(5, 5) in moves
        assert Square.at(6, 6) in moves
        assert Square.at(7, 7) in moves


    @staticmethod
    def test_queen_can_move_up_left_corner_direction():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(0, 7)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(1, 6) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(3, 4) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(6, 1) in moves
        assert Square.at(7, 0) in moves

    @staticmethod
    def test_queen_can_move_down_right_corner_direction():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(7, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(6, 1) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(3, 4) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 6) in moves
        assert Square.at(0, 7) in moves

    @staticmethod
    def test_queen_can_move_down_left_corner_direction():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(7, 7)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(6, 6) in moves
        assert Square.at(5, 5) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(1, 1) in moves
        assert Square.at(0, 0) in moves




    @staticmethod
    def test_white_queen_cannot_move_up_if_white_piece_is_in_way():

        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(3, 2)
        board.set_piece(square, queen)

        obstructing_square = Square.at(4, 2)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(4, 2) not in moves
        assert Square.at(5, 2) not in moves
        assert Square.at(6, 2) not in moves
        assert Square.at(7, 2) not in moves

    @staticmethod
    def test_white_queen_cannot_move_left_if_white_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(3, 2)
        board.set_piece(square, queen)

        obstructing_square = Square.at(3, 1)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(3, 1) not in moves
        assert Square.at(3, 0) not in moves

    @staticmethod
    def test_white_queen_cannot_move_right_if_white_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(3, 2)
        board.set_piece(square, queen)

        obstructing_square = Square.at(3, 3)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(3, 3) not in moves
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_white_queen_cannot_move_down_if_white_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(3, 2)
        board.set_piece(square, queen)

        obstructing_square = Square.at(2, 2)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(2, 2) not in moves
        assert Square.at(1, 2) not in moves

    @staticmethod
    def test_black_queen_cannot_move_up_if_black_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(3, 3)
        board.set_piece(square, queen)

        obstructing_square = Square.at(4, 3)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(4, 3) not in moves
        assert Square.at(5, 3) not in moves

    @staticmethod
    def test_black_queen_cannot_move_left_if_black_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(3, 3)
        board.set_piece(square, queen)

        obstructing_square = Square.at(3, 2)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(3, 2) not in moves
        assert Square.at(3, 1) not in moves

    @staticmethod
    def test_black_queen_cannot_move_right_if_black_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(3, 3)
        board.set_piece(square, queen)

        obstructing_square = Square.at(3, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves
        assert Square.at(3, 5) not in moves

    @staticmethod
    def test_black_queen_cannot_move_down_if_black_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(3, 3)
        board.set_piece(square, queen)

        obstructing_square = Square.at(2, 3)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) not in moves
        assert Square.at(1, 3) not in moves

    @staticmethod
    def test_white_queen_cannot_move_up_right_corner_if_white_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(3, 2)
        board.set_piece(square, queen)

        obstructing_square = Square.at(4, 3)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(4, 3) not in moves
        assert Square.at(5, 4) not in moves
        assert Square.at(6, 5) not in moves
        assert Square.at(7, 6) not in moves

    @staticmethod
    def test_white_queen_cannot_move_up_left_corner_if_white_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(3, 2)
        board.set_piece(square, queen)

        obstructing_square = Square.at(4, 1)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(4, 1) not in moves

    @staticmethod
    def test_white_queen_cannot_move_down_right_corner_if_white_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(3, 2)
        board.set_piece(square, queen)

        obstructing_square = Square.at(2, 3)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) not in moves

    @staticmethod
    def test_white_queen_cannot_move_down_left_corner_if_white_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(3, 2)
        board.set_piece(square, queen)

        obstructing_square = Square.at(2, 1)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(2, 1) not in moves

    @staticmethod
    def test_black_queen_cannot_move_up_right_corner_if_black_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(3, 3)
        board.set_piece(square, queen)

        obstructing_square = Square.at(4, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_black_queen_cannot_move_up_left_corner_if_black_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(3, 3)
        board.set_piece(square, queen)

        obstructing_square = Square.at(4, 2)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(4, 2) not in moves

    @staticmethod
    def test_black_queen_cannot_move_down_right_corner_if_black_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(3, 3)
        board.set_piece(square, queen)

        obstructing_square = Square.at(2, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(2, 4) not in moves

    @staticmethod
    def test_black_queen_cannot_move_down_left_corner_if_black_piece_is_in_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(3, 3)
        board.set_piece(square, queen)

        obstructing_square = Square.at(2, 2)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(2, 2) not in moves

    @staticmethod
    def test_white_queen_cannot_move_at_top_of_board():

        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(7, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(8, 0) not in moves

    @staticmethod
    def test_white_queen_cannot_move_at_bottom_of_board():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(0, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(-1, 0) not in moves

    @staticmethod
    def test_white_queen_cannot_move_at_left_of_board():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(0, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(0, -1) not in moves

    @staticmethod
    def test_white_queen_cannot_move_at_right_of_board():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(0, 7)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(0, 8) not in moves

    @staticmethod
    def test_black_queen_cannot_move_at_top_of_board():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(7, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(8, 0) not in moves

    @staticmethod
    def test_black_queen_cannot_move_at_bottom_of_board():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(0, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(-1, 0) not in moves

    @staticmethod
    def test_black_queen_cannot_move_at_left_of_board():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(0, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(0, -1) not in moves

    @staticmethod
    def test_black_queen_cannot_move_at_right_of_board():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(0, 7)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(0, 8) not in moves

    @staticmethod
    def test_white_queens_can_capture_cardinally():

        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(2, 2)
        board.set_piece(square, queen)

        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(3, 2)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.BLACK)
        enemy2_square = Square.at(2, 3)
        board.set_piece(enemy2_square, enemy2)

        enemy3 = Pawn(Player.BLACK)
        enemy3_square = Square.at(1, 2)
        board.set_piece(enemy3_square, enemy3)

        enemy4 = Pawn(Player.BLACK)
        enemy4_square = Square.at(2, 1)
        board.set_piece(enemy4_square, enemy4)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves
        assert enemy3_square in moves
        assert enemy4_square in moves

    @staticmethod
    def test_black_queens_can_capture_cardinally():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(2, 2)
        board.set_piece(square, queen)

        enemy1 = Pawn(Player.WHITE)
        enemy1_square = Square.at(3, 2)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.WHITE)
        enemy2_square = Square.at(2, 3)
        board.set_piece(enemy2_square, enemy2)

        enemy3 = Pawn(Player.WHITE)
        enemy3_square = Square.at(1, 2)
        board.set_piece(enemy3_square, enemy3)

        enemy4 = Pawn(Player.WHITE)
        enemy4_square = Square.at(2, 1)
        board.set_piece(enemy4_square, enemy4)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves
        assert enemy3_square in moves
        assert enemy4_square in moves


    @staticmethod
    def test_white_queens_can_capture_diagonally():

        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(2, 3)
        board.set_piece(square, queen)

        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(3, 4)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.BLACK)
        enemy2_square = Square.at(1, 2)
        board.set_piece(enemy2_square, enemy2)

        enemy3 = Pawn(Player.BLACK)
        enemy3_square = Square.at(1, 4)
        board.set_piece(enemy3_square, enemy3)

        enemy4 = Pawn(Player.BLACK)
        enemy4_square = Square.at(3, 2)
        board.set_piece(enemy4_square, enemy4)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves
        assert enemy3_square in moves
        assert enemy4_square in moves

    @staticmethod
    def test_black_queens_can_capture_diagonally():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(2, 2)
        board.set_piece(square, queen)

        enemy1 = Pawn(Player.WHITE)
        enemy1_square = Square.at(3, 3)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.WHITE)
        enemy2_square = Square.at(1, 1)
        board.set_piece(enemy2_square, enemy2)

        enemy3 = Pawn(Player.WHITE)
        enemy3_square = Square.at(1, 3)
        board.set_piece(enemy3_square, enemy3)

        enemy4 = Pawn(Player.WHITE)
        enemy4_square = Square.at(3, 1)
        board.set_piece(enemy4_square, enemy4)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves
        assert enemy3_square in moves
        assert enemy4_square in moves
