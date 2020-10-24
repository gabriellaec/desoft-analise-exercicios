import math
def calcula_elongacao(A,p,w,t):
    w*=(math.pi)/180
    p*=(math.pi)/180
    cos=math.cos(p+w*t)
    x = A*cos
    return x