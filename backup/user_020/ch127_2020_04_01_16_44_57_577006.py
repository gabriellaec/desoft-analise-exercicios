import math
def calcula_elongacao(A, t0, w, t):
    x = A*math.cos(math.radians(t0)+(math.radians(w))*t)
    return x