from abc import ABC, abstractmethod


class Pawn(ABC):
    def __init__(self, up: bool, down: bool):
        self.down = 0
        self.up = 0
        if up:
            self.up = -1
        if down:
            self.down = 1

    @property
    def moving(self):
        return [self.down, self.up]


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
