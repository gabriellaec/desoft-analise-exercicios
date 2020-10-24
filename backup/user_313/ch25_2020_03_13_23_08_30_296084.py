import math


v = float(input('Velocidade: '))
a = float(input('Angulo: '))

g = 9.8

d = (((v**2)*math.sin(2*math.radians(a)))/g)


if (d > 98):
    print('Muito longe')

if (d < 98):
    print('Muito perto')

if (d == 98):
    print('Acertou!')
