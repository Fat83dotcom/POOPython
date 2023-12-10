from faker import Faker
from random import randint


def preFix(preFix: str):
    pre = preFix

    def concat(suFix: str):
        nonlocal pre
        pre += f' {suFix}'
        return pre

    return concat


if __name__ == '__main__':

    f = Faker(locale='pt_BR')
    for n in range(200):
        rand = randint(1, 9999)
        Faker.seed(n + rand)
        nome = f.first_name()
        sobreNome = f.last_name()
        conc = preFix(nome)
        nomeCompleto = conc(sobreNome)
        print(nomeCompleto)
