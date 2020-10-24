import math
def calcula_elongacao (A, t0, omega, t):
    x = A * (math.cos(t0 + omega))*t
    return x