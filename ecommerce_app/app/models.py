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
from app import db

class Pedido(db.Model):
    __tablename__ = 'pedidos'

    codigo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.codigo'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.codigo'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Float, nullable=False) # Adiciona o campo valor

    def __init__(self, cliente_id, produto_id, quantidade, valor):
        self.cliente_id = cliente_id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.valor = valor