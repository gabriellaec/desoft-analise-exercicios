from math import *
def snell_descartes(n1,n2,t1) :
    t1 = radians(t1)
    t2 = asin((n1 + sin(t1))/n2)
    t2 = degrees(t2)
    return t2
    
    
