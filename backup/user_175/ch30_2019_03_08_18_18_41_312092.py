import math
a = float(input())
velocidade = float(input())

a = math.radians(a)
distancia = (((velocidade**2)*(math.sin(2*a)))/9.8)

if (distancia < 98):
    print('Muito perto')
elif (distancia > 102):
    print('Muito longe')
else:
    print('Acertou!')