import math
def snell_descartes(n1,n2,o):
    x = (n1 * math.sin(o))/ n2 
    o2= math.radians(x)
    return o2