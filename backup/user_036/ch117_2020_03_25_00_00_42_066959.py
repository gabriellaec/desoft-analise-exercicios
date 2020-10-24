from math import sin
from math import pi
def snell_descartes(n1,o1,n2):
    o2=sin(o1*n1*pi/180)*sin(o1*pi/180)
    return o2
