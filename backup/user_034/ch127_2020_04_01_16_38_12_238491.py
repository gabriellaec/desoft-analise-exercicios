import math
def calcula_elongacao(A,graus,w,t):
    b = math.radians(graus + w *t)
    x = A * math.cos(b)
    return x