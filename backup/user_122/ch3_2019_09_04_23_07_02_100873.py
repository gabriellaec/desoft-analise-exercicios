import math

def calcula_gaussiana(x, mi, sigma):
    denominador = sigma*(2*math.pi)**0.5
    numerador = math.exp(-0.5*((x - mi)/sigma)**2)
    gauss = numerador / denominador
    return gauss