import math
def calcula_elongacao(A,fi, w, t):
    x=A*math.cos(math.degrees(fi)+(w*t))
    return x