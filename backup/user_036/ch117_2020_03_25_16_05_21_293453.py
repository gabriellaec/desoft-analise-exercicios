from math import sin
from math import radians
def snell_descartes(n1,n2,o1):
    o2=n1*sin(radians(o1))/n2
    return sin(radians(o2))
print(snell_descartes(1,2,30))