from app import db

class Cliente(db.Model):
    __tablename__ = 'clientes'

    codigo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, telefone, cpf, email):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email

class Produto(db.Model):
    __tablename__ = 'produtos'

    codigo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=True)
    descricao = db.Column(db.String(255), nullable=True)
    valor = db.Column(db.Float, nullable=True)

    def __init__(self, nome, descricao, valor):
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