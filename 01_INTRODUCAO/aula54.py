"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista_compras = []

while True:
    print('Selecione uma opção:')
    print('1 - Incluir item na lista')
    print('2 - Excluir item da lista')
    print('3 - Listar itens da lista')
    print('4 - Sair')
    opcao = input('Opcão: ')
    
    try:
        opcao = int(opcao)
        
    
        if opcao == 1:           
            item = input('Item: ')
            lista_compras.append(item)
        elif opcao == 2:
            item = input('Item: ')
            if item in lista_compras:
                lista_compras.remove(item)
            else:
                print('Item inexistente')
        elif opcao == 3:
            print('Lista de itens:')
            for item in lista_compras:
                print(item)
        elif opcao == 4:
            break
        else:
            print('Opcão inválida')
        
    except ValueError:
        print('Por favor, insira um número válido para a opção.')
        
    print()
    
print('Programa encerrado')