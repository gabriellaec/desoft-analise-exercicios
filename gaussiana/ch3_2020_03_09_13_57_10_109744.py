import math

def calcula_gaussiana(x, mi, sigma):
    f=(1/sigma*math)*(sqrt(2*math.pi))*math.e**(-0.5*(((x-mi)/sigma)**2))
    return f

print(calcula_gaussiana(0, 0, 1))
print(calcula_gaussiana(0, 0.3989, 0.3989))
print(calcula_gaussiana(1, 1, 1))
print(calcula_gaussiana(10000, -10000, 0.1))
