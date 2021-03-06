import math

angulo_graus = float(input())
velocidade = float(input())

g = 9.8
r = 2

angulo_radianos = (((math.pi)*(angulo_graus))/180)

distancia = (((velocidade**2)*(math.sin(2*angulo_radianos)))/g) 

if (abs(distancia-r) < 2):
    print('Acertou!')
elif (96<=distancia<=98) or (102<=distancia<=104):
    print('Muito perto')
else:
    print('Muito longe')