import math
def snell_descartes(n1,n2,o1):
    r1=(o1*math.pi)/180
    r2=math.asin(n1*math.sin(r1)/n2)
    o2= r2*180/math.pi
    return o2
