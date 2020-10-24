# catapulta do vizinho a 100m
import math
def acertou(v,teta,g,d):
    v = int(input('velocidade: '))
    teta = int(input('angulo: '))  
    g = 9.8
    d = ((v**2)*math.sin(2*teta))/g

    if d - 100 > 2:
        print ('Muito longe')

    elif d - 100 < 2:
        print ('Muito perto')
    else:
        print ('Acertou!')