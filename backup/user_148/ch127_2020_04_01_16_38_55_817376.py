import math

def calcula_elongacao(A, k0, w, t):
    x = A*(math.cos(k0+w*t))
    return x