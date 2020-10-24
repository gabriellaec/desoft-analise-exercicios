import math
def calcula_elongacao(A, o, w, t):
    o=math.radiant(o)
    w=math.radiant(w)
    x=A*math.cos(o+t)
    return x