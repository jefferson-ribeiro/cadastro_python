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
    def __init__(self, codigo, cliente, produto, quantidade):
        self.codigo = codigo
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = self.quantidade * self.produto.valor
