import math
def snell_descartes(n1,n2,a1):
    A = ((math.sin((math.radians)*n1)))
    B = ((math.sin((math.radians)*n2)))
    a2 = a1 * A/B
    return a2
