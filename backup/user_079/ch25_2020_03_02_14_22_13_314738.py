import math
import numpy as np

vel = int(input('vel?:'))
a = int(input('a?:'))
d=((vel**2)*(2*np.sin(np.deg2rad(a))))/9.8
if 98<d<102:
    print('Acertou!')
if d<=98:
    print('Muito perto')
elif d>=102:
    print('Muito longe')

