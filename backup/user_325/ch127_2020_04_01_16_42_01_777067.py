import math
def calcula_elongacao(a, O0, w, t):
    b = math.radians(O0)
    c = math.radians(w)
    d = a*math.cos(b+c*t)
    return d