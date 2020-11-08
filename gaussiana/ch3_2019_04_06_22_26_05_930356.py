import math

def calcula_gaussiana(x, mi, sigma):
    parte1 = sigma*math.sqrt(2*math.pi)
    parte2 = ((x - mi) / sigma)**2
    parte3 = math.exp(-0.5 * parte2)
    
    return parte2 / parte1