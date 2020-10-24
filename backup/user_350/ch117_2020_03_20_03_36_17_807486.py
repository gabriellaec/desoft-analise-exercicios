from math import sin
from math import pi
from math import asin

x1=float(input("valor de x1"))

def radianos(x1): 
    y = (pi*x1)/180   
    return y

def graus(x1): 
    y = (180*x1)/pi   
    return y
a = asin((n1/n2)*sin(radianos(x1)))
print (graus(a))
