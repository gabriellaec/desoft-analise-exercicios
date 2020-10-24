import math
def calcula_gaussiana(x,u,o):
    A=(1/(o*math.sqrt(2*math.pi)))
    y=A*math.e**(-0.5*((x-u)/o)**2)
    return y
