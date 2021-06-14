from __future__ import annotations
from abc import ABC, abstractmethod
from pawns import NewBlackKing, NewBlackPawn, NewWhitePawn, NewWhiteKing


class Move:
    def __init__(self, x, y):
        if x[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] and x[1] in ['1', '2', '3', '4', '5', '6', '7', '8']:
            self.x = x
        if y[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] and y[1] in ['1', '2', '3', '4', '5', '6', '7', '8']:
            self.y = y


class Checkers:
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)
        self.board_state = []
        self.new_white_pawn = NewWhitePawn()
        self.new_black_pawn = NewBlackPawn()
        self.new_white_king = NewWhiteKing()
        self.new_black_king = NewBlackKing()

        for row in range(3):
            self.board_state.append([])
            for col in range(8):
                if (row + col) % 2 == 0:
                    self.board_state[row].append(None)
                else:
                    self.board_state[row].append(self.new_white_pawn.create_pawn())

        for row in range(3,5):
            self.board_state.append([])
            for col in range(8):
                self.board_state[row].append(None)

        for row in range(5,8):
            self.board_state.append([])
            for col in range(8):
                if (row + col) % 2 == 0:
                    self.board_state[row].append(None)
                else:
                    self.board_state[row].append(self.new_black_pawn.create_pawn())

    def transition_to(self, state: State):
        self._state = state
        self._state.context = self

    def request(self, move: Move):
        self._state.move(move)


class State(ABC):
    @property
    def context(self) -> Checkers:
        return self._context

    @context.setter
    def context(self, context: Checkers) -> None:
        self._context = context

    @abstractmethod
    def move(self, move: Move) -> None:
        pass


class WhiteMove(State):
    def move(self, move: Move) -> None:
        # self.context.transition_to(ConcreteStateB())
        pass


class BlackMove(State):
    def move(self, move: Move) -> None:
        print("ConcreteStateB handles request1.")


class EndGame(State):
    def move(self, move: Move) -> None:
        print("ConcreteStateB handles request1.")


if __name__ == '__main__':
    game = Checkers(WhiteMove())
    print(game.board_state)
