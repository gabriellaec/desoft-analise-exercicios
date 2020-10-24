import math
v = float(input('Velocidade'))
a = float(input('Angulo Graus'))
g = 9.8
r = math.radians(a)

d = v**2 * math.sin(2*a) / g

if d <= 98:
    print('Muito perto')
elif d >= 102:
    print('Muito longe')
else:
    print('Acertou!')