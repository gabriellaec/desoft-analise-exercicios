from math import degrees
from math import sin
from math import radians
from math import asin
def snell_descartes(n1,n2,o1):
    x = sin(radians(o1)) * n1/n2
    y = asin(x)
    o2= degrees(y)
    return o2

print(snell_descartes(1,2,30))