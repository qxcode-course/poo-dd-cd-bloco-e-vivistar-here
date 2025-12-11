from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao

    def resumo(self):
        print(f"Pagamento de R$ {self.valor:.2f}: {self.descricao}")

    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("O valor do pagamento deve ser maior que zero")

    @abstractmethod
    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor, descricao, numero, nome_titular, limite_disponivel):
        super().__init__(valor, descricao)
        self.numero: int = numero
        self.nome_titular: str = nome_titular
        self.limite_disponivel = limite_disponivel

    def processar(self):
        self.validar_valor()
        if self.valor > self.limite_disponivel:
            return f"Erro: Limite insuficiente no cartão {self.numero}"
        self.limite_disponivel -= self.valor
        return f"Pagamento aprovado no cartão {self.nome_titular}. Limite restante: {self.limite_disponivel:.2f}"

class Pix(Pagamento):
    def __init__(self, valor, descricao, banco, chave):
        super().__init__(valor, descricao)
        self.banco: str = banco
        self.chave = chave

    def processar(self):
        self.validar_valor()
        return f"PIX enviado via {self.banco} usando chave {self.chave}"

class Boleto(Pagamento):
    def __init__(self, valor, descricao, codigo_barras, vencimento):
        super().__init__(valor, descricao)
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento
    
    def processar(self):
        self.validar_valor()
        return "Boleto gerado. Aguardando pagamento..."

def processar_pagamento(pagamento: Pagamento):
    pagamento.validar_valor()
    pagamento.resumo()
    print(pagamento.processar())