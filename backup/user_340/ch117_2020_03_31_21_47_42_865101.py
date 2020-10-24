import math
def snell_descartes(n1,n2,t1):
    c=math.degrees(t1)
    a=math.radians(c)
    t2=(math.sin(a)*n1)/n2
    return math.degrees(t2)