from math import radians, cos

def calcula_elongacao(A, W, t, O):
    W0 = radians(W)
    O0 = radians(O)
    x = A(cos(O0 + (W0*t)))
    return x
