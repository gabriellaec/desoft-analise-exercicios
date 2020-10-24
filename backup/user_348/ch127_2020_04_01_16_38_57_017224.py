import math
def calcula_elongacao (A, o, w, t):
    a = math.radians(o)
    b = w*0.01745329251994
    x = A*math.cos(a + b*t)
    return x