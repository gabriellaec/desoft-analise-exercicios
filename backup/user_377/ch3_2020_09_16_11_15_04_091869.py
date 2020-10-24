import math
def calcula_gaussiana (x, mi, sigma):
    gaussiana = math.exp ((-0.5 * ((x - mi)/ sigma)**2))/ (sigma *((2 * math.pi)**0.5))
    return guassiana

