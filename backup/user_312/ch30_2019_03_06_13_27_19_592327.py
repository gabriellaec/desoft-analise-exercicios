import math
v=float(input('escreva a velocidade'))
angulo=float(input('escreva o angulo de lançamento'))
d=(v**2*math.sin(math.radians(2*angulo)))/9.8
if 98<d:
    print('Muito perto')
elif d>102:
    print('Muito longe')
else:
    print('Acertou!')