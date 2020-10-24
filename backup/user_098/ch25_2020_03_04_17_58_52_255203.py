import math

def verifica_distancia(v,o):
    d = ((v**2)*math.sin(2*o))/(9.8)
    dfinal = 100-d
    print(d)
    print(dfinal)
    if dfinal<0:
        print('Muito perto')
        return 'Muito perto'
    elif dfinal==100:
        print('Acertou!')
        return 'Acertou!'
    else:
        print('Muito longe')
        return 'Muito longe'

vel = float(input("Velocidade: "))

ang = float(input("Angulo: "))