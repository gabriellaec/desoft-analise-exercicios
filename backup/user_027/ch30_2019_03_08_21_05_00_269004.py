import math

angulo = int(input())
angulo = math.radians(angulo)
v = float(input('Digite a velocidade'))
g = 9.8
d = ((v**2)*sin(2*angulo))/g
if d <= 98:
    print('Muito perto')
elif d >= 102:
    print('Muito longe')
else:
    print('Acertou!')