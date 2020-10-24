import math

def calcula_gaussiana (x, mi, sig):
    a = 1 / (sig * math.sqrt(2 * math.pi))
    b = math.e ** (((x - mi) / sig) ** 2 / 2 )
    
    return a * b