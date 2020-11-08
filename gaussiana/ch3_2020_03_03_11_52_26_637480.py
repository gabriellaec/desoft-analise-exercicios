# Cálcula gaussiana
import math
def calcula_gaussiana(x,u,o):
    a = o*(math.sqrt(2*math.pi))
    b = 2.71828
    c = (-0.5)*((x - u)/(o))**2
    return (1/a)*(b**c)
print(calcula_gaussiana(1,2,3))