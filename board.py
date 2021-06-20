from __future__ import annotations
from abc import ABC, abstractmethod
from pawns import NewBlackKing, NewBlackPawn, NewWhitePawn, NewWhiteKing


class Move:
    def __init__(self, x, y):
        transform_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, '1': 0, '2': 1, '3': 2,
                            '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
        if x[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] and x[1] in ['1', '2', '3', '4', '5', '6', '7', '8']:
            self.x = [transform_to_num[x[0]], transform_to_num[x[1]]]
        else:
            print('Wrong move')
        if y[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] and y[1] in ['1', '2', '3', '4', '5', '6', '7', '8']:
            self.y = [transform_to_num[y[0]], transform_to_num[y[1]]]
        else:
            print('Wrong move')


class Checkers:
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)
        self.board_state = []
        self.amount_kings_moves = 0
        self.new_white_pawn = NewWhitePawn()
        self.new_black_pawn = NewBlackPawn()
        self.new_white_king = NewWhiteKing()
        self.new_black_king = NewBlackKing()
        self.reset()

    def reset(self):
        self.amount_kings_moves = 0
        for row in range(3):
            self.board_state.append([])
            for col in range(8):
                if (row + col) % 2 == 0:
                    self.board_state[row].append(None)
                else:
                    self.board_state[row].append(self.new_white_pawn.create_pawn())

        for row in range(3, 5):
            self.board_state.append([])
            for col in range(8):
                self.board_state[row].append(None)

        for row in range(5, 8):
            self.board_state.append([])
            for col in range(8):
                if (row + col) % 2 == 0:
                    self.board_state[row].append(None)
                else:
                    self.board_state[row].append(self.new_black_pawn.create_pawn())
        self.transition_to(WhiteMove())

    def transition_to(self, state: State):
        self._state = state
        self._state.context = self

    def request(self, move: Move):
        if self._state.move(move):
            if self.amount_kings_moves>=30:
                print('DRAW')
                self.transition_to(EndGame())
            else:
                self.transition_to(WhiteMove()if 'Black' in str(self._state) else BlackMove())
                self.make_new_kings()
                check_winner = 'Black' if 'Black' in str(self._state) else 'White'
                is_capable_of_move = False
                if self.check_captures():
                    is_capable_of_move = True
                for row in range(8):
                    if is_capable_of_move:
                        break
                    for col in range(8):
                        if check_winner in str(self.board_state[row][col]):
                            for move in self.get_moves(row,col).values():
                                if not self.board_state[move[0]][move[1]]:
                                    is_capable_of_move = True
                                    break
                if not is_capable_of_move:
                    self.transition_to(EndGame())
                    print('White wins' if 'Black' in check_winner else 'Black wins')

    def transposition_board(self):
        state = []
        for row in range(8):
            state.append([])
            for col in range(8):
                if not self.board_state[row][col]:
                    state[-1].append(0)
                elif type(self.board_state[row][col]).__name__ == 'WhitePawn':
                    state[-1].append(1)
                elif type(self.board_state[row][col]).__name__ == 'BlackPawn':
                    state[-1].append(-1)
                elif type(self.board_state[row][col]).__name__ == 'WhiteKing':
                    state[-1].append(2)
                elif type(self.board_state[row][col]).__name__ == 'BlackKing':
                    state[-1].append(-2)
        return state

    def get_moves(self, row, col):
        moves = {}
        if self.board_state[row][col].down:
            moves['move'] = [self.board_state[row][col].down, 1]
            moves['move2'] = [self.board_state[row][col].down, -1]
        if self.board_state[row][col].up:
            moves['move3'] = [self.board_state[row][col].up, 1]
            moves['move4'] = [self.board_state[row][col].up, -1]
        if row == 0:
            if 'move4' in moves.keys():
                moves.pop('move4')
            if 'move3' in moves.keys():
                moves.pop('move3')
        elif row == 7:
            if 'move' in moves.keys():
                moves.pop('move')
            if 'move2' in moves.keys():
                moves.pop('move2')
        if col == 0:
            if 'move2' in moves.keys():
                moves.pop('move2')
            if 'move4' in moves.keys():
                moves.pop('move4')
        if col == 7:
            if 'move' in moves.keys():
                moves.pop('move')
            if 'move3' in moves.keys():
                moves.pop('move3')
        return  moves

    def check_captures(self):
        opponent = 'Black' if 'White' in str(self._state) else 'White'
        for row in range(8):
            for col in range(8):
                if self.board_state[row][col] and not opponent in str(self.board_state[row][col]):
                    moves = self.get_moves(row, col)
                    for move in moves.values():
                        if self.board_state[row+move[0]][col+move[1]] and opponent in str(self.board_state[row+move[0]][col+move[1]]):
                            try:
                                if not self.board_state[row+2*move[0]][col+2*move[1]] and row+2*move[0] >= 0 and col+2*move[1]>=0 and row+2*move[0] <= 7 and col+2*move[1] <= 7:
                                    return True
                            except:
                                pass
        return False

    def make_new_kings(self):
        for col in range(8):
            if 'WhitePawn' in str(self.board_state[7][col]):
                self.board_state[7][col] = self.new_white_king.create_pawn()
            if 'BlackPawn' in str(self.board_state[0][col]):
                self.board_state[0][col] = self.new_black_king.create_pawn()


class State(ABC):
    @property
    def context(self) -> Checkers:
        return self._context

    @context.setter
    def context(self, context: Checkers) -> None:
        self._context = context

    @abstractmethod
    def move(self, move: Move) -> bool:
        pass


