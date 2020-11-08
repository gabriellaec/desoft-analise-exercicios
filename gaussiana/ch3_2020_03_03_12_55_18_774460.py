import math
def calcula_gaussiana (x,u,s):
    f=1/s(2*math.pi)**1/2*math.e**(-0.5*((x-u)/s)**2)
    return f