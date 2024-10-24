class Cliente:
    def __init__(self, codigo, nome, telefone, cpf, email):
        self.codigo = codigo
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email

class Produto:
    def __init__(self, codigo, nome, descricao, valor):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Pedido:
    def __init__(self, codigo, cliente, produtos):
        self.codigo = codigo
        self.cliente = cliente
        self.produtos = produtos  # Lista de tuplas (produto, quantidade)
        self.valor_total = self.calcular_valor_total()

    def calcular_valor_total(self):
        total = 0
        for produto, quantidade in self.produtos:
            total += produto.valor * quantidade
        return total