import math

vel = int(input('vel?:'))
a = int(input('a?:'))
d=((vel**2)*math.sin(2*a*0.0174533))/9.8
if 98<d<102:
    print('Acertou!')
if d<=98:
    print('Muito perto')
elif d>=102:
    print('Muito longe')

