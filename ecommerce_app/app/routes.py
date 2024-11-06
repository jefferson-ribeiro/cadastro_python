from app import app, db
from flask import redirect, render_template, request, flash, url_for
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
    nome = request.form.get('nomeCompleto')
    telefone = request.form.get('telefone')
    cpf = request.form.get('cpf')
    email = request.form.get('email')
    
    cursor = db.cursor()
    cursor.execute("INSERT INTO clientes (nome, telefone, cpf, email) VALUES (%s, %s, %s, %s)",
                   (nome, telefone, cpf, email))
    db.commit()
    return redirect(url_for('cliente'))

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

@app.route('/show_clientes')
def show_clientes():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    return render_template('clientes.html', clientes=clientes)

@app.route('/show_produtos')
def show_produtos():
    return render_template('produtos.html', produtos=produtos)

@app.route('/show_pedidos')
def show_pedidos():
    return render_template('pedidos.html', pedidos=pedidos)