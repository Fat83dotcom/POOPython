from abc import ABC, abstractmethod


class Veicle(ABC):
    @abstractmethod
    def callVeicle(self): ...


class VeicleLux(Veicle):
    def callVeicle(self):
        return 'Veiculo de Luxo.'


class VeiclePop(Veicle):
    def callVeicle(self):
        return 'Veiculo Popular.'


