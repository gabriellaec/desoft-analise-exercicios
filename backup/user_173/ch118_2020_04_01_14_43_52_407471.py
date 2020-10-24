from math import *

def snell_descartes (n1,n2,o1):
    a = (n1/n2)*sin(radians(o1))
    o2 = degrees(asin(a))
    return o2

def reflexao_total_interna (n1,n2,o2):
    o1 = snell_descartes (n2,n1,o2)
    if o1 > 90:
        return True
    else:
        return False
    
   