import math
def calcula_gaussiana(x,m,s):
    a=(2*math.pi)**(0.5)
    b=(x-m)/s
    c=b**2
    d=(-0.5)*c
    e=math.e
    f=e**d
    g=f/a
    return g