import math
from math import asin

def radianos(x1):
	a=(x1*math.pi)/180
	return a

def graus(x2):
    b=(180*x2)/math.pi
    return b
def snell_descartes(n1,n2,x):
    
	y=graus*(math.asin(n1/n2)*math.sin(math.radians(x))
	return y