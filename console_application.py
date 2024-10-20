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
                print('-------------------------------------')
            
            cod_cliente_pd = int(input(f'Informe o código cliente para o pedido {num_pedido}: '))
            cliente_selecionado = None
            for cli in clientes:
                if cli[0] == cod_cliente_pd:
                    cliente_selecionado = cli
                    break
            if cliente_selecionado:
                pedido.append(cliente_selecionado)
            else:
                print('Cliente não encontrado.')
                print('-------------------------------------')
            
            print('══════════════════════ Produtos: ')
            for produto in produtos:
                print(f'COD: {produto[0]}')
                print(f'PRODUTO: {produto[1]}')
            print('-------------------------------------')
            produtos_ped = []
            while True:     
                cod_produto_pd = int(input(f'Informe o código do produto para o pedido {num_pedido}: '))
                # Usando um loop para encontrar o produto
                produto_selecionado = None
                for prod in produtos:
                    if prod[0] == cod_produto_pd:
                        produto_selecionado = prod
                        break
                if produto_selecionado:
                    qtd_produto_pd = int(input(f'Informe a quantidade do produto {produto_selecionado[1]} para o pedido {num_pedido}: '))
                    produto_selecionado.append(qtd_produto_pd)
                    produtos_ped.append(produto_selecionado)
                else:
                    print('Produto não encontrado.')
                    print('-------------------------------------')
                # Pergunta se deseja continuar cadastrando mais produtos
                continuar = str(input('Deseja cadastrar outro produto? (s/n): ')).lower()
                if continuar != 's':
                    break      
            # Adiciona os produtos ao pedido
            pedido.append(produtos_ped)
            # Adiciona o pedido à lista de pedidos
            pedidos.append(pedido)
            # Pergunta se deseja cadastrar um novo pedido
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
            # pedido: pedido: [1, [1, 'jefferson', '1197436', '297', 'jef@gmail'], [[2, 'teclado', 'mecanico', 102.78, 2], [1, 'mouse', 'gamer', 50.36, 3]]]
            num_ped = pedido[0] # Número do pedido
            nom_cliente = pedido[1][1] # Nome do cliente
            
            print(f'Pedido Número: {num_ped}')
            print(f'Nome: {nom_cliente}')
            
            # lista_prod = [[2, 'teclado', 'mecanico', 102.78, 2], 
            # [1, 'mouse', 'gamer', 50.36, 3]]
            
            lista_prod = pedido[2]
            total_ped = 0
            for prod in lista_prod:
                nom_prod_ped = prod[1] # Nome do produto
                vlr_prod_ped_uni = prod[3] # Valor unitário do produto
                qtd_prod_ped = prod[4] # Quantidade de produto
                total_prod = qtd_prod_ped * vlr_prod_ped_uni # Valor total do produto
                print(f'Qtd {qtd_prod_ped} - {nom_prod_ped} - R$ {vlr_prod_ped_uni:.2f}.....R$ {total_prod:.2f}')
                total_ped += total_prod
            print(f'Valor Total..................R$ {total_ped:.2f}')
            print('-------------------------------------')
    elif opcao == '0':
        print('Saindo do sistema. Até mais!')
        break
    else:
        print('Opção inválida. Tente novamente.')