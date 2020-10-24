import math
g= 9.8
def distancia(v, o):
    k= math.sin
    #h= (180/math.pi)*o
    d= ((v**2)*k(math.radians(2*o)))/g
    if d>98 and d<102:
        print ('Acertou!')
    elif d>102:
        print ('Muito longe')
    elif d<98:
        print ('Muito perto')

v= int(input('qual a velocidade? '))
o= int(input('qual o angulo? '))