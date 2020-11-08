import math
def calcula_gaussiana(x, mi, sigma):
    gauss = (1/sigma*(2*math.pi)**1/2)**(-0,5*(x - mi/sigma)**2)
    return gauss
a = calcula_gaussiana(1.000.000, -1.000.000, 0,1)
print(a)