class WhiteMove(State):
    def move(self, move: Move) -> bool:
        opponent = 'Black'
        if type(self.context.board_state[move.x[0]][move.x[1]]).__name__ in ['WhitePawn', 'WhiteKing'] and self.context.board_state[move.y[0]][move.y[1]] == None:
            if self.context.check_captures() and [(move.y[0]-move.x[0])//2, (move.y[1]-move.x[1])//2] in self.context.get_moves(move.x[0],move.x[1]).values():
                for a_move in self.context.get_moves(move.x[0],move.x[1]).values():
                    if self.context.board_state[move.x[0]+ a_move[0]][move.x[1] + a_move[1]] and opponent in str(self.context.board_state[move.y[0] - a_move[0]][move.y[1]- a_move[1]]):
                        try:
                            if not self.context.board_state[move.x[0]+ 2*a_move[0]][move.x[1] + 2*a_move[1]] and move.x[0] + 2 * a_move[0] >= 0 and move.x[1]+2*a_move[1]>=0:
                                if not'King' in str(self.context.board_state[move.x[0]][move.x[1]]):
                                    self.context.amount_kings_moves = 0
                                self.context.board_state[move.y[0]][move.y[1]] = self.context.board_state[move.x[0]][move.x[1]]
                                self.context.board_state[move.x[0]+a_move[0]][move.x[1]+a_move[1]] = None
                                self.context.board_state[move.x[0]][move.x[1]] = None
                                if self.context.check_captures():
                                    return False
                                else:
                                    return True
                        except:
                            pass
            elif [move.y[0]-move.x[0], move.y[1]-move.x[1]] in self.context.get_moves(move.x[0],move.x[1]).values()and not self.context.check_captures():
                if 'King' in str(self.context.board_state[move.x[0]][move.x[1]]):
                    self.context.amount_kings_moves+=1
                else:
                    self.context.amount_kings_moves = 0

                self.context.board_state[move.y[0]][move.y[1]] = self.context.board_state[move.x[0]][move.x[1]]
                self.context.board_state[move.x[0]][move.x[1]] = None
                return True
        return False


class BlackMove(State):
    def move(self, move: Move) -> bool:
        opponent = 'White'
        if type(self.context.board_state[move.x[0]][move.x[1]]).__name__ in ['BlackPawn', 'BlackKing'] and self.context.board_state[move.y[0]][move.y[1]] == None:
            if self.context.check_captures() and [(move.y[0]-move.x[0])//2, (move.y[1]-move.x[1])//2] in self.context.get_moves(move.x[0],move.x[1]).values():
                for a_move in self.context.get_moves(move.x[0],move.x[1]).values():
                    if self.context.board_state[move.x[0]+ a_move[0]][move.x[1] + a_move[1]] and opponent in str(self.context.board_state[move.y[0] - a_move[0]][move.y[1]- a_move[1]]):
                        try:
                            if not self.context.board_state[move.x[0]+ 2*a_move[0]][move.x[1] + 2*a_move[1]] and move.x[0] + 2 * a_move[0] >= 0 and move.x[1]+2*a_move[1]>=0:
                                if not'King' in str(self.context.board_state[move.x[0]][move.x[1]]):
                                    self.context.amount_kings_moves = 0
                                self.context.board_state[move.y[0]][move.y[1]] = self.context.board_state[move.x[0]][move.x[1]]
                                self.context.board_state[move.x[0]+a_move[0]][move.x[1]+a_move[1]] = None
                                self.context.board_state[move.x[0]][move.x[1]] = None
                                if self.context.check_captures():
                                    return False
                                else:
                                    return True
                        except:
                            pass
            elif [move.y[0]-move.x[0], move.y[1]-move.x[1]] in self.context.get_moves(move.x[0],move.x[1]).values()and not self.context.check_captures():
                if 'King' in str(self.context.board_state[move.x[0]][move.x[1]]):
                    self.context.amount_kings_moves+=1
                else:
                    self.context.amount_kings_moves = 0
                self.context.board_state[move.y[0]][move.y[1]] = self.context.board_state[move.x[0]][move.x[1]]
                self.context.board_state[move.x[0]][move.x[1]] = None
                return True
        return False


class EndGame(State):
    def move(self, move=None) -> bool:
        if move:
            self.context.reset()
        return False


if __name__ == '__main__':
    game = Checkers(WhiteMove())
    print(game.board_state)

    move = Move('C2', 'D3')
    game.request(move)
    move = Move('F1', 'E2')
    game.request(move)
    move = Move('D3', 'E4')
    game.request(move)
    move = Move('D3', 'F1')
    game.request(move)
    move = Move('F3', 'E2')
    game.request(move)
    move = Move('C4', 'D3')
    game.request(move)
    move = Move('E2', 'D1')
    game.request(move)
    move = Move('E2', 'C4')
    game.request(move)

    new_white_pawn = NewWhitePawn()
    new_black_pawn = NewBlackPawn()
    game = Checkers(WhiteMove())
    game.transition_to(BlackMove())
    game.board_state = [[None, None, None, None, None, None, None, None],
                        [None, None, new_black_pawn.create_pawn(), None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, new_white_pawn.create_pawn(), None, None, None, None, None, None],
                        [None, None, None, None, new_black_pawn.create_pawn(), None, new_black_pawn.create_pawn(), None],
                        [None, new_black_pawn.create_pawn(), None, new_black_pawn.create_pawn(), None,
                         new_black_pawn.create_pawn(), None, new_black_pawn.create_pawn()],
                        [new_black_pawn.create_pawn(), None, new_black_pawn.create_pawn(), None,
                         new_black_pawn.create_pawn(), None, new_black_pawn.create_pawn(), None]]

    move = Move('B3', 'A2')
    game.request(move)