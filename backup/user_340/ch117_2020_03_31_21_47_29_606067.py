import math
def snell_descartes(n1,n2,t1):
    t1=math.degrees(t1)
    a=math.radians(t1)
    t2=(math.sin(a)*n1)/n2
    return math.degrees(t2)