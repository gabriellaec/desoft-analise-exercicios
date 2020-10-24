import math
x = 0
def calcula_elongacao(A, n, w, t):
    return A*math.cos(math.radians(n) + (math.radians(w)*t))