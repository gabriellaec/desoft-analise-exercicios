import math
g = 9.8
angulo = int(input())
angulo = math.radians(angulo)
v = float(input('Digite a velocidade'))
d = (v**2)*math.sin(2*angulo)/g
if d > 102:
    print('Muito longe')
elif d < 98:
    print('Muito perto')
else:
    print('Acertou!')