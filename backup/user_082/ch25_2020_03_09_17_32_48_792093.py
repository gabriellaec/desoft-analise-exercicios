import math
def jaca_wars(velocidade, angulo):
    d = velocidade**2 * (math.sin(2 * (angulo))) / 9.8
    return d

    if 99 < d < 101:
        print('Acertou!')
    elif d < 99:
        print('Muito perto')
    elif d > 101:
        print('Muito longe')