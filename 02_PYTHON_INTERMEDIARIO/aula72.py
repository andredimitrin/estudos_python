# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

numMult = multiplica(3,7)
# print(numMult)

def par_impar(numero):
    multiplo = numero % 2 == 0
    
    if multiplo:
        return f'{numero} é par'
    return f'{numero} é impar'
            
print(par_impar(numMult))