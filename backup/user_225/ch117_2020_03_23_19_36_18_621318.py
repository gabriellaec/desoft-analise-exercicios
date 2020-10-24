import math
def snell_descartes (n1, n2, a1):
    a2 = math.degrees(math.asin ((n1*math.sin(math.radians(a1))/n2)))
    return a2