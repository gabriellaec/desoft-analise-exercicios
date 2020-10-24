from math import radians, cos
def calcula_elongacao(A,o,w,t):
    o0 = radians(o)
    w0 = radians(w)
    x=A*(cos(o0+(w0*t)))
    return x