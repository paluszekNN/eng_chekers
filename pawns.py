from abc import ABC, abstractmethod


class Pawn(ABC):
    def __init__(self, up: bool, down: bool):
        self._down = [None, None]
        self._up = [None, None]
        if up:
            self._up = [-1, -1]
        if down:
            self._down = [1, 1]

    @property
    def moving(self):
        return [self._down, self._up]


class WhitePawn(Pawn):
    def __init__(self):
        super().__init__(False, True)


class BlackPawn(Pawn):
    def __init__(self):
        super().__init__(True, False)


class WhiteKing(Pawn):
    def __init__(self):
        super().__init__(True, True)


class BlackKing(Pawn):
    def __init__(self):
        super().__init__(True, True)


class NewPawn(ABC):
    @abstractmethod
    def create_pawn(self) -> Pawn:
        pass


class NewWhitePawn(NewPawn):
    def create_pawn(self) -> Pawn:
        return WhitePawn()


class NewBlackPawn(NewPawn):
    def create_pawn(self) -> Pawn:
        return BlackPawn()


class NewWhiteKing(NewPawn):
    def create_pawn(self) -> Pawn:
        return WhiteKing()


class NewBlackKing(NewPawn):
    def create_pawn(self) -> Pawn:
        return BlackKing()
