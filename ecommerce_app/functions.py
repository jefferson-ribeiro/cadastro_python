import time
import models as m

# Inicializa as listas para armazenar dados
clientes = []
produtos = []
pedidos = []

def boasvindas():
    print('╔═════════════════════════════════╗')
    print('║   Bem-vindo ao E-Shop Brasil    ║')
    print('║     Tecnologia e Inovação       ║')
    print('╚═════════════════════════════════╝')
    time.sleep(2)
    
def menu():
        print('╔═══════════════════════════════════════════╗')
        print('║               MENU PRINCIPAL              ║')
        print('╠═══════════════════════════════════════════╣')
        print('║ 1. Cadastrar Cliente                      ║')
        print('║ 2. Cadastrar Produto                      ║')
        print('║ 3. Realizar Pedido                        ║')
        print('║ 4. Mostrar Clientes                       ║')
        print('║ 5. Mostrar Produtos                       ║')
        print('║ 6. Mostrar Pedidos                        ║')
        print('║ 0. Sair                                   ║')
        print('╚═══════════════════════════════════════════╝')
        
def cadastrar_cliente():
    while True:
        # Gera um código de cliente sequencial
        cod_cliente = len(clientes) + 1
        print(f'\nCadastro do Cliente {cod_cliente}')
        # Coleta informações do cliente
        nome = str(input('Informe o nome completo do cliente: '))
        cel = str(input(f'Informe o número de celular do cliente [{nome}]: '))
        cpf = str(input(f'Informe o CPF do cliente [{nome}]: '))
        email = str(input(f'Informe o email do cliente [{nome}]: '))
        # Cria instancia Cliente
        cliente = m.Cliente(cod_cliente, nome, cel, cpf, email)
        # Adiciona instancia Cliente à lista de clientes
        clientes.append(cliente)
        # Pergunta se deseja continuar cadastrando mais clientes
        continuar = str(input('Deseja cadastrar outro cliente? (s/n): ')).lower()
        if continuar != 's':
            break
    
def cadastrar_produto():
    while True:
        # Gera um código de produto sequencial
        cod_produto = len(produtos) + 1
        print(f'\nCadastro do produto [{cod_produto}]')
        # Coleta informações do produto
        nome_produto = str(input('Informe o nome do produto: '))
        descricao = str(input(f'Informe uma breve descrição para o produto [{nome_produto}]: '))
        valor = float(input(f'Informe o valor do produto [{nome_produto}] R$:'))
        # Cria instancia Produto
        produto = m.Produto(cod_produto,nome_produto,descricao,valor)
        # Adiciona o produto à lista de proddutos
        produtos.append(produto)
        # Pergunta se deseja continuar cadastrando mais produtos
        continuar = str(input('Deseja cadastrar outro produto? (s/n): ')).lower()
        if continuar != 's':
            break

def cadastrar_pedido():
    while True:
        # Gera um código de pedido sequencial
        num_pedido = len(pedidos) + 1
        print(f'\nCadastro do pedido [{num_pedido}]')
        # Coleta informações do pedido
        
        # Mostra os clientes disponiveis
        print('══════════════════════ Clientes: ')
        mostrar_clientes()
        # Captura código do cliente do pedido
        cod_cliente_pd = int(input(f'Informe o código cliente para o pedido {num_pedido}: '))
        # cria variavel para receber o cliente do pedido
        cliente_selecionado = None
        # procura o cliente selecionado na lista de clientes
        for cli in clientes:
            if cli.codigo == cod_cliente_pd:
                cliente_selecionado = cli
                break
        if cliente_selecionado:
            print(f'Cliente {cliente_selecionado.nome} selecionado')
        else:
            print('Cliente não encontrado.')
            print('-------------------------------------')
        
        # Mostra os produtos disponiveis
        print('══════════════════════ Produtos: ')
        mostrar_produtos()
        # cria lista para armazenar os produtos para o pedido
        produtos_ped = []
        while True:
            # Captura código do produto do pedido
            cod_produto_pd = int(input(f'Informe o código do produto para o pedido {num_pedido}: '))
            produto_selecionado = None
            for prod in produtos:
                if prod.codigo == cod_produto_pd:
                    produto_selecionado = prod
                    break
            
            if produto_selecionado:
                # Captura a quantidade de produto que será adquirida
                qtd_produto_pd = int(input(f'Informe a quantidade do produto {produto_selecionado.nome} para o pedido {num_pedido}: '))
                # Adiciona o produto e a quantidade como uma tupla na lista de produtos do pedido
                produtos_ped.append((produto_selecionado, qtd_produto_pd))
            else:
                print('Produto não encontrado.')
                print('-------------------------------------')

            # Pergunta se deseja continuar cadastrando mais produtos
            continuar = str(input('Deseja cadastrar outro produto? (s/n): ')).lower()
            if continuar != 's':
                break

        # Cria a instância do Pedido
        pedido = m.Pedido(num_pedido, cliente_selecionado, produtos_ped)
        # Adiciona o pedido à lista de pedidos
        pedidos.append(pedido)
        print(f'Pedido {num_pedido} cadastrado com sucesso.')

        # Pergunta se deseja cadastrar um novo pedido
        continuar = str(input('Deseja cadastrar outro pedido? (s/n): ')).lower()
        if continuar != 's':
            break

def mostrar_clientes():
    if not clientes:
        print('Nenhum cliente cadastrado.')
        cadastrar_cliente()
    for cliente in clientes:
        print(f'COD: {cliente.codigo}')
        print(f'CLIENTE: {cliente.nome}')
        print(f'CELULAR: {cliente.telefone}')
        print(f'CPF: {cliente.cpf}')
        print(f'EMAIL: {cliente.email}')
        print('-------------------------------------')
    
def mostrar_produtos():
    if not produtos:
        print('Nenhum produto cadastrado.')
        cadastrar_produto()
    for produto in produtos:
        print(f'COD: {produto.codigo}')
        print(f'PRODUTO: {produto.nome}')
        print(f'DESCRIÇÃO: {produto.descricao}')
        print(f'VALOR: R${produto.valor:.2f}')
        print('-------------------------------------')
    
def mostrar_pedidos():
    if not pedidos:
        print('Nenhum pedido cadastrado.')
        cadastrar_pedido()
    
    for pedido in pedidos:
        print(f'Pedido Número: {pedido.codigo}')
        print(f'Cliente: {pedido.cliente.nome}')
        
        total_ped = 0
        for produto, quantidade in pedido.produtos:
            total_prod = quantidade * produto.valor
            print(f'Qtd {quantidade} - {produto.nome} - R$ {produto.valor:.2f}.....R$ {total_prod:.2f}')
            total_ped += total_prod
        
        print(f'Valor Total..................R$ {total_ped:.2f}')
        print('-------------------------------------')

