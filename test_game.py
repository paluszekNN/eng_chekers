from board import *
import unittest


class TestGame(unittest.TestCase):
    def test_3_row_board(self):
        game = Checkers(WhiteMove())
        check_board = [[0, 1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 1, 0, 1, 0, 1, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, 0, -1, 0, -1, 0, -1, 0],
                       [0, -1, 0, -1, 0, -1, 0, -1],
                       [-1, 0, -1, 0, -1, 0, -1, 0]]
        self.assertEqual(game.transposition_board(), check_board)

    def test_move_in_game(self):
        game = Checkers(WhiteMove())
        move = Move('C2', 'D3')
        game.request(move)
        check_board = [[0, 1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 0, 0, 1, 0, 1, 0, 1],
                       [0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, 0, -1, 0, -1, 0, -1, 0],
                       [0, -1, 0, -1, 0, -1, 0, -1],
                       [-1, 0, -1, 0, -1, 0, -1, 0]]
        self.assertEqual(game.transposition_board(), check_board)

    def test_capture(self):
        game = Checkers(WhiteMove())
        move = Move('C2', 'D3')
        game.request(move)
        check_board = [[0, 1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 0, 0, 1, 0, 1, 0, 1],
                       [0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [-1, 0, -1, 0, -1, 0, -1, 0],
                       [0, -1, 0, -1, 0, -1, 0, -1],
                       [-1, 0, -1, 0, -1, 0, -1, 0]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('F1', 'E2')
        game.request(move)
        check_board = [[0, 1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 0, 0, 1, 0, 1, 0, 1],
                       [0, 0, 1, 0, 0, 0, 0, 0],
                       [0, -1, 0, 0, 0, 0, 0, 0],
                       [0, 0, -1, 0, -1, 0, -1, 0],
                       [0, -1, 0, -1, 0, -1, 0, -1],
                       [-1, 0, -1, 0, -1, 0, -1, 0]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('D3', 'E4')
        game.request(move)
        check_board = [[0, 1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 0, 0, 1, 0, 1, 0, 1],
                       [0, 0, 1, 0, 0, 0, 0, 0],
                       [0, -1, 0, 0, 0, 0, 0, 0],
                       [0, 0, -1, 0, -1, 0, -1, 0],
                       [0, -1, 0, -1, 0, -1, 0, -1],
                       [-1, 0, -1, 0, -1, 0, -1, 0]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('D3', 'F1')
        game.request(move)
        check_board = [[0, 1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 0, 0, 1, 0, 1, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, -1, 0, -1, 0, -1, 0],
                       [0, -1, 0, -1, 0, -1, 0, -1],
                       [-1, 0, -1, 0, -1, 0, -1, 0]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('F3', 'E2')
        game.request(move)
        check_board = [[0, 1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 0, 0, 1, 0, 1, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, -1, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, -1, 0, -1, 0],
                       [0, -1, 0, -1, 0, -1, 0, -1],
                       [-1, 0, -1, 0, -1, 0, -1, 0]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('C4', 'D3')
        game.request(move)
        check_board = [[0, 1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 1, 0, 0, 0, 0, 0],
                       [0, -1, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, -1, 0, -1, 0],
                       [0, -1, 0, -1, 0, -1, 0, -1],
                       [-1, 0, -1, 0, -1, 0, -1, 0]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('E2', 'D1')
        game.request(move)
        check_board = [[0, 1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 1, 0, 0, 0, 0, 0],
                       [0, -1, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, -1, 0, -1, 0],
                       [0, -1, 0, -1, 0, -1, 0, -1],
                       [-1, 0, -1, 0, -1, 0, -1, 0]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('E2', 'C4')
        game.request(move)
        check_board = [[0, 1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1, 0],
                       [0, 0, 0, -1, 0, 1, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, -1, 0, -1, 0],
                       [0, -1, 0, -1, 0, -1, 0, -1],
                       [-1, 0, -1, 0, -1, 0, -1, 0]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('B3', 'D5')
        game.request(move)
        check_board = [[0, 1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, -1, 0, -1, 0],
                       [0, -1, 0, -1, 0, -1, 0, -1],
                       [-1, 0, -1, 0, -1, 0, -1, 0]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('G2', 'F3')
        game.request(move)
        check_board = [[0, 1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, -1, 0, -1, 0, -1, 0],
                       [0, 0, 0, -1, 0, -1, 0, -1],
                       [-1, 0, -1, 0, -1, 0, -1, 0]]
        self.assertEqual(game.transposition_board(), check_board)

    def test_ending_win(self):
        new_white_pawn = NewWhitePawn()
        new_black_pawn = NewBlackPawn()
        game = Checkers(WhiteMove())
        game.transition_to(BlackMove())
        game.board_state = [[None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, new_white_pawn.create_pawn(), None, None, None, None, None, None],
                            [new_black_pawn.create_pawn(), None, new_black_pawn.create_pawn(), None,
                             new_black_pawn.create_pawn(), None, new_black_pawn.create_pawn(), None],
                            [None, new_black_pawn.create_pawn(), None, new_black_pawn.create_pawn(), None,
                             new_black_pawn.create_pawn(), None, new_black_pawn.create_pawn()],
                            [new_black_pawn.create_pawn(), None, new_black_pawn.create_pawn(), None,
                             new_black_pawn.create_pawn(), None, new_black_pawn.create_pawn(), None]]

        move = Move('F1', 'D3')
        game.request(move)
        check_board = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, -1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, -1, 0, -1, 0, -1, 0],
                       [0, -1, 0, -1, 0, -1, 0, -1],
                       [-1, 0, -1, 0, -1, 0, -1, 0]]
        self.assertEqual(game.transposition_board(), check_board)
        self.assertEqual(type(game._state).__name__, 'EndGame')

    def test_ending_draw(self):
        new_white_king = NewWhiteKing()
        new_black_king = NewBlackKing()
        game = Checkers(WhiteMove())
        game.board_state = [[new_white_king.create_pawn(), None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, new_black_king.create_pawn(), None]]
        game.amount_kings_moves = 29
        move = Move('A1', 'B2')
        game.request(move)
        check_board = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 2, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, -2, 0]]
        self.assertEqual(game.transposition_board(), check_board)
        self.assertEqual(type(game._state).__name__, 'EndGame')

    def test_new_king(self):
        new_white_pawn = NewWhitePawn()
        new_black_pawn = NewBlackPawn()
        new_white_king = NewWhiteKing()
        new_black_king = NewBlackKing()
        game = Checkers(WhiteMove())
        game.board_state = [[None, None, None, None, None, None, None, None],
                            [None, None, new_white_king.create_pawn(), None, new_black_pawn.create_pawn(), None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, new_black_king.create_pawn(), None]]
        game.transition_to(BlackMove())
        move = Move('B5', 'A4')
        game.request(move)
        check_board = [[0, 0, 0, -2, 0, 0, 0, 0],
                       [0, 0, 2, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, -2, 0]]
        self.assertEqual(game.transposition_board(), check_board)

    def test_king_move(self):
        new_black_pawn = NewBlackPawn()
        new_white_king = NewWhiteKing()
        new_black_king = NewBlackKing()
        game = Checkers(WhiteMove())
        game.board_state = [[None, None, None, None, None, None, None, None],
                            [None, None, new_white_king.create_pawn(), None, new_black_pawn.create_pawn(), None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, new_white_king.create_pawn(), None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, new_black_king.create_pawn(), None]]
        game.transition_to(BlackMove())
        move = Move('B5', 'A4')
        game.request(move)
        move = Move('E2', 'D3')
        game.request(move)
        check_board = [[0, 0, 0, -2, 0, 0, 0, 0],
                       [0, 0, 2, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 2, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, -2, 0]]
        self.assertEqual(game.transposition_board(), check_board)

    def test_king_capture(self):
        new_black_pawn = NewBlackPawn()
        new_white_king = NewWhiteKing()
        new_black_king = NewBlackKing()
        game = Checkers(WhiteMove())
        game.board_state = [[None, None, None, None, None, None, None, None],
                            [None, None, new_white_king.create_pawn(), None, new_black_pawn.create_pawn(), None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, new_white_king.create_pawn(), None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, None, None],
                            [None, None, None, None, None, None, new_black_king.create_pawn(), None]]
        game.transition_to(BlackMove())
        move = Move('B5', 'A4')
        game.request(move)
        move = Move('E2', 'D3')
        game.request(move)
        move = Move('A4', 'C2')
        game.request(move)
        check_board = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, -2, 0, 0, 0, 0, 0, 0],
                       [0, 0, 2, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, -2, 0]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('C2', 'D1')
        game.request(move)
        check_board = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, -2, 0, 0, 0, 0, 0, 0],
                       [0, 0, 2, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, -2, 0]]
        self.assertEqual(game.transposition_board(), check_board)
        move = Move('C2', 'E4')
        game.request(move)
        check_board = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, -2, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, -2, 0]]
        self.assertEqual(game.transposition_board(), check_board)
        self.assertEqual(type(game._state).__name__, 'EndGame')

    def test_move(self):
        move = Move('A1', 'B2')
        self.assertEqual(move.x, [0, 0])
        self.assertEqual(move.y, [1, 1])
