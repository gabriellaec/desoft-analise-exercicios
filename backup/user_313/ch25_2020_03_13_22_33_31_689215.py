import math


v = int(input('Velocidade: '))
a = int(input('Angulo: '))

g = 9.8

d = ((v**2)*(math.sin(a)))/g

if (d > 98):
    print('Muito longe')

if (d < 98):
    print('Muito perto')

if (d == 98):
    print('Acertou!')
