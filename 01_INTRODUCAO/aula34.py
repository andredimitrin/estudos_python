"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual seu nome? ')
    print(f'Seja bem-vindo(a) {nome}')
    
    if nome == 'sair':
        break