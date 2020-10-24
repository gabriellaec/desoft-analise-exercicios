import math
angulo_graus = float(input())
velocidade = float(input())
angulo_radianos = (((math.pi)*(angulo_graus))/180)
distancia = (((velocidade**2)*(math.sin(2*angulo_radianos)))/9.8)
if (distancia < 98):
    print('Muito perto')
elif (distancia > 102):
    print('Muito longe')
else:
    print('Acertou!')