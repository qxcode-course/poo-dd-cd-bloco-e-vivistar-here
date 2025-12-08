from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def apresentar_nome(self):
        return f"Eu sou um(a) {self.nome}!"

    @abstractmethod

    def fazer_som(self):
        pass

    @abstractmethod

    def mover(self):
        pass

class Tartaruga(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        return "cowabunga!"

    def mover(self):
        return "Move-se nas sombras."

t = Tartaruga("Michelangelo")
print(t.apresentar_nome())
print(t.fazer_som())
print(t.mover())