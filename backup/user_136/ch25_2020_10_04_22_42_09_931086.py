import math
g= 9.8

def distancia(v, o):
    k= math.sin
    d= ((v**2)*k(math.radians(2*o)))/g
    #return d
    if d>102:
        print ('Muito longe')
    elif d<98:
        print ('Muito perto')
    else:
        print ('Acertou!')

x= int(input('qual a velocidade? '))
y= int(input('qual o angulo? '))
distancia(x, y)