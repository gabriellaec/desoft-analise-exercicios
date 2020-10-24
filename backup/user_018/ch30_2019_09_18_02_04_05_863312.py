import math

def calcula_jaca (v,ang):
    ang = math.radians(ang)
    d = (((v)^2 * sin * (2*ang)) / 9.8)
    if d > 102:
        print('Muito longe')
    elif d < 98:
        print('Muito perto')
    else:
        print('Acertou!')
    return d

v = float(input('Qual a velocidade de lançamento? '))
ang = float(input('Qual o ângulo de lançamento? '))