# Cálcula gaussiana
import math
def calcula_gaussiana(x,u,o):
    a = 1
    b = o*(2*math.pi)**1/2
    c = math.e
    d = ((-0.5)*((x-u)/(o))**2)
    return ((a)/(b))*c**(d)
print(calcula_gaussiana(10,10,5))
