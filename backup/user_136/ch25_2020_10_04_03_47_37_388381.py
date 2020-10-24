import math
g= 9.8
def distancia(v, o):
    k= math.sin
    d= ((v**2)*k(2*o))/g
    if d>=98 and d<=102:
        print ('Acertou!')
    elif d>102:
        print ('Muito longe')
    elif d<98:
        print ('Muito perto')