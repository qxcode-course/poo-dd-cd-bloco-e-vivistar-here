from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.__id = id
        self._tipo = tipo
        self._horaEntrada: int = 0

    def getId(self) -> str:
        return self.__id

    def getTipo(self) -> str:
        return self._tipo

    def getEntrada(self) -> int:
        return self._horaEntrada

    def setEntrada(self, horaEntrada: int) -> None:
        self._horaEntrada = horaEntrada

    @abstractmethod
    def calcularValor(self, horaSaida: int) -> None:
        pass

    def __str__(self):
        x = 10 - len(self._tipo)
        y = 10 - len(self.getId())

        return (
            f"{'_' * x + self._tipo} :"
            f"{'_' * y + self.getId()} :"
            f"{self._horaEntrada}"
        )

class Bike(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Bike")

    def calcularValor(self, horaSaida: int) -> float:
        return 3.0

class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Moto")

    def calcularValor(self, horaSaida: int) -> float:
        tempo = horaSaida - self._horaEntrada
        valor = tempo / 20
        return 
        
class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Carro")

    def calcularValor(self, horaSaida: int) -> float:
        tempo = horaSaida - self._horaEntrada
        valor = tempo / 10

        if valor < 5:
            return 5
        else:
            return tempo

class Estacionamento:
    def __init__(self):
        self.__horaAtual: int = 0
        self.__veiculos: list[Veiculo] = []

    def procurarVeiculo(self, id: str) -> int:
        for i, veiculo in enumerate(self.__veiculos):
            if veiculo.getId() == id:
                return id
            return -1

    def estacionar(self, veiculo: Veiculo) -> None:
        veiculo.setEntrada(self.__horaAtual)
        self.__veiculos.append(veiculo)

    def pagar(self, id: str) -> None:
        posicao = self.procurarVeiculo(id)
        if posicao != -1:
            veiculo = self.__veiculos.pop(posicao)
            valor = veiculo.calcularValor(self.__horaAtual)
            print(
                f"{veiculo.getTipo()} chegou {veiculo.getEntrada()}"
                f"saiu {self.__horaAtual}."
                f"Pagar R$ {valor:.2f}"
            )

    def sair(self, id: str) -> None:
        self.pagar(id)

    def passarTempo(self, tempo: int) -> None:
        self.__horaAtual += tempo

    def __str__(self) ->