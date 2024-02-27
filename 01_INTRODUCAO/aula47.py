"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

# import os

# def limpar_tela():
#     os.system('cls' if os.name == 'nt' else 'clear')

# palavra_secreta = input('Digite a palavra secreta: ').lower()
# limpar_tela()

# letras_adivinhadas = ['*' for _ in palavra_secreta]

# erros = 0
# tentativas = 0
# while erros < 3:
#     tentativas += 1
#     print('Palavra: ', ' '.join(letras_adivinhadas))  
#     letra = input('Digite uma letra: ').lower()
#     limpar_tela()
#     if letra in palavra_secreta:
#         print(f'A letra "{letra}" está na palavra secreta!')
#         letras_adivinhadas = list(letras_adivinhadas)
#         for i in range(len(palavra_secreta)):
#             if palavra_secreta[i] == letra:
#                 letras_adivinhadas[i] = letra
#     else:
#         print(f'A letra "{letra}" não está na palavra secreta.')
#         erros += 1

#     if '*' not in letras_adivinhadas:
#         print('Parabéns! Você adivinhou a palavra secreta:', palavra_secreta)
#         print('Número de tentativas:', tentativas)
#         break
# else:
#     print('Você excedeu o número máximo de tentativas. A palavra secreta era:', palavra_secreta)
#     print('Número de tentativas:', tentativas)


import os


palavra_secreta = 'perfume'
letras_acertadas =''
tentativas = 0

while True:
    
    
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'          
    
    print(f'Palavra formada: \n{palavra_formada}')
    
    if palavra_formada == palavra_secreta:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Parabéns, você acertou a palavra secreta {palavra_secreta} em {tentativas} tentativas.')
        break