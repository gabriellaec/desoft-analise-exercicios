# Cálcula gaussiana
import math
def calcula_gaussiana(x,u,o):
    a = 1
    b = o*(2*math.pi)**1/2
    c = 2.71828
    d = ((-0.5)*((x-u)/(o))**2)
    return ((a)/(b))*c**(d)
print(calcula_gaussiana(0,0,1))
