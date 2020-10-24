import math

angulo_graus = float(input())
velocidade = float(input())

g = 9.8
r = 2
x = 10

angulo_radianos = (((math.pi)*(angulo_graus))/180)
distancia = (((velocidade**2)*(math.sin(2*angulo_radianos)))/g) 

if (abs(distancia-100) < r):
    print('Acertou!')
elif (abs(distancia-100) < x):
    print('Muito perto')
else:
    print('Muito longe')