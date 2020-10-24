import math


v = float(input('Velocidade: '))
a = float(input('Angulo: '))

g = 9.8

d = ((v*v)*math.degrees(math.sin(2*a)))/g
print(d)

if (d > 98):
    print('Muito longe')

if (d < 98):
    print('Muito perto')

if (d == 98):
    print('Acertou!')
