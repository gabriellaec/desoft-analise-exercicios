import math
def calcula_gaussiana (x, mi, o):
    resultado = (1/o*math.sqrt(2*math.pi))**(-0.5*(x-mi/o)**2)
    return resultado