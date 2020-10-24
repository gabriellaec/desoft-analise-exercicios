import math

def verifica_distancia(v,o):
    d = (((v**2)*math.sin(((2*o)*math.pi)/(180)))/(9.8))
    dfinal = abs(100-d)
    print(d)
    print(dfinal)
    if dfinal>102:
        print('Muito longe')
        return 'Muito longe'
    elif abs(dfinal)<=2:
        print('Acertou!')
        return 'Acertou!'
    else:
        print('Muito perto')
        return 'Muito perto'  

vel = float(input("Velocidade: "))

ang = float(input("Angulo: "))