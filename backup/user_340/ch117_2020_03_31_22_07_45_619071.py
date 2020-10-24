import math
def snell_descartes(n1,n2,t1):
    a=(t1*math.pi)/180
    t2=((math.sin(a))*n1)/n2
    return math.degrees(t2)