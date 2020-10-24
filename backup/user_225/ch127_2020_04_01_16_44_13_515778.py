import math
x = 0
def calcula_elongacao(A, w, t, n):
    x = A*math.cos(math.degrees(n) + (math.degrees(w)*t))
    return x