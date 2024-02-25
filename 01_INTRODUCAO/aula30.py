"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
# Constantes
RADAR_VELOCIDADE_MAXIMA = 60
RADAR_POSICAO = 100
RADAR_ALCANCE = 1

# Variáveis do carro
velocidade_carro = 80
posicao_carro = 80

# Verificar se a velocidade do carro está acima da velocidade máxima do radar
if velocidade_carro > RADAR_VELOCIDADE_MAXIMA:
    print('O carro está acima da velocidade máxima do radar')

# Verificar se o carro está dentro do alcance do radar
if RADAR_POSICAO - RADAR_ALCANCE <= posicao_carro <= RADAR_POSICAO + RADAR_ALCANCE:
    print('O carro está dentro do alcance do radar')
else:
    print('O carro está fora do alcance do radar')
