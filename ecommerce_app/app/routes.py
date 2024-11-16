from app import app, db
from flask import jsonify, redirect, render_template, request, flash, url_for
from app.models import Cliente, Produto, Pedido

@app.route('/')
def home():
    clientes = Cliente.query.all()
    produtos = Produto.query.all()
    return render_template('index.html', clientes=clientes, produtos=produtos)

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

    # Criação do cliente sem calcular o 'codigo' manualmente
    novo_cliente = Cliente(nome=nome, telefone=telefone, cpf=cpf, email=email)
    db.session.add(novo_cliente)
    db.session.commit()

    flash("Cliente cadastrado com sucesso!")
    return redirect(url_for('cliente'))

@app.route('/submit_produto', methods=['POST'])
def submit_produto():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    valor = float(request.form.get('valor'))

    novo_produto = Produto(nome=nome, descricao=descricao, valor=valor)
    db.session.add(novo_produto)
    db.session.commit()

    flash("Produto cadastrado com sucesso!")
    return redirect(url_for('produto'))

# @app.route('/submit_pedido', methods=['POST'])
# def submit_pedido():
#     codigo_cliente = int(request.form.get('cliente'))
#     codigo_produto = int(request.form.get('produto'))
#     quantidade = int(request.form.get('quantidade'))
    
#     cliente = next((cli for cli in clientes if cli.codigo == codigo_cliente), None)
#     produto = next((prod for prod in produtos if prod.codigo == codigo_produto), None)
    
#     if not cliente or not produto:
#         return "Cliente ou Produto não encontrado."

#     codigo_pedido = len(pedidos) + 1
#     pedido = Pedido(codigo_pedido, cliente, [(produto, quantidade)])
#     pedidos.append(pedido)
#     return f"Pedido cadastrado com sucesso! Cliente: {cliente.nome}, Produto: {produto.nome}, Quantidade: {quantidade}"

@app.route('/submit_pedido', methods=['POST'])
def submit_pedido():
    cliente_id = int(request.form.get('cliente'))
    produto_id = int(request.form.get('produto'))
    quantidade = int(request.form.get('quantidade'))

    # Buscar o cliente e o produto no banco de dados
    cliente = Cliente.query.get(cliente_id)
    produto = Produto.query.get(produto_id)

    if not cliente or not produto:
        flash("Cliente ou Produto não encontrado.")
        return redirect(url_for('home'))

    # Calcular o valor total do pedido
    valor_total = quantidade * produto.valor

    # Criar o novo pedido com o valor total
    novo_pedido = Pedido(cliente_id=cliente_id, produto_id=produto_id, quantidade=quantidade, valor=valor_total)

    # Adicionar e confirmar no banco de dados
    db.session.add(novo_pedido)
    db.session.commit()

    flash("Pedido cadastrado com sucesso!")
    return redirect(url_for('home'))

@app.route('/show_clientes')
def show_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

@app.route('/show_produtos')
def show_produtos():
    produtos = Produto.query.all()
    return render_template('produtos.html', produtos=produtos)

@app.route('/show_pedidos')
def show_pedidos():
    pedidos = Pedido.query.all()
    pedidos_completos = []

    for pedido in pedidos:
        cliente = Cliente.query.get(pedido.cliente_id)
        produto = Produto.query.get(pedido.produto_id)
        pedidos_completos.append({
            'codigo': pedido.codigo,
            'cliente': cliente.nome,
            'produto': produto.nome,
            'quantidade': pedido.quantidade,
            'valor_unitario': produto.valor,
            'valor_total': pedido.valor
        })    
    return render_template('pedidos.html', pedidos=pedidos_completos)

@app.route('/clientes')
def get_clientes():
    clientes = Cliente.query.all()
    clientes_data = [{'codigo': cliente.codigo, 'nome': cliente.nome} for cliente in clientes]
    return jsonify(clientes_data)

@app.route('/produtos')
def get_produtos():
    produtos = Produto.query.all()
    produtos_data = [{'codigo': produto.codigo, 'nome': produto.nome} for produto in produtos]
    return jsonify(produtos_data)