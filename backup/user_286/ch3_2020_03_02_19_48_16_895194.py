import math

def calcula_gaussiana(x, mi, sigma):
    gauss = (1/math.sqrt((math.pi)*2))*((math.e)**(-0.5*math.sqrt((x-mi)/sigma)))
    return gauss