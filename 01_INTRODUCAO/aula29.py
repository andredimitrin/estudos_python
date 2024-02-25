"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorrer o erro 
"""
numero = input('Vou dorar um número. Qual e ele? ')


# if numero.isdigit():
#     print(f'O dobro de {numero} é {float(numero) * 2}')
# else: 
#     print('Isso não e um número')    

try:
    print(f'O dobro de {numero} é {float(numero) * 2}')
except:
    print('Isso não e um número')