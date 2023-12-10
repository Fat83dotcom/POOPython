from abc import ABC, abstractmethod
from time import sleep
from random import randint
import datetime


class Pagamento(ABC):
    ''' Abstract Product'''
    def __init__(self, valorPagamento, data) -> None:
        self.__valorPagamento = valorPagamento
        self.__dataPedido = data
        self.__status = False

    @property
    def valor(self):
        return self.__valorPagamento

    @property
    def data(self):
        return self.__dataPedido

    @property
    def valorPagamento(self):
        return self.__valorPagamento

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if isinstance(value, bool):
            self.__status = value
        else:
            raise AttributeError(f'{value} não é uma instância de bool()')

    @abstractmethod
    def enviarPagamento(self): ...

    def statusPagamento(self) -> bool:
        if self.status:
            print('Pagamento Aprovado!')
        else:
            print('Pagamento Não Aprovado!')
        return self.status


class PagSeguro(Pagamento):
    ''' Concrete Product'''
    def __init__(self, valorPagamento, data) -> None:
        super().__init__(valorPagamento, data)

    def enviarPagamento(self):
        print(f'Processando Pagamento Pag Seguro: R$ {self.valorPagamento}')
        print(f'Data Pagamento: {self.data}')
        sleep(1)
        status = randint(0, 1)
        if status:
            self.status = True


class Pix(Pagamento):
    ''' Concrete Product '''
    def __init__(self, valorPagamento, data) -> None:
        super().__init__(valorPagamento, data)

    def enviarPagamento(self):
        print(f'Processando Pagamento Pix: R$ {self.valorPagamento}')
        print(f'Data Pagamento: {self.data}')
        sleep(1)
        status = randint(0, 1)
        if status:
            self.status = True


class CartaoCredito(Pagamento):
    juros = 7

    def __init__(self, valorPagamento, data, numeroCartao, qtdParcelas: int):
        super().__init__(valorPagamento, data)
        self.numeroCartao = numeroCartao
        self.qtdParcelas = qtdParcelas

    def valorParcelas(self) -> float:
        vParcela = (self.valor / self.qtdParcelas)
        vParcelaJuros = vParcela + (vParcela * (self.juros / 100))
        return round(vParcelaJuros, 2)

    def valorTotal(self) -> float:
        return round((self.valorParcelas() * self.qtdParcelas), 2)

    def enviarPagamento(self):
        print(
            f'Processando Pagamento Cartão Crédito: R$ {self.valorPagamento}'
        )
        print(f'Número do cartão: {self.numeroCartao}')
        print(f'Número Parcelas: {self.qtdParcelas} X')
        print(
            f'Valor das parcelas(acresc.{self.juros}%): {self.valorParcelas()}'
        )
        print(f'Valor total com juros: {self.valorTotal()}')
        print(f'Data Pagamento: {self.data}')
        status = randint(0, 1)
        if status:
            self.status = True


class GerenciadorPagamento(ABC):
    ''' Creator '''
    def __init__(self) -> None:
        pass

    def pagar(self, valor, data):
        pag = self.processarPagamento(valor, data)
        return pag

    @abstractmethod
    def processarPagamento(self, valor, data) -> bool: ...


class PagarComPagSeguro(GerenciadorPagamento):
    ''' Concrete Creator '''
    def processarPagamento(self, valor, data) -> bool:
        pagSeg = PagSeguro(valor, data)
        pagSeg.enviarPagamento()
        return pagSeg.statusPagamento()


class PagarComPix(GerenciadorPagamento):
    ''' Concrete Creator '''
    def processarPagamento(self, valor, data) -> bool:
        pagPix = Pix(valor, data)
        pagPix.enviarPagamento()
        return pagPix.statusPagamento()


class PagarComCartaoCred(GerenciadorPagamento):
    ''' Concrete Creator '''
    def __init__(self, numeroCartao, qtdParcelas) -> None:
        super().__init__()
        self.numeroCartao = numeroCartao
        self.qtdParcelas = qtdParcelas

    def processarPagamento(self, valor, data) -> bool:
        pagCard = CartaoCredito(
            valor, data, self.numeroCartao, self.qtdParcelas
        )
        pagCard.enviarPagamento()
        return pagCard.statusPagamento()


if __name__ == '__main__':
    valor = 10000
    data = datetime.date.today()
    pix = PagarComPix()
    pag = PagarComPagSeguro()
    pagCard = PagarComCartaoCred('5412654898845', 15)
    pix.pagar(valor, data)
    pag.pagar(valor, data)
    pagCard.pagar(valor, data)
