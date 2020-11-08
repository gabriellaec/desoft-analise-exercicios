import math
print(math.pi)
print(math.e)

def calcula_gaussiana (x, mi, sigma):
    f1=1/(sigma*math.sqrt(2*math.pi))
    f2=math.e**(-0.5*((x-mi/sigma)**2))
    return (f1*f2)
print(calcula_gaussiana(0,1/math.sqrt(2*math.pi),1/math.sqrt(2*math.pi))
print(calcula_gaussiana(0,0,1))
print(calcula_gaussiana(0,0,1/math.sqrt(2*math.pi)))

