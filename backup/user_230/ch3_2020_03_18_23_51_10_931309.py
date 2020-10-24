import math
def calcula_gaussiana (x, mi, sigma):
    f1=1/(sigma*math.sqrt(2*math.pi))
    f2=math.e**(-0.5*((x-mi/sigma)**2))
    return (f1*f2)
