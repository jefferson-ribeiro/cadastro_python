# Um estabelecimento  precisa de um e-commerce para a venda de seus produtos, para este e-comerce, iremos precisar vincular os clientes, a os produtos e a os pedidos

#   para isso crie um sistema na qual será capturado os 
#   - Clientes (Codigo, Nome, Telefone, CPF, Email)
#   - Produtos (Codigo, Nome, descricao, valor)
#   - Pedidos (Codigo, CodigoCliente, CodigoProduto, QuantidadeProduto, ValorTotal)

#   Resultado final, mostre um relatório com os pedidos dos clientes da sequinte forma:

#   ::::: Pedidos ::::
#   --------------------------
#   Pedido Número: 1
#   Nome: Danilo
#   Produto: Mouse
#   ValorTotal: R$ 200
#   --------------------------
#   Pedido Número: 2
#   Nome: Jesus
#   Produto: Teclado
#   ValorTotal: R$ 250
#   --------------------------
#   Pedido Número: 3
#   Nome: Maria
#   Produto: Monitor
#   ValorTotal: R$ 300
#   --------------------------
import time

# Exibe o cabeçalho estilizado do console
print('╔═════════════════════════════════╗')
print('║   Bem-vindo ao E-Shop Brasil    ║')
print('║     Tecnologia e Inovação       ║')
print('╚═════════════════════════════════╝')
time.sleep(2)

# Inicializa as listas para armazenar dados
clientes = []
produtos = []
pedidos = []

# Loop principal do sistema
while True:
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
    opcao = input('Selecione uma opção: ')
    
    if opcao == '1':
        # Título para a seção de cadastro de clientes
        print('═══════════ CADASTRO DE CLIENTES ═══════════')     
        while True:
            cliente = []  # Lista para armazenar informações de um cliente 
            # Gera um código de cliente sequencial
            cod_cliente = len(clientes) + 1
            print(f'\nCadastro do Cliente {cod_cliente}')
            # Coleta informações do cliente
            cliente.append(cod_cliente)
            nome = str(input('Informe o nome completo do cliente: '))
            cliente.append(nome)
            cel = str(input(f'Informe o número de celular do cliente [{nome}]: '))
            cliente.append(cel)
            cpf = str(input(f'Informe o CPF do cliente [{nome}]: '))
            cliente.append(cpf)
            email = str(input(f'Informe o email do cliente [{nome}]: '))
            cliente.append(email)
            # Adiciona o cliente à lista de clientes
            clientes.append(cliente)
            # Pergunta se deseja continuar cadastrando mais clientes
            continuar = str(input('Deseja cadastrar outro cliente? (s/n): ')).lower()
            if continuar != 's':
                break
    elif opcao == '2':
        # Título para a seção de cadastro de produtos
        print('═══════════ CADASTRO DE PRODUTOS ═══════════')
        while True:
            produto = []  # Lista para armazenar informações de um produto 
            # Gera um código de produto sequencial
            cod_produto = len(produtos) + 1
            print(f'\nCadastro do produto [{cod_produto}]')
            # Coleta informações do produto
            produto.append(cod_produto)
            nome_produto = str(input('Informe o nome do produto: '))
            produto.append(nome_produto)
            descricao = str(input(f'Informe uma breve descrição para o produto [{nome_produto}]: '))
            produto.append(descricao)
            valor = float(input(f'Informe o valor do produto [{nome_produto}] R$:'))
            produto.append(valor)
            # Adiciona o produto à lista de proddutos
            produtos.append(produto)
            # Pergunta se deseja continuar cadastrando mais produtos
            continuar = str(input('Deseja cadastrar outro produto? (s/n): ')).lower()
            if continuar != 's':
                break
    elif opcao == '3':
        # Título para a seção de cadastro de clientes
        print('═══════════ REALIZAR PEDIDO ═══════════')
        
        while True:
            pedido = []  # Lista para armazenar informações de um pedido 
            # Gera um código de pedido sequencial
            num_pedido = len(pedidos) + 1
            print(f'\nCadastro do pedido [{num_pedido}]')
            # Coleta informações do pedido
            pedido.append(num_pedido)
            
            print('══════════════════════ Clientes: ')
            for cliente in clientes:
                print(f'COD: {cliente[0]}')
                print(f'CLIENTE: {cliente[1]}')
            cod_cliente_pd = int(input(f'Informe o código cliente para o pedido {num_pedido}: '))
            pedido.append(cod_cliente_pd)
            print('-------------------------------------') 
            
            print('══════════════════════ Produtos: ')
            for produto in produtos:
                print(f'COD: {produto[0]}')
                print(f'PRODUTO: {produto[1]}')
            cod_produto_pd = int(input(f'Informe o código do produto para o pedido {num_pedido}: '))
            qtd_produto_pd = int(input(f'Informe a quantidade do produto {cod_produto_pd} para o pedido {num_pedido}: '))
            pedido.append(cod_produto_pd)
            pedido.append(qtd_produto_pd)
            print('-------------------------------------') 
            
            # Adiciona o pedido à lista de pedidos
            pedidos.append(pedido)
            # Pergunta se deseja continuar cadastrando mais produtos
            continuar = str(input('Deseja cadastrar outro pedido? (s/n): ')).lower()
            if continuar != 's':
                break  
    elif opcao == '4':
        # Título para a seção de clientes cadastrados
        print('═══════════ CLIENTES CADASTRADOS ═══════════')
        for cliente in clientes:
            print(f'COD: {cliente[0]}')
            print(f'CLIENTE: {cliente[1]}')
            print(f'CELULAR: {cliente[2]}')
            print(f'CPF: {cliente[3]}')
            print(f'EMAIL: {cliente[4]}')
            print('-------------------------------------')
    elif opcao == '5':
        # Título para a seção produtos cadastrados
        print('═══════════ PRODUTOS CADASTRADOS ═══════════')
        for produto in produtos:
            print(f'COD: {produto[0]}')
            print(f'PRODUTO: {produto[1]}')
            print(f'DESCRIÇÃO: {produto[2]}')
            print(f'VALOR: R${produto[3]}')
            print('-------------------------------------')   
    elif opcao == '6':
        # Título para a seção de pedidos cadastrados
        print('═══════════ PEDIDOS CADASTRADOS ═══════════')
        for pedido in pedidos:
            cliente = [cli for cli in clientes if cli[0] == pedido[1]][0]
            produto = [prod for prod in produtos if prod[0] == pedido[2]][0]
            print(f'Pedido Número: {pedido[0]}')
            print(f'Nome: {cliente[1]}')
            print(f'Qtd:{pedido[3]}..........Produto: {produto[1]}')
            print(f'Preço Unitário: R${produto[3]:.2f} Total: R${pedido[3] * produto[3]:.2f}')
            print('-------------------------------------')
    elif opcao == '0':
        print('Saindo do sistema. Até mais!')
        break
    else:
        print('Opção inválida. Tente novamente.')