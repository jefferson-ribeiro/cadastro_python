from app import app
from flask import render_template, request
from app.models import Cliente, Produto, Pedido

clientes = []
produtos = []
pedidos = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cliente')
def cliente():
    return render_template('cliente_form.html')

@app.route('/produto')
def produto():
    return render_template('produto_form.html')

@app.route('/pedido')
def pedido():
    return render_template('pedido_form.html')

@app.route('/submit_cliente', methods=['POST'])
def submit_cliente():
    nome = request.form.get('name')
    telefone = request.form.get('telefone')
    cpf = request.form.get('cpf')
    email = request.form.get('email')
    codigo = len(clientes) + 1
    cliente = Cliente(codigo, nome, telefone, cpf, email)
    clientes.append(cliente)
    return f"Cadastrado com sucesso! Nome: {nome}, Telefone: {telefone}, CPF: {cpf}, Email: {email}"

@app.route('/submit_produto', methods=['POST'])
def submit_produto():
    nome = request.form.get('name')
    descricao = request.form.get('descricao')
    valor = float(request.form.get('valor'))
    codigo = len(produtos) + 1
    produto = Produto(codigo, nome, descricao, valor)
    produtos.append(produto)
    return f"Produto cadastrado com sucesso! Nome: {nome}, Descrição: {descricao}, Valor: {valor}"

@app.route('/submit_pedido', methods=['POST'])
def submit_pedido():
    codigo_cliente = int(request.form.get('cliente'))
    codigo_produto = int(request.form.get('produto'))
    quantidade = int(request.form.get('quantidade'))
    
    cliente = next((cli for cli in clientes if cli.codigo == codigo_cliente), None)
    produto = next((prod for prod in produtos if prod.codigo == codigo_produto), None)
    
    if not cliente or not produto:
        return "Cliente ou Produto não encontrado."

    codigo_pedido = len(pedidos) + 1
    pedido = Pedido(codigo_pedido, cliente, [(produto, quantidade)])
    pedidos.append(pedido)
    return f"Pedido cadastrado com sucesso! Cliente: {cliente.nome}, Produto: {produto.nome}, Quantidade: {quantidade}"