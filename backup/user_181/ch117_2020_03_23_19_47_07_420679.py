import math
def snell_descartes(n1,n2,a1):
    A = ((math.sin(math.pi/180*n1)))
    B = ((math.sin(math.pi/180*n2)))
    a2 = a1 * A/B
    return a2