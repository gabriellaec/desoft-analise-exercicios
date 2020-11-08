# Cálcula gaussiana
import math
def calcula_gaussiana(x,u,o):
    a = o*(math.sqrt(2*math.pi))
    b = math.e
    c = (((x - u)/(o))**2)*(-0.5)
    return (b**c)/(a)
print(calcula_gaussiana(1,2,3))