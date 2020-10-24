from math import sin
from math import degrees
def snell_descartes(n1,n2,o1):
    o2=sin(degrees(n1*sin(degrees(o1))/n2))
    return o2
print(snell_descartes(1,2,30))