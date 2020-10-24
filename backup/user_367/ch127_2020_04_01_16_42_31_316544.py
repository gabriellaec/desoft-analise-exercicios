import math
def calcula_elongacao (a, t0, w, t):
    x = a * math.degrees(math.asin(math.cos(math.radians(t0 + w * t))))
    return x