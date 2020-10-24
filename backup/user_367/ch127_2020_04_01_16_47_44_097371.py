import math
def calcula_elongacao (A, t0, omega, t):
    x = A * (math.degrees(math.asin(math.cos(math.radians(t0 + omega))*t)))
    return x