import math
def snell_descartes(n1,n2,a1):
    a2 = a1/(math.sin(math.radians(n1))/math.sin(math.radians(n2)))
    return a2
