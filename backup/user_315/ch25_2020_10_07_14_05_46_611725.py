from math import *
g = 9.8
def catapulta (a,b):
    d = ((a**2)*sin(radians(2*b)))/g
    print (d)
    if d <= 102 and d>= 98:
        return ('Acertou!')
    elif d < 98:
        return ('Muito perto')
    else:
        return ('Muito longe')

v = float(input('Insira a velocidade: '))
ang = float(input('Insira o angulo: '))