import math

def verifica_distancia(v,o):
    d = ((v**2)*math.sin(2*o))/(9.8)
    dfinal = abs(d-100)
    print(d)
    print(dfinal)
    if dfinal>2:
        print('Muito perto')
    elif dfinal<2:
        print('Muito longe')
    else:
        print('Acertou!')

vel = float(input("Velocidade: "))

ang = float(input("Angulo: "))