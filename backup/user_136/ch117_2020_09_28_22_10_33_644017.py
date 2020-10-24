import math
def snell_descartes(n1, n2, o1):
    k= math.sin(o2)
    k= (n1 * math.sin(o1))/n2
    return k
    