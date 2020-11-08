import math
print(math.pi)
print(math.e)
print(math.sqrt)
def calcula_gaussiana (x, mi, sigma):
    f=1/(sigma*(2*math.pi)**1/2)*math.e**(-0.5*(x-mi/sigma)**2)
    return f
print(calcula_gaussiana(0,1/math.sqrt(2*math.pi),1/math.sqrt(2*math.pi))
print(calcula_gaussiana(0,0,1))
print(calcula_gaussiana(0,0,1/math.sqrt(2*math.pi)))

