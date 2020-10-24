import math
velocidade=float(input('Qual é a velocidade?'))
angulo=float(input('Qual o angulo de lançamento?'))
distancia=(velocidade**2*math.sin(2*angulo))/9.8
if distancia>=90 and distancia<=110:
    print('Acertou!')
elif distancia=96 and distancia<=104:
    print('Muito perto')
else:
    print('Muito longe')