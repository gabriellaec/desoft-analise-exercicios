import math


v = float(input('Velocidade: '))
a = float(input('Angulo: '))

g = 9.8

d = ((v**2)*(math.sin(a)))/g

if (d > 100):
    print('Muito longe')

if (d < 100):
    print('Muito perto')

if (d == 98):
    print('Acertou!')
