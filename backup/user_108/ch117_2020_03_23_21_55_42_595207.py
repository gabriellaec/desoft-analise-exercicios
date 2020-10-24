import math
def snell_descartes(n1,n2,a1):
    return math.asin(n1 * math.sin(a1) / n2)