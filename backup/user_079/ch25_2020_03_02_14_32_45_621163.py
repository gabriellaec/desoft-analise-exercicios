import math

vel = float(input('vel?:'))
a = float(input('a?:'))
d=((vel**2)*(math.sin(2*math.radians(a))))/9.8
if 98<=d and d<=102:
    print('Acertou!')
elif d<98:
    print('Muito perto')
elif d>102:
    print('Muito longe')

