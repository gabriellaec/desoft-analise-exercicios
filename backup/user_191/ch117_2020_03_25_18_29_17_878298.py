import math
def snell_descartes(n1,n2,t1):
    a=(t1*180)/math.pi
    t2=math.asin((math.sin(a)*n1)/n2)
    return t2