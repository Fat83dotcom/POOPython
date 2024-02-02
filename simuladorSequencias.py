from itertools import combinations
from math import factorial


class ComparatorNumbers:
    def __init__(
        self, init: int, finish: int, sequenceComparator
    ) -> None:
        self.__n = finish
        self.__k = len(sequenceComparator)
        self.__numbers = range(init, finish)
        self.__sena: list = [
            (n, sequence)
            for n, sequence in enumerate(
                combinations(self.__numbers, self.__k)
            )
            if sequence == tuple(sequenceComparator)
        ]

    @property
    def sena(self) -> list:
        return self.__sena

    def __repr__(self) -> str:
        if len(self.__sena) > 0:
            return f'A posição da sequencia {self.sena[0][1]} -> '\
                f'{self.sena[0][0]} de {self.totalNumberCombinations()}.'
        else:
            return f'{self.sena}'

    def totalNumberCombinations(self) -> int:
        return int(factorial(self.__n - 1) / (
            factorial(self.__k) * factorial((self.__n - 1) - self.__k)
        ))


if __name__ == '__main__':
    game = sorted([24, 56, 33, 48, 21, 41])
    print(game)
    gen = ComparatorNumbers(1, 60, game)
    print(gen)
    print('Terminou.')
