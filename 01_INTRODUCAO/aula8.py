import datetime

data_atual = datetime.datetime.now().year

nome = 'André Eduardo'
sobrenome = 'Dimitrin Andrade'
idade = data_atual - 1987
ano_nascimento = data_atual - idade
maior_de_idade = 'Sim' if idade >= 18 else 'Não'
altura_em_metros = 1.91



print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de Nascimento:', ano_nascimento)
print('É maior de idade?: ', maior_de_idade)
print('Altura em metros:', altura_em_metros , 'cm')