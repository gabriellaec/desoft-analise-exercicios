import math
def calcula_gaussiana (x, mi, sigma):
    y= math.e**((-0.5)*(((x-mi)/sigma))**2)/(sigma*math.sqrt(2*math.pi))
    return y
