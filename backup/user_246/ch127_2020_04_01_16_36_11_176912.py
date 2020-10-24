import math
def calcula_elongacao(A, o, w, t):
    o=math.radians(o)
    w=math.radians(w)
    x=A*math.cos(o+w*t)
    return x