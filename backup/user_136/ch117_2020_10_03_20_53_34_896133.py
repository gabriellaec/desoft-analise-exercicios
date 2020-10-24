import math
def snell_descartes(n1, n2, o1):
    k= math.sin
    pi= math.pi
    o2= math.asin((n1 * k(o1))/n2)
    graus= (180/pi)*o2
    return graus
    