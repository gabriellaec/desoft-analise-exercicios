import math
def calcula_gaussiana (x, mi, si):
    a = 1 / (si * sqrt(2*pi))
    b = exp(-0.5*((x-mi)/si)**2)
    resultado = a*b
    return resultado
    