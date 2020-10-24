import math
def calcula_elongacao (A, t0, w, t):
    x = A * (math.degrees(math.asin(math.cos(math.radians(t0 + w))*t)))
    return x