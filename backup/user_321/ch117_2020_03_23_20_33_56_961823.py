import math
def snell_descartes(n1,n2,o1):
    o2 = math.sin(math.sin(o1)*n1/n2)
    return o2