import math
def snell_descartes (n1, n2, ø1):
    y = (n1 * math.sin(ø1)) / n2
    z = math.asin(y)
    return math.degrees (z)