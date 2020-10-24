from math import *

def snell_descartes (n1,n2,o1):
    a = (n1/n2)*sin(radians(o1))
    o2 = degrees(asin(a))
    return o2

