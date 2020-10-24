import math
def snell_descartes(n1,n2,t1):
    a=(t1*math.pi)/180
    b=math.sin(a)
    y=(b*n1)/n2
    t2=math.asin(y)
    return math.degrees(t2)