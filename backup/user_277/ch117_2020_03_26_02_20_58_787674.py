import math
def snell_descartes(n1,n2,o1):
    o2=math.asin((math.sin(o1)*n1)/n2)
    k=o2*math.pi/180
    return k