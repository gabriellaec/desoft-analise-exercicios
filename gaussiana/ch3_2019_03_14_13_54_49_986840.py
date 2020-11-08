import math
def calcula_gaussiana (x,mi,sigma):
    a = (1 / sigma * (2 * math.pi) ** 1/2) * math.exp(-0,5 * (x - sigma/mi)**2)
    return a