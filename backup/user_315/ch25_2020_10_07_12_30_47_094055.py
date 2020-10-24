from math import *
alvo = 100
g = 9.8

def catapulta (a,b):
    teta = degrees(b)
    c = (a**2)*sin(2*teta)
    d = c/g
    if d < alvo:
        return ('Muito perto')
    elif d > alvo:
        return ('Muito longe')
    else:
        return ('Acertou!')

v = float(input('Insira a velocidade: '))
ang = float(input('Insira o angulo: '))