import math
def snell_descartes(n1,n2,o1):
    r = math.degrees((n1/n2) * math.sin(math.degrees(o1)))
    o2 = math.asin(r)
    return math.degrees(o2)