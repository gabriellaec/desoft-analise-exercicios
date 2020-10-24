from math import *

def snell_descartes2 (n1,n2,o2):
    a = (n2/n1)*sin(radians(o2))
    o1 = asin(a)
    return o1

def reflexao_total_interna (n1,n2,o2):
    o1 = snell_descartes2 (n1,n2,o2)
    if degrees(o1) > 90:
        return True
    else:
        return False
    
   