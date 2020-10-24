import math
def calcula_elongacao(A,o,w,t):
    x=A*math.cos(math.radians(o)+(math.radians(w)*t))
    return x
