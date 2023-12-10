from abc import ABC, abstractmethod


class Burger(ABC):
    ''' Abstrct Product '''
    @abstractmethod
    def prepare(self): ...


class BeefBurger(Burger):
    ''' Concrete Product '''
    def prepare(self):
        return 'Burger Beef Pronto'


class VeganBurger(Burger):
    ''' Concrete Product '''
    def prepare(self):
        return 'Burger Vegan Pronto'


class Restaurant():
    ''' Creator '''
    def __init__(self) -> None:
        pass

    def orderBurger(self):
        burger = self.createBurger()
        return burger

    def createBurger(self): ...
    '''Factory Method'''


class BeefBurgerRestaurant(Restaurant):
    ''' Concrete Creator '''
    def createBurger(self):
        return BeefBurger.prepare(self)


class VeganBurgerRestaurant(Restaurant):
    ''' Concrete Creator '''
    def createBurger(self):
        return VeganBurger.prepare(self)


if __name__ == '__main__':

    veg = VeganBurgerRestaurant()
    bef = BeefBurgerRestaurant()
    print(veg.orderBurger())
    print(bef.orderBurger())
