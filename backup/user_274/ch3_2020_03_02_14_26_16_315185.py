import math

def calcula_gaussiana(x,u,sig):
    f = (1/(sig*math.sqrt(2*math.pi)))*math.exp(-0.5*((x-u)/sig)**2)
    return f
