import math
def calcula_elongacao(A,fi, w, t):
    x=A*math.acos(math.radians(fi)+(w*t))
    return x