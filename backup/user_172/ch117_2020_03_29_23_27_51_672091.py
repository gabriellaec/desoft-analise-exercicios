import math
def snell_descartes (n1, n2, o1):
    x = math.radians(o2)
    x = math.asin(n1*math.sin(math.radians(o1))/n2)
    x == math.degrees(o2)
    return x