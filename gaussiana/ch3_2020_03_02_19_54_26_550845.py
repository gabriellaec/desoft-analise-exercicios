import math
def calcula_gaussiana(x, mi, sigma):
    a = 1/(sigma * (math.sqrt(2 * math.pi)))
    c= (-0.5 * (((x-mi)/sigma)**2))
    z = a * math.e ** c
    return z
