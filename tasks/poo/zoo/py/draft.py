from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def apresentar_nome(self):
        return f"Eu sou {self.nome}!"

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
    
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        return "miau"

    def mover(self):
        return "ataque ferozmente fofo"

class Égua(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        return "nirrrr"

    def mover(self):
        return "pocoto pocoto pocoto"

def apresentar(animal: Animal):
        print(animal.apresentar_nome())
        print("Som:", animal.fazer_som())
        print("Movimento:", animal.mover())
        print("Tipo:", type(animal).__name__)
        print("-----------")

t = Tartaruga("Michelangelo")
g = Gato("Vitin")
e = Égua("Éguinha Pocotó")

lista = [t, g, e]

for animal in lista:
    apresentar(animal)
