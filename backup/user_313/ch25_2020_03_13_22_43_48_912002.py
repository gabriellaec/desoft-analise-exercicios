import math


v = float(input('Velocidade: '))
a = float(input('Angulo: '))

g = 9.8

d = ((v*v)*(math.sin(2a)))/g

if (d > 98):
    print('Muito longe')

elif (d < 98):
    print('Muito perto')

else:
    print('Acertou!')
