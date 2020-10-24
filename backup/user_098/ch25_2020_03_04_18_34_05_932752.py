import math

def verifica_distancia(v,o):
    o = math.radians(2*o)
    d = (v**2)*math.sin(o)/(9.8)
    if d>102:
        print('Muito longe')
    elif d>=98 and d<=102:
        print('Acertou!')    
    else:
        print('Muito perto')