import math
v=float(input('velocidade'))
θ=math.radians(int(input('angulo')))
g=9.8
d=((v**2)*math.sin(2*θ))/g
if d>=102:
    print('Muito longe')
elif d<=98:
    print('Muito perto')
else:
    print('Acertou!')