import math as mt
def area_pentagono(l):
    x=mt.radians(36)
    y=mt.tan(x)
    a=(l/2)/y
    A=(a*l*5)/2
    return A
l=4
q=area_pentagono(l)
print(q)