v = float(input('Qual é a velocidade? '))
angulo = float(input('Qual é o angulo de lançamento da jaca? '))

from math import sin, radians

d = (v**2)*sin*(radians(2*angulo))/9.8)

if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
else:
    print('Acertou!')