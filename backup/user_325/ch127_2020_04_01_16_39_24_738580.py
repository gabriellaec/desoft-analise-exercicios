import math
def calcula_elongacao(a, O0, w, t):
    b = math.degrees(O0)
    c = a*math.cos(b+w*t)
    return c