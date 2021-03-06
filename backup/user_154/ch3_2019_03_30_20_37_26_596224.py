import math

def calcula_gaussiana(x, mi, sigma):
    if sigma == 0:
        return -1
    if sigma == 1/math.sqrt(2*math.pi):
        return 0
    return (1/sigma*math.sqrt(2*math.pi))*math.exp(-0.5((x - mi)/sigma)**2)