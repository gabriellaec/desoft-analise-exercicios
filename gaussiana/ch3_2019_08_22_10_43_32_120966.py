import math
def calcula_gaussiana(x,m,s):
    den = s * (2 * math.pi)**0.5
    pot = -0.5 *((x-m)/s)**2
    valor = 1/den*math.exp(pot)
    return valor