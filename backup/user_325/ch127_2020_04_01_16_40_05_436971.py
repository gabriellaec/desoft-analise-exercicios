import math
def calcula_elongacao(a, O0, w, t):
    b = math.radians(O0)
    c = a*math.cos(b+w*t)
    return c