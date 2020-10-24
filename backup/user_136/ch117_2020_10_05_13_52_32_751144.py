import math
def snell_descartes(n1, n2, o1):
    k= math.sin
    o2= math.asin((n1 * k(math.radians(o1))) /n2)
    f= (180/math.pi)*o2
    return f
    