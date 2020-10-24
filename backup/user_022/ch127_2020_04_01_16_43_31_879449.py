from math import radians, cos
def calcula_elongacao(A,o,w,t):
    o = radians(o)
    w = radians(w)
    x = A*(cos(o+(w*t)))
    return x