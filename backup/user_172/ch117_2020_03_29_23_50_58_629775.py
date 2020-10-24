import math
def snell_descartes (n1, n2, o1):
    x = math.radians(o2)
    y = math.sin(math.radians(o1))
    x = math.asin(n1*y/n2)
    return math.degrees(o2)