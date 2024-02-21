nome = 'André Dimitrin'
altura = 1.91
peso = 103

imc = peso / (altura * altura)
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso normal')
elif imc < 30:
    print('Acima do peso')
elif imc < 35:
    print('Obeso')
else:
    print('Obeso mórbido')

# print('Nome:', nome)
# print('Altura:', altura)
# print('Peso:', peso)
# print('IMC:', imc)