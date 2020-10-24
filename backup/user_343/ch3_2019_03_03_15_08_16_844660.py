import math
def calcula_gaussiana(x, mi, sigma):
    y = ((1/sigma)*((2*math.pi)**0.5))**((0.5)*((x-mi)/sigma)**2)
    return y
print (calcula_gaussiana(1, 1, 1))
      