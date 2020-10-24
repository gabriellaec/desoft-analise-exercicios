import math
v=float(input('velocidade'))
g=float(input('graus'))

d=(v**2*math.radians(2*r))/9.8
if d<98:
    print('Muito longe')
elif d>=98 and d<=102:
    print('Acertou!')
else:
    print('Muito perto')
  