import math
def jacawars(angulo,v):
    d = (v**2*math.sin(angulo))/9.8
    if d>=98 and d<102:
        return 'Acertou!'
    if d<98:
        return'Muito perto'
    if d>102:
        return 'Muito longe'