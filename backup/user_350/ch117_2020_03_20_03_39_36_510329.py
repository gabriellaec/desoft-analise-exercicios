from math import sin
from math import pi
from math import asin


def radianos(x1): 
    y = (pi*x1)/180   
    return y

def graus(x1): 
    y = (180*x1)/pi   
    return y

def snell(n1,n2,x1):
    a = graus(asin((n1/n2)*sin(radianos(x1))))
    return a 



