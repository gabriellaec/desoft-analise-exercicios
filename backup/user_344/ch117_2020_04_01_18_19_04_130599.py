from math import *
def snell_descartes(n1,n2,teta1):
    a = (n1/n2)*math.sin(radians(teta1))
    teta2 = degrees(asin(a))
    return teta2
    
