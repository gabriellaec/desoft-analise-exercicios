import math
def jaca(v, o):
    d = (((v**2)*math.sin*(2*o))/9.8)
    if d < 98:
        return ("Muito perto")
    elif d >= 98 and d <= 102:
        return ("Acertou!")
    else:
        return ("Muito longe")