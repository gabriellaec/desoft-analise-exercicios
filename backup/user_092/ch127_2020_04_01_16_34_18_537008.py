import math
def calcula_elongacao(A,o,w,t):
    radianos = math.radians(o +w * t)
    x = A * math.cos(radianos)