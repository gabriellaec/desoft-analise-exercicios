from math import radians, cos
def calcula_elongacao(O,A,T,W):
    O0 = randians(O)
    W0 = randians(W)
    x = A*(cos(O0+(W0*T)))
    return x