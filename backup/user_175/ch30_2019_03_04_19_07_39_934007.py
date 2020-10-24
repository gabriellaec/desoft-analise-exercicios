import math
angulo_graus = float(input())
velocidade = float(input())
g = 9.8
angulo_radianos = (((math.pi)*(angulo_graus))/180)
distancia = (((velocidade**2)*(math.sin(2*angulo_radianos)))/g)
if (98 < distancia < 102):
    print('Acertou!')
elif (distancia < 98):
    print('Muito perto')
else:
    print('Muito longe')