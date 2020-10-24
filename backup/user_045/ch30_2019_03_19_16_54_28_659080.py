import math
v=float(input('velocidade'))
g=float(input('graus'))

d=v**2*math.sin(math.radians(2*g))/9.8
if d<98:
    print('Muito perto')
elif d>102:
    print('Muito longe')
else:
    print('Acertou!')
  