import math
def calcula_elongacao(A,o0,w,t):
    x=A*math.cos(math.radians(o0)+math.radians(w)*t)
    return x