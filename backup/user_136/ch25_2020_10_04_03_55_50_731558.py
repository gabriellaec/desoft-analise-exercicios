import math
g= 9.8
def distancia(v, o):
    k= math.sin
    d= ((v**2)*k(2*o))/g
    if d>=99 and d<=101:
        print ('Acertou!')
    elif d>101:
        print ('Muito longe')
    elif d<99:
        print ('Muito perto')