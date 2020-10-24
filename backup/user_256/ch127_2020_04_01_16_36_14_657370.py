import math
def calcula_elongacao(A, i, v, t):
    x = A*math.cos(math.radians(i)+(math.radians(v)*t))
    return x