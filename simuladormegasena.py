from itertools import combinations
from math import factorial


class ComparatorNumbers:
    def __init__(
        self, init: int, finish: int, k: int, gameComparator: tuple
    ) -> None:
        self.__n = finish
        self.__k = k
        self.__number = range(init, finish)
        self.__sena: list = []
        for x, game in enumerate(combinations(self.__number, self.__k)):
            if game == gameComparator:
                self.__sena.append(x)
                self.__sena.append(game)
                break

    @property
    def sena(self) -> list:
        return self.__sena

    @property
    def possibilities(self) -> int:
        return self.__numberPossibilities

    def __repr__(self) -> str:
        return f'{self.__sena}'

    def totalNumberCombinations(self) -> int:
        return int(factorial(self.__n - 1) / (
            factorial(self.__k) * factorial((self.__n - 1) - self.__k)
        ))


if __name__ == '__main__':
    game: tuple = (21, 24, 33, 41, 48, 56)
    gen = ComparatorNumbers(1, 61, 6, game)
    print(gen.sena)
    print(gen.totalNumberCombinations())
    print('Terminou.')
