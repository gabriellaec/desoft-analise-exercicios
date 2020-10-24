import math
g=9.8
v=float(input('Velocidade da jaca: '))
t=float(input('Ângulo de lançamento da jaca: '))
d=((v**2)*math.sin(2*t))/g
if 98<d<102:
    print('Acertou!')
elif d>=102:
    print('Muito longe')
elif d<=98:
    print('Muito perto')