import math
def calcula_gaussiana ( x, mi, sigma):
    g = (1/ sigma * (2* math.pi)** 1/2) math.exp (-1/2*(x-mi/sigma)**2)
    return g
