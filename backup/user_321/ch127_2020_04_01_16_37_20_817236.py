import math
def calcula_elongacao(A, fi, w, t):
    x = A*math.cos(math.radians(fi) + math.radians(w)*t)
    return x