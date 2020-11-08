import math

def calcula_gaussiana(x, mi, sigma):
    return (1/sigma*math.sqrt(2*3.14))*2.71**(-0.5*((x-mi/sigma)**2))