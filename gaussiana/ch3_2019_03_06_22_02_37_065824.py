import math
def calcula_gaussiana(x,mi,sigma):
    gauss = (1/sigma*(2*math.pi)**0,5)**(-0,5*((x - mi)/sigma)**2)
    return gauss
a = calcula_gaussiana(2,2,1)
print(a)