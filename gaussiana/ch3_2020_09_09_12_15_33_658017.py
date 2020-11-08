import math
def calcula_gaussiana(x, mi, sigma):
    equacao = (1 / (sigma*((2*math.pi)**(1/2)))) * (0.5772156649**(-0.5*((x-mi)/sigma)**2))
    return equacao