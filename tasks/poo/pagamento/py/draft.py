from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao

    def resumo(self):
        print(f"Pagamento de R$ {self.valor}: {self.descricao}")

    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("O valor do pagamento deve ser maior que zero")

    @abstractmethod
    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor, descricao, numero, nome_titular, limite_disponivel):
        super().__init__(valor, descricao)
        self.numero = numero
        self.nome_titular = nome_titular
        self.limite_disponivel = limite_disponivel

    def processar(self):
        self.validar_valor()
        if self.valor > self.limite_disponivel:
            return f"Erro: Limite insuficiente no cartão {self.numero}"
        self.limite_disponivel -= self.valor
        return f"Pagamento aprovado no cartão {self.nome_titular}. Limite restante: {self.limite_disponivel}"

class Pix(Pagamento):
    def __init__(self, valor, descricao, banco, chave):
        super().__init__(valor, descricao)
        self.banco = banco
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

carrinho = [
    Pix(150.0, "Camisa esportiva", "Banco XPTO", "email@ex.com"),
    CartaoCredito(400.0, "Tênis esportivo", "1111 2222 3333 4444", "Cliente X", 500.0),
    Boleto(89.9, "Livro de Python", "12345678900", "10/12/2025"),
    CartaoCredito(800.0, "Notebook", "9999 8888 7777 6666", "Cliente Y", 300)
]

for pagamento in carrinho:
    processar_pagamento(pagamento)
    print()
    