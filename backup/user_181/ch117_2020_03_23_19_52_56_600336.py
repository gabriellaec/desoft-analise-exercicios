import math
def snell_descartes(n1,n2,a1):
    a2 = n1/n2 * math.sin(math.radians(a1))
    return math.radians(a2)
