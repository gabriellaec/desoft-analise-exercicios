import math
def snell_descartes(n1,n2,t1):
    t2=(math.sin(t1)*n1)/n2
    return math.radians(t2)