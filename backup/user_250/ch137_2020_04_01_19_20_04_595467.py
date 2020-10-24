import math
def calcula_aceleracao(r, f):
    fH = f/60
    w = (2*(math.pi))*fH
    ac = (w**2)*r
    return ac