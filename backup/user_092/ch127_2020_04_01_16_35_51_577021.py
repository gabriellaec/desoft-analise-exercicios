import math
def calcula_elongacao(A,o,w,t):
    cos = o +w*t
    radianos = math.radians(cos)
    x = A * math.cos(radianos)
    return x