import math
def calcula_gaussiana(x,mi,sigma):
    calculo=((1/(sigma*(2*math.pi))))*math.exp(-0.5*(x-mi/sigma)**2)
    return calculo
