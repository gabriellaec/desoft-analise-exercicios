import math
def snell_descartes(n1,n2,o1):
 
    o2=180*math.asin(n1*math.sin(o1*180/math.pi)/n2)/math.pi
    return o2