import math
v = int (input('velocidade'))
a = input('angulo')
def distancia(v, a):
    d = ((v**2) * math.sin * (2 * a))/9.8
    return d
    if d < 102:
    print ('Acertou!')
    elif d > 102:
        print ('Muito longe')
    else: print ('Muito perto')