import math
def jacawars(angulo,v):
    convert = math.radians(angulo)
    d = v**2*(math.sin(convert))/9.8
    if d>=98 and d<102:
        return 'Acertou!'
    if d<98:
        return'Muito perto'
    if d>102:
        return 'Muito longe'