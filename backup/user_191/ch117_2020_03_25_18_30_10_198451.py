import math
def snell_descartes(n1,n2,t1):
    a=(t1*180)/math.pi
    b=(t2*180)/math.pi
    b=math.asin((math.sin(a)*n1)/n2)
    return t2