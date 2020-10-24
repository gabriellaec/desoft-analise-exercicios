from math import sin
from math import pi

def jaca(v, a):
    o = (a/180)* pi
    d = ((v**2)*sin(2*o))/9.8
    if d < 98:
        return("Muito perto")
    elif d > 102:
        return("Muito longe")
    else:
        return("Acertou!")
    v = float(input("Velocidade"))
    a = float(input("angulo"))