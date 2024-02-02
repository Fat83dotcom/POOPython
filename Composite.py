from abc import ABC, abstractmethod
from copy import deepcopy


class Element(ABC):
    def __init__(self) -> None:
        self.transferArea: Element

    @abstractmethod
    def copy(self): pass

    @abstractmethod
    def paste(self): pass

    @abstractmethod
    def showContent(self): pass

    def addElement(self, child): pass

    def removeElement(self, child): pass


class Folder(Element):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.__children: list[Element] = []

    def copy(self):
        for child in self.__children:
            child.copy()

    def paste(self):
        for child in self.__children:
            child.paste()

    def showContent(self):
        print(f'\n {self.name}')
        for child in self.__children:
            child.showContent()

    def addElement(self, child: Element):
        self.__children.append(child)

    def removeElement(self, child: Element):
        if child in self.__children:
            self.__children.remove(child)


class File(Element):
    def __init__(self, name: str, content) -> None:
        super().__init__()
        self.name = name
        self.conten = content

    def __str__(self) -> str:
        return f'Name: {self.name} - Content: {self.conten}'

    def copy(self):
        self.transferArea = deepcopy(self)

    def paste(self):
        return self.transferArea

    def showContent(self):
        print(self)


if __name__ == '__main__':
    pasta1 = Folder('pasta 1')
    pasta2 = Folder('pasta 2')

    arquivo1 = File('texto 1', 'Aqui é um arquivo de texto')
    arquivo2 = File('Carta', 'era uma vez...')
    arquivo4 = File('log.txt', 'Aqui tem alguns logs de sistema...')

    pasta1.addElement(arquivo1)
    pasta1.addElement(arquivo2)

    pasta2.addElement(arquivo4)
    pasta2.addElement(pasta1)

    pasta2.showContent()

    arquivo1.copy()
    arquivo3 = arquivo1.paste()

    pasta1.addElement(arquivo3)

    pasta1.showContent()
    pasta2.showContent()
