import math
def snell_descartes(n1, n2, o1):
    o2 = (math.sin(math.radians(o1)))*(n1)/(n2)
    graus_o2 = math.degrees(math.asin(o2))
    return graus_o2