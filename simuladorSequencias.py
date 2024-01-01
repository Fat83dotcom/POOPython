from itertools import combinations
from math import factorial


class ComparatorNumbers:
    def __init__(
        self, init: int, finish: int, sequenceComparator: tuple
    ) -> None:
        self.__n = finish
        self.__k = len(sequenceComparator)
        self.__numbers = range(init, finish)
        self.__sena: list = [
            (n, sequence)
            for n, sequence in enumerate(combinations(self.__numbers, self.__k))
            if sequence == sequenceComparator
        ]

    @property
    def sena(self) -> list:
        return self.__sena

    def __repr__(self) -> str:
        return f'A posição da sequencia {self.sena[0][1]} -> '\
            f'{self.sena[0][0]} de {self.totalNumberCombinations()}.'

    def totalNumberCombinations(self) -> int:
        return int(factorial(self.__n - 1) / (
            factorial(self.__k) * factorial((self.__n - 1) - self.__k)
        ))


if __name__ == '__main__':
    game: tuple = (21, 24, 33, 41, 48)
    gen = ComparatorNumbers(1, 61, game)
    print(gen)
    print('Terminou.')
