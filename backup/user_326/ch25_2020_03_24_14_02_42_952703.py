import math
gravidade = 9.8

velocidade = int(input('Qual a velocidade de sua jaca? '))

angulo = math.radians(int(input('qual o ângulo de lançamento? ')))

distancia = velocidade**2 * math.sin(2 * angulo) / gravidade

if distancia <= 102 and distancia >= 98:
    print('Acertou!')
    print(distancia)
elif distancia < 98:
    print('Muito perto')
    print(distancia)
else:
    print('Muito longe')
    print(distancia)
