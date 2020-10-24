import math
def jaca(velocidade, angulo):
    d = (velocidade*velocidade*math.sin((math.radians(angulo))))/9.8
    if d < 98:
        return 'Muito perto'
    elif d > 98 and d <= 102:
        return 'Acertou!'
    else:
        return 'Muito longe'