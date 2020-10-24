import math

def calcula_elongacao(A,O,w,t):
    a = w*t
    b = a + O
    c = math.radians(b)
    d = math.cos(c)
    x = A*d
    return x