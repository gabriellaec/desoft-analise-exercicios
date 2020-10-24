import math
def snell_descartes(n1,n2,o1):
    return math.degrees((n1 * math.sin(math.radians(o1)))/n2)