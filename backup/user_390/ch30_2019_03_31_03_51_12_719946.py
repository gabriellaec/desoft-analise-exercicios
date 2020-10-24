import math
v=int(input('velocidade'))
a=int(input('angulo'))
g=9.8
d=((v**2)*math.sin(2*a))/g
if d>=101:
    print('Muito longe')
elif d<=99:
    print('Muito perto')
else:
    print('Acertou!')