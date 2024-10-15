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
            cel = str(input(f'Informe o número de celular do cliente {nome}: '))
            cliente.append(cel)
            cpf = str(input(f'Informe o CPF do cliente {nome}: '))
            cliente.append(cpf)
            email = str(input(f'Informe o email do cliente: '))
            cliente.append(email)
            # Adiciona o cliente à lista de clientes
            clientes.append(cliente)
            # Pergunta se deseja continuar cadastrando mais clientes
            continuar = str(input('Deseja cadastrar outro cliente? (s/n): ')).lower()
            if continuar != 's':
                break
    elif opcao == '2':
        # Título para a seção de cadastro de clientes
        print('═══════════ CADASTRO DE PRODUTOS ═══════════')
    elif opcao == '3':
        # Título para a seção de cadastro de clientes
        print('═══════════ REALIZAR PEDIDO ═══════════')
    elif opcao == '4':
        # Título para a seção de cadastro de clientes
        print('═══════════ CLIENTES CADASTRADOS ═══════════')
        for cliente in clientes:
            print(f'COD: {cliente[0]}')
            print(f'CLIENTE: {cliente[1]}')
            print(f'CELULAR: {cliente[2]}')
            print(f'CPF: {cliente[3]}')
            print(f'EMAIL: {cliente[4]}')
            print('-------------------------------------')
    elif opcao == '5':
        # Título para a seção de cadastro de clientes
        print('═══════════ PRODUTOS CADASTRADOS ═══════════')    
    elif opcao == '6':
        # Título para a seção de cadastro de clientes
        print('═══════════ PEDIDOS CADASTRADOS ═══════════')
    elif opcao == '0':
        print('Saindo do sistema. Até mais!')
        break
    else:
        print('Opção inválida. Tente novamente.')
