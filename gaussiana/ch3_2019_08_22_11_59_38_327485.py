import math
def calcula_gaussiana(x, mi, sigma):
    denominador=sigma*(2*math.pi)**0.5
    potencia=(-0.5*((x-mi)/sigma)**2)
    gau=(1/denominador)*math.exp(potencia)
    return gau

x=calcula_gaussiana(100, 5, 10)
print(x)
