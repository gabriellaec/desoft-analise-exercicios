import math

velocidade = int(input())
angulo = int(input())

g = 9.8
d = ((velocidade**2) * math.sin(2*angulo))/g

if d > 98 or d < 102:
    print('Acertou!')
elif d <= 98:
    print('Muito perto')
else:
    print('Muito longe')