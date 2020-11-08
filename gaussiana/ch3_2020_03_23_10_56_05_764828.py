import math
def calcula_gaussiana(x,m,s):
    a=(2*3.14159265359)**-0.5
    b=(x-m)/s
    c=b**2
    d=-0.5*c
    e=2.71828182845904523
    f=e**d
    g=f/a
    return g