import math
def snell_descartes(n1,n2,o1):
    o2 = (n1/n2)*math.sin(math.radians(o1))
    g = math.asin(o2)
    return math.degrees(g)