from math import radians, cos
def calcula_elongacao(A, W, t, O):
    O0 = radians(O)
    W0 = radians(W)
    x = A*(cos(O0 + (W0*t)))
    return x
