import math
def snell_descartes(n1,n2,o1):
    r = (n1 * math.sin(math.radians(o1)))/n2
    o2 = math.asin(r)
    return math.degrees(o2)