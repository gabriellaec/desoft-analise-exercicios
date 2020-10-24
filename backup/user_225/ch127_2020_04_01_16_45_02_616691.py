import math
x = 0
def calcula_elongacao(A, n, w, t):
    x = A*math.cos(math.degrees(n) + (math.degrees(w)*t))
    return x