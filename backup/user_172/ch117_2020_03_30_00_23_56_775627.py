import math
def snell_descartes (n1, n2, o1):
    y = math.sin(math.radians(o1))
    o2 = math.asin(n1*y/n2)
    return math.degrees(o2)