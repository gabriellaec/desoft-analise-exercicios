import math

def calcula_elongacao(A, k0, w, t):

    x = A*(math.cos(math.radians(k0)+math.radians(w*t)))
    return x