import math
velocidade = int(input('velocidade: '))
angulo = int(input('angulo: '))
d = (velocidade**2*math.sin(2*math.radians(angulo))/9.8
if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
else:
    print('Acertou!')
print(d)