import math
def calcula_elongacao(A,p,w,t):
    p*=(math.pi)/180
    cos=(p+w*t)
    x = A*cos
    return x