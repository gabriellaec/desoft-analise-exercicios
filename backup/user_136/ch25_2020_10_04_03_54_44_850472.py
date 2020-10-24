import math
g= 9.8
def distancia(v, o):
    k= math.sin
    h= (180/math.pi)*o
    d= ((v**2)*k(2*h))/g
    if d>=99 and d<=101:
        print ('Acertou!')
    elif d>101:
        print ('Muito longe')
    elif d<99:
        print ('Muito perto')