"""
Flag(Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é(tipo, valor, identidade)
id = identidade 
"""

# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Verdadeiro')
else:
    print('Falso')
    



if passou_no_if is None:
    print('Falso')

if passou_no_if is not None:
    print('Verdadeiro')