import math
gravidade = 9.8

velocidade = int(input('Qual a velocidade de sua jaca? '))

angulo = int(input('qual o ângulo de lançamento? '))

distancia = ((velocidade**2) * math.sin(2 * angulo)) / gravidade

if distancia <= 102 and distancia >= 98:
    print('Acertou!')
elif distancia < 98:
    print('Muito perto')
else:
    print('Muito longe')
