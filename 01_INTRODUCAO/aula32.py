"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Primeiro exercício 

numero_inteiro = input('Digite um número inteiro: ')

if numero_inteiro.isdigit():
    if int(numero_inteiro) % 2 == 0:
        print('Par')
    else:
        print('Impar')
else:
    print('Isso não é um número inteiro')


# Segundo exercício   
    
horario = input('Qual horário é (0-23) ? ')

if horario.isdigit():
    horario = int(horario)
    if horario <= 11:
        print('Bom dia')
    elif horario <= 17:
        print('Boa tarde')
    else:
        print('Boa noite')
else:
    print('Isso não é um horário')
    
# Terceiro exercício
    
nome = input('Qual seu nome? ')

if nome is not None:
    if len(nome) <= 4:
        print('Seu nome é curto')
    elif len(nome) <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Desculpe, você deixou campos vazios.')