import math
def jaca_wars(velocidade, angulo):
    d = velocidade**2 * math.sin(2 * (math.radians(angulo))) / 9.8
    return d

    if 98 < d < 102:
        print('Acertou!')
    elif d < 98:
        print('Muito perto')
    elif d > 102:
        print('Muito longe')