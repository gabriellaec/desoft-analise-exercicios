import math
def calcula_gaussiana (x,u,s):
    f=1/(s*math.sqrt(2*math.pi))*math.exp(-0.5*((x-u)/s)**2)
    return f