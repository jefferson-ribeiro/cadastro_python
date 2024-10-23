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
import functions as f

# Exibe o cabeçalho estilizado do console
f.boasvindas()

# Loop principal do sistema
while True:
    # Menu principal
    f.menu()
    opcao = input('Selecione uma opção: ')
    
    if opcao == '1':
        # Título para a seção de cadastro de clientes
        print('═══════════ CADASTRO DE CLIENTES ═══════════')
        f.cadastrar_cliente()        
    elif opcao == '2':
        # Título para a seção de cadastro de produtos
        print('═══════════ CADASTRO DE PRODUTOS ═══════════')
        f.cadastrar_produto()  
        
    elif opcao == '3':
        # Título para a seção de cadastro de clientes
        print('═══════════ REALIZAR PEDIDO ═══════════')
        f.cadastrar_pedido()
        
    elif opcao == '4':
        # Título para a seção de clientes cadastrados
        print('═══════════ CLIENTES CADASTRADOS ═══════════')
        f.mostrar_clientes()
        
    elif opcao == '5':
        # Título para a seção produtos cadastrados
        print('═══════════ PRODUTOS CADASTRADOS ═══════════')
        f.mostrar_produtos()
           
    elif opcao == '6':
        # Título para a seção de pedidos cadastrados
        print('═══════════ PEDIDOS CADASTRADOS ═══════════')
        f.mostrar_pedidos()
        
    elif opcao == '0':
        print('Saindo do sistema. Até mais!')
        break
    else:
        print('Opção inválida. Tente novamente.')