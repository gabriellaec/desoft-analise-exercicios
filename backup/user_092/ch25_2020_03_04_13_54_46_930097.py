import math
g = 9.8
def jaca(v,θ):
    math.radians(θ)
    d = ((V**2)*(math.sin(2*θ)))/g
    if d>=102:
        print('Muito longe')
    if d<=98:
        print('Muito perto')
    if d<102 and d>98:
        print('Acertou!')