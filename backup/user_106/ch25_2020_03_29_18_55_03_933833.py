import math
g=9.8
v=float(input('Velocidade da jaca: '))
t=float(input('Ângulo de lançamento da jaca (em graus): '))
d=(v**2)*math.sin(math.radians(2*t))/g

if d>=102:
    print('Muito longe')
elif d<=98:
    print('Muito perto')
else:
    print('Acertou!')