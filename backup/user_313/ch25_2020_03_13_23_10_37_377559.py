import math


v = float(input('Velocidade: '))
a = float(input('Angulo: '))

g = 9.8

d = ((v**2)*(math.sin(2*math.degrees(a))))/g


if (d > 102):
    print('Muito longe')

elif (d < 98):
    print('Muito perto')

else:
    print('Acertou!')
