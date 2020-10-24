import math
def calcula_elongacao (A, f0, om, t):
    x = A * (math.cos(math.radians(f0) + math.radians(om) * t))
    return x