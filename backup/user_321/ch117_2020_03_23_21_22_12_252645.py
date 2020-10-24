import math
def snell_descartes(n1,n2,o1):
    r = math.sin(math.radians(o1))*n1/n2
    o2 = math.asin(r)
    return math.degrees(o2)