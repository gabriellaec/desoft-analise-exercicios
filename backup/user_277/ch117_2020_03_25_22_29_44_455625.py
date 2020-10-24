import math
def snell_descartes(n1,n2,o1):
    p=math.pi
    a=(n1*math.sin(o1*180)/p)/n2
    o2=180*math.asin(a)/p
    return o2