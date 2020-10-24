import math

def calcula_elongacao(A,p,w,t):
    c=p+w*t
    x=A*math.cos(math.radians(c))
    return x