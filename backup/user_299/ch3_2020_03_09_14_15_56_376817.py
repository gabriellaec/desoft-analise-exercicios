import math

def calcula_gaussiana(x, m, s):
    f=(1/(s*(math.sqrt(2*math.pi))))*math.e**(-0.5*(((x-m)/s)**2))
    return f

i=(math.sqrt(1/2*math.pi))
 

print(calcula_gaussiana(0, 0, 1))
print(calcula_gaussiana(0, i, i))
print(calcula_gaussiana(1, 1, i))
print(calcula_gaussiana(1, 1, 1))