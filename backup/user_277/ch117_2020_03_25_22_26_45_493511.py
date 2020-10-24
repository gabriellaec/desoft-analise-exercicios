import math
def snell_descartes(n1,n2,o1):
    a=(n1*math.sin(o1*180)/math.pi)/n2
    o2=180*math.asin(a)/math.pi
    return o2