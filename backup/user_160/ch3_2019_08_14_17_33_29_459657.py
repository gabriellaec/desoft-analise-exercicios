import math
def calcula gaussiana(x, mi, sigma):
    f = (1 / (sigma*(2*math.pi)))**(-0,5*((x-mi)/sigma)**2)
    return f