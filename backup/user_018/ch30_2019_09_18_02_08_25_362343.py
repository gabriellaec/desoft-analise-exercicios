import math

def calcula_jaca (v,ang):
    ang = math.radians(ang)
    d = v**2 * math.sin(2*ang)/9.8
    if d > 102:
        return 'Muito longe'
    elif d < 98:
        return 'Muito perto'
    else:
        return 'Acertou!'

v = float(input('Qual a velocidade de lançamento? '))
ang = float(input('Qual o ângulo de lançamento? '))