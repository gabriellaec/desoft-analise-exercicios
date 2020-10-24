import math
def snell_descartes(n1,n2,o1):
    return math.degrees((n1/n2) * math.sin(math.degrees(o1)))