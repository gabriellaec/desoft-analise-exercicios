import math
def snell_descartes(n1, n2, o1):
    k= math.sin
    o2= math.asin((n1 * k(o1))/n2)
    return o2
    