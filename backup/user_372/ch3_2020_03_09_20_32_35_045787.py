import math
def calcula_gaussiana(x, mi, sigma):
    c=(1/sigma*2*math.pi**(1/2))*2,71**(-1/2*((x−mi)/sigma)**2)
    return c

