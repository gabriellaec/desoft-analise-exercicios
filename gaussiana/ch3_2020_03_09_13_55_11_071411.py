import math
def calcula_gaussiana (x,u,o):
    calcula_gaussiana = (1/(o*(2*math.pi)**(1/2)))*math.e**(-0.5*((x-u)/o)**2)
    return calcula_gaussiana