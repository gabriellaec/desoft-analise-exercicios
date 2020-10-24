from math import radians, cos
def calcula_elongacao(O,A,T,W):
    O0 = radians(O)
    W0 = radians(W)
    x=A*(cos(O0+(W0*T)))
    return x