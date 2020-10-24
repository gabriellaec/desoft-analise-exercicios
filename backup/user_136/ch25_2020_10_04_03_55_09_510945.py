import math
g= 9.8
def distancia(v, o):
    k= math.sin
    h= (180/math.pi)*o
    d= ((v**2)*k(2*h))/g
    if d>=97 and d<=103:
        print ('Acertou!')
    elif d>103:
        print ('Muito longe')
    elif d<97:
        print ('Muito perto')