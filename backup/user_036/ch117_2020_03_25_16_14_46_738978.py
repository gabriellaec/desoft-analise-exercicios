from math import degrees
from math import sin
from math import radians
def snell_descartes(n1,n2,o1):
    x = n1/n2 * sin(radians(o1))
    y = sin(x)
    o2= degrees(y)
    return o2