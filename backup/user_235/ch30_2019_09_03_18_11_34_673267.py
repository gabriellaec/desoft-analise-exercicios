import math
g=9.8
v=float(input('qual a vel?'))
a=float(input('qual o angulo?'))
d=(v**2*math.sin(2*a))/g
if 98<=d and d<=102:
        print('Acertou!')
elif d<98:
        print('Muito perto')
elif d>102:
        print('Muito longe')