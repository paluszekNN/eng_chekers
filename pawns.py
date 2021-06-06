from abc import ABC, abstractmethod


class Pawn(ABC):
    @abstractmethod
    def move(self, new_position):
        pass


class WhitePawn(Pawn):
    def __init__(self, position):
        self.position = position

    def move(self, new_position):
        self.position = new_position


class BlackPawn(Pawn):
    def __init__(self, position):
        self.position = position

    def move(self, new_position):
        self.position = new_position


class King(ABC):
    @abstractmethod
    def move(self, new_position):
        pass


class WhiteKing(King):
    def __init__(self, position):
        self.position = position

    def move(self, new_position):
        self.position = new_position


class BlackKing(King):
    def __init__(self, position):
        self.position = position

    def move(self, new_position):
        self.position = new_position


class NewPawn(ABC):
    @abstractmethod
    def create_pawn(self, position) -> Pawn:
        pass


class NewKing(ABC):
    @abstractmethod
    def create_king(self, position) -> King:
        pass


class NewWhitePawn(NewPawn):
    def create_pawn(self, position) -> Pawn:
        return WhitePawn(position)


class NewBlackPawn(NewPawn):
    def create_pawn(self, position) -> Pawn:
        return BlackPawn(position)


class NewWhiteKing(NewKing):
    def create_king(self, position) -> King:
        return WhiteKing(position)


class NewBlackKing(NewKing):
    def create_king(self, position) -> King:
        return BlackKing(position)
