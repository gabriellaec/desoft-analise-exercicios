import math
v=float(input('escreva a velocidade'))
angulo=float(input('escreva o angulo de lançamento'))
d=(v**2*math.sin(math.radians(2*angulo)))/9.8
if 98<=d or d<=102:
    print('Acertou!')
elif d<98:
    print('Muito perto')
else:
    print('Muito longe')