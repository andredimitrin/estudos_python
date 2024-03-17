"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ["Maria", "Helena", "Luiz"]

for nome in lista:
    print(f"{lista.index(nome)} {nome}")
