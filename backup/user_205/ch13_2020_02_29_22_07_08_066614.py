import math

def encontra_cateto (a,b):
    c = math.sqrt(a*a - b*b)
    return c
print (encontra_cateto(5,4))