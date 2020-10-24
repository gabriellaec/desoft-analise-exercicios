import math
def jaca(v,t):
    d=v**2*math.sin(2*t)/9.8
    return d
if d>98:
    if d<102:
        print('Acertou!')
    else:
        print('Muito longe')
else:
    print('Muito perto')