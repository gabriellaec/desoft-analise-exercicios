import math
def calcula_gaussiana(x,mi,sig):
    return (1/(sig*math.sqrt(2*math.pi))) * math.exp**(-0.5*((x - mi)/sig)**2)