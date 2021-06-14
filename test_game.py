from board import *
import unittest


class TestGame(unittest.TestCase):
    def test_3_row_board(self):
        game = Checkers(WhiteMove())
        check_board = [[None, game.new_white_pawn.create_pawn(), None, game.new_white_pawn.create_pawn(), None,
                        game.new_white_pawn.create_pawn(), None, game.new_white_pawn.create_pawn()],
                       [game.new_white_pawn.create_pawn(), None, game.new_white_pawn.create_pawn(), None,
                        game.new_white_pawn.create_pawn(), None, game.new_white_pawn.create_pawn(), None],
                       [None, game.new_white_pawn.create_pawn(), None, game.new_white_pawn.create_pawn(), None,
                        game.new_white_pawn.create_pawn(), None, game.new_white_pawn.create_pawn()],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [game.new_black_pawn.create_pawn(), None, game.new_black_pawn.create_pawn(), None,
                        game.new_black_pawn.create_pawn(), None, game.new_black_pawn.create_pawn(), None],
                       [None, game.new_black_pawn.create_pawn(), None, game.new_black_pawn.create_pawn(), None,
                        game.new_black_pawn.create_pawn(), None, game.new_black_pawn.create_pawn()],
                       [game.new_black_pawn.create_pawn(), None, game.new_black_pawn.create_pawn(), None,
                        game.new_black_pawn.create_pawn(), None, game.new_black_pawn.create_pawn(), None]]
        for row in range(8):
            for col in range(8):
                self.assertEqual(type(game.board_state[row][col]).__name__, type(check_board[row][col]).__name__)
