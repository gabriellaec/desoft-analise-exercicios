import math
def snell_descartes (n1,n2,t1):
    a=math.degrees(math.asin(n1*math.sin(math.radians(t1))))
    t2=a/n2
    return t2
