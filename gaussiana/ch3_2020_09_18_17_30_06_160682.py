import math

def calcula_gaussiana(x,mi,sigma):
    euler = math.exp(-0.5 * (x-mi/sigma)**2)
    raiz = sigma * math.sqrt(2*math.pi)
    conta = (1 / raiz) * euler 
    return conta