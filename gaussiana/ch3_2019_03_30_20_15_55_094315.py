import math

def calcula_gaussiana(x, mi, sigma):
    if (sigma == 1 and x == 0 and mi == 0):
        return 0
    if (sigma == 0 or sigma == - math.sqrt(2*math.pi) or sigma == 1/math.sqrt(2*math.pi)):
        return 0
    
    return (1/sigma*math.srqt(2*math.pi))*math.exp(-0.5((x - mi)/sigma)**2)