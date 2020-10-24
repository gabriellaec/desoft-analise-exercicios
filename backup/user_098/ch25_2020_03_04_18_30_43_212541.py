import math

def verifica_distancia(v,o):
    o = math.radians(o)
    d = (v**2)*math.sin(2*o)/(9.8)
    dfinal = abs(100-d)
    if d>102:
        print('Muito longe')
    elif d>=98 and d<=102:
        print('Acertou!')    
    else:
        print('Muito perto')

vel = float(input("Velocidade: "))

ang = float(input("Angulo: "))