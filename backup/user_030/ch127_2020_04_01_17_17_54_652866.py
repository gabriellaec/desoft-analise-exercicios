from math import radians, cos
def calcula_elongacao(A, O, W, t):
    O0 = radians(O)
    W0 = radians(W)
    x = A*(cos(O0 + (W0*t)))
    return x
