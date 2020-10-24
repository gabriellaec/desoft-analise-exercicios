import math
g=9.8
v=float(input('Velocidade da jaca: '))
t=float(input('Ângulo de lançamento da jaca: '))
h=t*180/math.pi
d=((v**2)*math.sin(2*h))/g
if d>98 and d<102:
    print('Acertou!')
elif d>=102:
    print('Muito longe')
elif d<=98:
    print('Muito perto')