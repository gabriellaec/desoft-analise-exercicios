import math
def snell_descartes(n1,n2,t1):
    a=(t1*math.pi)/180
    b=math.sin(a)
    t2=(b*n1)/n2
    return math.degrees(t2)