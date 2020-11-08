import math
def calcula_gaussiana (x,m,o):
    y= 1/o*(2**1/2*math.pi)*math.e**(-0.5*(x-m/o)*2)
    return y