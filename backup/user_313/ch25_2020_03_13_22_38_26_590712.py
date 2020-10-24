import math


v = int(input('Velocidade: '))
a = int(input('Angulo: '))

g = 9.8

d = ((v**2)*(math.sin(2a)))/g

if (d > 98):
    print('Muito longe')

elif (d < 98):
    print('Muito perto')

else:
    print('Acertou!')
