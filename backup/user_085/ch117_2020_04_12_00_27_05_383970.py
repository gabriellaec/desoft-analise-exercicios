import math
def snell_descartes(n1,n2,o1):
    r = math.radians((n1/n2) * math.sin(math.radians(o1)))
    o2 = math.asin(r)
    return math.degrees(o2)