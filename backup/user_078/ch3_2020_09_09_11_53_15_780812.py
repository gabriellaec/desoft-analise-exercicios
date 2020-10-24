import math
def calcula_gaussiana (x, mi, o):
    
    a = 1/o*math.sqrt(2*math.pi)
    b = -0.5 * ((x - mi)/o)**2

    resultado = a**b
    return resultado