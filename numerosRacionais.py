class Racional:
    def __init__(self, numerador: int, denominador: int) -> None:
        self.numerador = numerador
        self.denominador = denominador

    @property
    def denominador(self) -> int:
        return self.__denominador

    @property
    def numerador(self) -> int:
        return self.__numerador

    @numerador.setter
    def numerador(self, valor) -> None:
        if isinstance(valor, int):
            self.__numerador = valor
        else:
            raise ValueError('O numerador deve ser um numero inteiro.')

    @denominador.setter
    def denominador(self, valor) -> None:
        if valor != 0 and isinstance(valor, int):
            self.__denominador = valor
        else:
            raise ValueError(
                'O denominador deve ser um inteiro diferente de Zero.'
            )

    def __repr__(self) -> str:
        return f'{self.numerador}/{self.denominador}'

    def inveterSinal(self):
        if self.numerador >= 0 and self.denominador > 0:
            self.numerador = -self.numerador
        elif self.numerador < 0 and self.denominador < 0:
            self.numerador = -self.numerador
            self.denominador = -self.denominador
        elif self.numerador >= 0 and self.denominador < 0:
            self.denominador = -self.denominador
        else:
            self.numerador = -self.numerador

    def __redutorFracao(self, numerador, denominador) -> tuple[int, int]:
        for multiplo in list(range(2, 10)):
            while numerador % multiplo == 0 and denominador % multiplo == 0:
                numerador /= multiplo
                denominador /= multiplo
        return int(numerador), int(denominador)

    def __add__(self, other):
        resultDenominador = self.denominador * other.denominador
        resultNumA = (resultDenominador / self.denominador) * self.numerador
        resultNumB = (resultDenominador / other.denominador) * other.numerador
        numerador_, denominador_ = self.__redutorFracao(
            int((resultNumA + resultNumB)), int(resultDenominador)
        )
        return Racional(numerador_, denominador_)

    def __sub__(self, other):
        resultDenominador = self.denominador * other.denominador
        resultNumA = (resultDenominador / self.denominador) * self.numerador
        resultNumB = (resultDenominador / other.denominador) * other.numerador
        numerador_, denominador_ = self.__redutorFracao(
            int((resultNumA - resultNumB)), int(resultDenominador)
        )
        return Racional(numerador_, denominador_)

    def __mul__(self, other):
        numerador_ = self.numerador * other.numerador
        denominador_ = self.denominador * other.denominador
        numerador_, denominador_ = self.__redutorFracao(
            numerador_, denominador_
        )
        return Racional(numerador_, denominador_)

    def __truediv__(self, other):
        numerador_ = self.numerador * other.denominador
        denominador_ = self.denominador * other.numerador
        numerador_, denominador_ = self.__redutorFracao(
            numerador_, denominador_
        )
        return Racional(numerador_, denominador_)

    def quociente(self) -> float:
        return round(self.numerador / self.denominador, 3)


if __name__ == '__main__':
    r1 = Racional(3, 4)
    r2 = Racional(5, 8)
    r3 = Racional(6, 8)
    r4 = r1 * r1
    r5 = r4 - r3
    r6 = Racional(1, 2)
    r7 = r6 - r1

    print(r4)
    print(r5)
    print(r7)
