import math
def snell_descartes(n1,n2,o1):
    p=math.pi
    sin=math.sin
    asin=math.asin
    a=(n1*sin(o1*180)/p)/n2
    o2=180*asin(a)/p
    return o2