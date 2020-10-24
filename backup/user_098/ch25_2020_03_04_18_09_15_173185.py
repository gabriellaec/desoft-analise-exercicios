import math

def verifica_distancia(v,o):
    d = ((v**2)*math.sin(((2*o)*180)/(math.pi)))/(9.8)
    dfinal = 100-d
    print(d)
    print(dfinal)
    if d>102:
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