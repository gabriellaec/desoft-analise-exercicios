from math import sqrt, e, pi

def calcula_gaussiana(x, mi, sigma):
    
    expoente = -0.5 * ((x - mi) / sigma) ** 2
    
    return (1 / (sigma * sqrt(2 * pi))) * e ** expoente