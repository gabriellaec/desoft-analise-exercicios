import math
def calcula_gaussiana(x, mi, sigma):
    y = ((1/sigma)*((2*math.pi)**1/2))**((1/2)*((x-mi)/sigma)**2)
    return y
x = 10
mi = 10
sigma = 10
print (calcula_gaussiana(x, mi, sigma)
      