import math
def snell_descartes(n1,n2,o):
    o2 = math.asin((n1 * math.sin(math.degrees(o)))/ n2) 
    return graus