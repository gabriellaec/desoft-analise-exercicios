import math
def snell_descartes(n1,n2,o):
    o2 = math.asin((n1 * math.sin(math.radians(o)))/ n2)
    graus = math.degrees(o2)
    return graus