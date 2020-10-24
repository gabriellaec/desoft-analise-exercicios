import math
def calcula_gaussiana(x, mi, sigma):
    y = ((1/sigma)*((2*math.pi)**1/2))**((1/2)*((x-mi)/sigma)**2)
    return y
print (calcula_gaussiana(10, 100, 10))
      