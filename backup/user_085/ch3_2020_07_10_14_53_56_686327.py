import math
def calcula_gaussiana(x, mi , sigma):
    pxms = (1/(sigma * (math.sqrt(2 * math.pi)))) * math.e ** ((-1/2) * ((x - mi)/sigma) ** 2)
    return pxms